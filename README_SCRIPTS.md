# 📁 Scripts Histórico - Transformação de Dados

## ⚠️ ATENÇÃO: NÃO EXECUTAR ESTES SCRIPTS!

Os ficheiros CSV finais já foram processados e estão prontos para importação no Power BI.

Estes scripts estão arquivados apenas para **referência e documentação** do processo de transformação aplicado aos dados originais do SNS.

---

## 📝 Scripts de Transformação (Por Ordem de Execução)

### 1. Limpeza Inicial
- `limpar_csv_atendimentos.py` - Remove encoding issues e colunas geográficas
- `limpar_csv_custos.py` - Padroniza nomes de colunas
- `limpar_csv_trabalhadores.py` - Remove categorias administrativas
- `limpar_csv_monitorizacao.py` - Encurta nomes de indicadores

### 2. Padronização de Nomes
- `padronizar_nomes_instituicoes.py` - Normaliza nomes de hospitais
- `padronizar_todos_nomes.py` - Aplica padronização cross-file
- `alterar_ppp_para_epe.py` - Substitui PPP por EPE

### 3. Remoção de Dados Irrelevantes
- `remover_instituicoes_nao_hospitalares.py` - Remove serviços centrais
- `remover_admin_regional.py` - Remove ARS
- `remover_instituicoes_especializadas.py` - Remove IPOs e psiquiátricos
- `remover_portugal_continental.py` - Remove agregados nacionais

### 4. Normalização Temporal
- `normalizar_datas_2016.py` - Filtra >= 2016-01
- `analise_periodos.py` - Valida períodos comuns

### 5. Consolidação
- `criar_factual_consolidada.py` - LEFT JOIN de 3 ficheiros
- `criar_dimensoes.py` - Cria DimRegiao, DimInstituicao, DimIndicador

### 6. Otimização
- `adicionar_ids_factual.py` - Adiciona RegiaoID e InstituicaoID
- `adicionar_ids_monitorizacao.py` - Adiciona IDs na monitorização
- `adicionar_timekey.py` - Cria chave para DimCalendar
- `corrigir_valores_vazios.py` - Substitui NaN por 0
- `remover_decimais.py` - Remove .0 de inteiros
- `encurtar_nomes_colunas.py` - Simplifica nomes de colunas

### 7. Validação
- `diagnostico_join.py` - Valida JOIN entre tabelas
- `diagnostico_erros_powerbi.py` - Testa compatibilidade Power BI
- `comparar_instituicoes.py` - Verifica consistência cross-file
- `verificacao_powerbi.py` - Validação final

### 8. Arquitetura
- `modelo_2_factuais.py` - Explica modelo simplificado
- `arquitetura_modelo_dados.py` - Documenta Star Schema

---

## 📊 Resultados Finais (na pasta raiz)

- ✅ `FactAtendimentosUrgencia.csv` (4.133 linhas, 18 colunas)
- ✅ `FactMonitorizacaosazonal.csv` (64.816 linhas, 5 colunas)
- ✅ `DimRegiao.csv` (5 regiões de saúde)
- ✅ `DimInstituicao.csv` (76 instituições hospitalares + header)
- ✅ `DimIndicador.csv` (4 indicadores de monitorização)
- ✅ `DimCalendar.m` (script Power Query para dimensão temporal)

---

## 🔄 Para Reprocessar Dados (se necessário)

Se precisares reprocessar os dados originais do SNS:

1. Colocar CSVs originais na pasta raiz
2. Executar scripts na ordem acima
3. Validar resultados com scripts de diagnóstico

**Tempo estimado:** 10-15 minutos (todos os scripts)

---

## 📈 Melhorias Implementadas (Dezembro 2024)

### Correções no Score Ineficiência Global
- ✅ Atualizado de 90 para **100 pontos** (40% Não Urgentes, 30% Tempo Espera, 15% Produtividade, 15% Custos)
- ✅ Adicionado componente de **Custo Desperdiçado** (peso 15%)
- ✅ Corrigida distribuição de pesos para totalizar 100%

### Novas Medidas DAX de Qualidade de Dados
- ✅ `Taxa Cobertura RH` - Percentagem de registros com dados válidos (61,92%)
- ✅ `Registros com RH Válido` - Contagem de registros com Médicos > 0 E Enfermeiros > 0 (2.558)
- ✅ `Instituições Sem RH` - Instituições sem dados de RH (20)
- ✅ `Validação Total Atendimentos` - Diferença entre soma triagens e total (formato numérico)
- ✅ 8 medidas adicionais de benchmarking e validação

### Atualizações de Documentação
- ✅ Correção: **76 instituições** (não 120)
- ✅ Dashboard atualizado para **7 páginas** (adicionada página "Qualidade de Dados")
- ✅ Tipo de gráfico alterado: Line Chart → **Clustered Column Chart** (Executiva/Financeira)
- ✅ `GlossarioMetricas_M.txt` atualizado com 4 novas métricas
- ✅ Todos os relatórios técnicos atualizados (README, RELATÓRIO TÉCNICO, Relatorio_SNS, roteiro-apresentacao)

### Dados Validados
- ✅ Total de atendimentos: **301.177.048** (2016-2025)
- ✅ Custo desperdiçado: **€15.154.680.480**
- ✅ Tempo espera médio: **56,83 minutos**
- ✅ Taxa não urgentes: **41,93%** (crítico)
- ✅ Rácio Enf/Médico: **1,80** (vs meta 2,0)
- ✅ Défice enfermeiros: **10.400 profissionais**

---

## 📂 Estrutura de Backups

A pasta `Backup/` contém versões anteriores dos ficheiros principais:
- Backups pré-normalização (20/12/2024 12:09)
- Backups após ajustes de TimeKey (20/12/2024 12:34-37)
- Backup pré-filtro 2016 (20/12/2024 13:11)

**Política:** Manter backups antes de transformações destrutivas (filtros temporais, remoção de registros).

---

**Nota:** Estes scripts foram criados especificamente para os datasets do Portal da Transparência do SNS (2016-2025). Ajustes podem ser necessários para outros períodos ou fontes de dados.

**Última atualização:** Dezembro 2025 - Implementadas melhorias de qualidade de dados e correções de Score Global.
