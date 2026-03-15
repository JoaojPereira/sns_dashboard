# Como Criar a Tabela DimCalendar no Power BI

## Visão Geral
Este guia explica como criar a tabela de dimensão calendário (DimCalendar) no Power BI usando código M (Power Query). Esta tabela é essencial para análises temporais e inclui feriados nacionais de Portugal.

## Características da Tabela
A DimCalendar inclui:
- **Período**: 01/01/2016 a 31/12/2026
- **Chave primária**: TimeKey (formato: YYYYMMDD)
- **Hierarquia temporal**: Ano > Trimestre > Mês > Dia
- **Sazonalidade**: Baseada em hemisfério norte (Portugal)
- **Feriados**: Feriados nacionais portugueses (fixos e móveis)
- **Tipos de dia**: Dia Útil, Fim de Semana, Feriado

## Passo a Passo

### 1. Abrir o Editor do Power Query
1. No Power BI Desktop, clique em **Transformar Dados** ou **Editar Consultas**
2. No Editor do Power Query, clique em **Nova Origem** > **Consulta em Branco**

### 2. Abrir o Editor Avançado
1. Com a nova consulta selecionada, clique em **Visualização** > **Editor Avançado**
2. Delete todo o código existente

### 3. Colar o Código M
Cole o seguinte código M completo:

```m
let
    // Parâmetros de data
    StartDate = #date(2016, 1, 1),
    EndDate = #date(2026, 12, 31),
    
    // Criar lista de datas
    DayCount = Duration.Days(Duration.From(EndDate - StartDate)) + 1,
    Source = List.Dates(StartDate, DayCount, #duration(1,0,0,0)),
    TableFromList = Table.FromList(Source, Splitter.SplitByNothing()),
    
    // Renomear e adicionar colunas essenciais
    ChangedType = Table.TransformColumnTypes(TableFromList,{{"Column1", type date}}),
    RenamedColumns = Table.RenameColumns(ChangedType,{{"Column1", "Data"}}),
    
    // TimeKey - Chave para relacionamentos
    AddTimeKey = Table.AddColumn(RenamedColumns, "TimeKey", each 
        Date.Year([Data]) * 10000 + Date.Month([Data]) * 100 + Date.Day([Data]), 
        Int64.Type),
    
    // Hierarquia temporal: Ano > Trimestre > Mês > Dia
    AddAno = Table.AddColumn(AddTimeKey, "Ano", each Date.Year([Data]), Int64.Type),
    AddTrimestre = Table.AddColumn(AddAno, "Trimestre", each "T" & Number.ToText(Date.QuarterOfYear([Data])), type text),
    AddMes = Table.AddColumn(AddTrimestre, "Mes", each Date.Month([Data]), Int64.Type),
    AddMesNome = Table.AddColumn(AddMes, "MesNome", each Date.ToText([Data], "MMMM", "pt-PT"), type text),
    AddDia = Table.AddColumn(AddMesNome, "Dia", each Date.Day([Data]), Int64.Type),
    AddDiaSemana = Table.AddColumn(AddDia, "DiaSemana", each Date.ToText([Data], "dddd", "pt-PT"), type text),
    
    // Adicionar Sazonalidade (baseado em hemisfério norte - Portugal)
    AddSazonalidade = Table.AddColumn(AddDiaSemana, "Sazonalidade", each 
        let mes = Date.Month([Data])
        in if mes = 12 or mes = 1 or mes = 2 then "Inverno"
           else if mes >= 3 and mes <= 5 then "Primavera"
           else if mes >= 6 and mes <= 8 then "Verão"
           else "Outono",
        type text),
    
    // Coluna auxiliar para ordenação de mês/trimestre
    AddAnoMes = Table.AddColumn(AddSazonalidade, "AnoMes", each 
        Text.From(Date.Year([Data])) & "-" & Text.PadStart(Text.From(Date.Month([Data])), 2, "0"), 
        type text),
    
    // É Fim de Semana (Sábado ou Domingo)
    AddFimDeSemana = Table.AddColumn(AddAnoMes, "É Fim de Semana", each 
        Date.DayOfWeek([Data], Day.Monday) >= 5, 
        type logical),
    
    // É Feriado (Feriados Nacionais de Portugal)
    AddFeriado = Table.AddColumn(AddFimDeSemana, "É Feriado", each 
        let 
            ano = Date.Year([Data]),
            mes = Date.Month([Data]),
            dia = Date.Day([Data]),
            
            // Calcular Páscoa (Algoritmo de Meeus/Jones/Butcher)
            a = Number.Mod(ano, 19),
            b = Number.IntegerDivide(ano, 100),
            c = Number.Mod(ano, 100),
            d = Number.IntegerDivide(b, 4),
            e = Number.Mod(b, 4),
            f = Number.IntegerDivide(b + 8, 25),
            g = Number.IntegerDivide(b - f + 1, 3),
            h = Number.Mod(19 * a + b - d - g + 15, 30),
            i = Number.IntegerDivide(c, 4),
            k = Number.Mod(c, 4),
            l = Number.Mod(32 + 2 * e + 2 * i - h - k, 7),
            m = Number.IntegerDivide(a + 11 * h + 22 * l, 451),
            mesPascoa = Number.IntegerDivide(h + l - 7 * m + 114, 31),
            diaPascoa = Number.Mod(h + l - 7 * m + 114, 31) + 1,
            dataPascoa = #date(ano, mesPascoa, diaPascoa),
            
            // Feriados móveis baseados na Páscoa
            carnaval = Date.AddDays(dataPascoa, -47),           // 47 dias antes da Páscoa
            sextaFeiraSanta = Date.AddDays(dataPascoa, -2),     // Sexta-feira Santa
            pascoa = dataPascoa,                                 // Domingo de Páscoa
            corpusChristi = Date.AddDays(dataPascoa, 60),       // 60 dias após Páscoa
            
            // Feriados fixos de Portugal
            feriadosFixos = {
                #date(ano, 1, 1),    // Ano Novo
                #date(ano, 4, 25),   // 25 de Abril (Revolução dos Cravos)
                #date(ano, 5, 1),    // Dia do Trabalhador
                #date(ano, 6, 10),   // Dia de Portugal
                #date(ano, 8, 15),   // Assunção de Nossa Senhora
                #date(ano, 10, 5),   // Implantação da República
                #date(ano, 11, 1),   // Todos os Santos
                #date(ano, 12, 1),   // Restauração da Independência
                #date(ano, 12, 8),   // Imaculada Conceição
                #date(ano, 12, 25)   // Natal
            },
            
            // Todos os feriados (fixos + móveis)
            todosFeriados = feriadosFixos & {carnaval, sextaFeiraSanta, pascoa, corpusChristi}
        in
            List.Contains(todosFeriados, [Data]),
        type logical),
    
    // Tipo de Dia (útil, fim de semana ou feriado)
    AddTipoDia = Table.AddColumn(AddFeriado, "Tipo de Dia", each 
        if [É Feriado] then "Feriado"
        else if [É Fim de Semana] then "Fim de Semana"
        else "Dia Útil",
        type text),
    
    // Ordenar por TimeKey
    SortedRows = Table.Sort(AddTipoDia,{{"TimeKey", Order.Ascending}}),
    #"Linhas Filtradas" = Table.SelectRows(SortedRows, each true)
in
    #"Linhas Filtradas"
```

### 4. Renomear a Consulta
1. Clique em **OK** no Editor Avançado
2. No painel esquerdo, clique com o botão direito na consulta
3. Selecione **Renomear** e digite: `DimCalendar`

### 5. Carregar a Tabela
1. Clique em **Fechar e Aplicar** no Editor do Power Query
2. A tabela DimCalendar será carregada no modelo de dados

## Estrutura das Colunas

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| Data | Date | Data completa |
| TimeKey | Int64 | Chave primária (formato YYYYMMDD, ex: 20260101) |
| Ano | Int64 | Ano (ex: 2026) |
| Trimestre | Text | Trimestre (ex: T1, T2, T3, T4) |
| Mes | Int64 | Número do mês (1-12) |
| MesNome | Text | Nome do mês em português (ex: Janeiro) |
| Dia | Int64 | Dia do mês (1-31) |
| DiaSemana | Text | Nome do dia da semana em português (ex: Segunda-feira) |
| Sazonalidade | Text | Estação do ano (Inverno, Primavera, Verão, Outono) |
| AnoMes | Text | Formato YYYY-MM para ordenação (ex: 2026-01) |
| É Fim de Semana | Logical | True para Sábado e Domingo |
| É Feriado | Logical | True para feriados nacionais de Portugal |
| Tipo de Dia | Text | "Dia Útil", "Fim de Semana" ou "Feriado" |

## Feriados Incluídos

### Feriados Fixos
- 1 de Janeiro: Ano Novo
- 25 de Abril: Dia da Liberdade (Revolução dos Cravos)
- 1 de Maio: Dia do Trabalhador
- 10 de Junho: Dia de Portugal
- 15 de Agosto: Assunção de Nossa Senhora
- 5 de Outubro: Implantação da República
- 1 de Novembro: Todos os Santos
- 1 de Dezembro: Restauração da Independência
- 8 de Dezembro: Imaculada Conceição
- 25 de Dezembro: Natal

### Feriados Móveis (calculados automaticamente)
- Carnaval (47 dias antes da Páscoa)
- Sexta-feira Santa (2 dias antes da Páscoa)
- Páscoa (domingo)
- Corpo de Cristo (60 dias após a Páscoa)

## Criar Relacionamentos

Após criar a DimCalendar, crie relacionamentos com as tabelas de fatos:

1. Vá para a **Visualização de Modelo**
2. Arraste o campo **TimeKey** de DimCalendar para o campo de data correspondente nas tabelas de fatos
3. Configure o relacionamento como:
   - **Cardinalidade**: 1 para muitos (de DimCalendar para tabela de fatos)
   - **Direção do filtro cruzado**: Única

## Criar Hierarquia Temporal

Para facilitar a navegação temporal:

1. Na visualização de **Dados** ou **Modelo**, clique com o botão direito em **Ano**
2. Selecione **Criar hierarquia**
3. Renomeie para "Hierarquia Temporal"
4. Arraste as colunas na seguinte ordem:
   - Ano
   - Trimestre
   - Mes (ou MesNome)
   - Data

## Personalização

### Alterar o Período
Para modificar o intervalo de datas, edite os parâmetros no início do código:
```m
StartDate = #date(2016, 1, 1),  // Data inicial
EndDate = #date(2026, 12, 31),  // Data final
```

### Adicionar Feriados Regionais
Para incluir feriados específicos de uma região, adicione-os à lista `feriadosFixos`:
```m
feriadosFixos = {
    // ... feriados existentes ...
    #date(ano, 6, 13),  // Santo António (Lisboa)
    #date(ano, 6, 24)   // São João (Porto)
},
```

## Dicas e Boas Práticas

1. **Marque como Tabela de Datas**: 
   - Clique com o botão direito na tabela DimCalendar
   - Selecione **Marcar como tabela de datas**
   - Escolha a coluna **Data** como coluna de data

2. **Defina a Ordenação Personalizada**:
   - Ordene **MesNome** por **Mes**
   - Ordene **DiaSemana** por **Data**

3. **Desative o Carregamento de Etapas Intermediárias**:
   - No Power Query, desmarque "Habilitar carregamento" para consultas auxiliares

4. **Performance**:
   - A tabela contém aproximadamente 4.018 linhas (11 anos)
   - O carregamento é rápido devido à geração dinâmica

## Resolução de Problemas

### Erro de Sintaxe
- Certifique-se de copiar todo o código, incluindo `let` no início e `in` no final
- Verifique se não há caracteres especiais corrompidos

### Datas não aparecem em português
- Verifique as configurações regionais do Power BI Desktop
- O código usa `"pt-PT"` para garantir nomes em português

### TimeKey não funciona em relacionamentos
- Certifique-se de que a coluna de data na tabela de fatos está no formato YYYYMMDD
- Se necessário, crie uma coluna calculada na tabela de fatos:
  ```DAX
  TimeKey = YEAR([Data]) * 10000 + MONTH([Data]) * 100 + DAY([Data])
  ```

## Referências

- Código fonte: `sns\csv\DimCalendar.m`
- Algoritmo de cálculo da Páscoa: Meeus/Jones/Butcher
- Feriados baseados na legislação portuguesa atual

---

**Versão**: 1.0  
**Última atualização**: Março 2026  
**Compatibilidade**: Power BI Desktop (todas as versões recentes)
