# Roteiro de Apresentação Oral
## Análise de Ineficiências nas Urgências Hospitalares do SNS Portugal

**Duração:** 10 minutos  
**Apresentador:** João Domingues Pereira  
**Data:** 30/11/2025

---

## Estrutura da Apresentação

1. **Introdução** (1 minuto)
2. **Contexto e Motivação** (1,5 minutos)
3. **Metodologia e Desafios Técnicos** (2 minutos)
4. **Resultados e Métricas-Chave** (3 minutos)
5. **Justificação das Escolhas Visuais** (1,5 minutos)
6. **Conclusões e Impacto** (1 minuto)

---

## 1. INTRODUÇÃO (1 minuto)

### Abertura

"Boa tarde. Hoje vou apresentar um projeto de Business Intelligence que analisa **quase 10 anos de dados** das urgências hospitalares do SNS (2016-2025), identificando ineficiências que custam ao sistema **15,2 mil milhões de euros**.

Este não é apenas um exercício académico. É uma ferramenta de decisão estratégica baseada em **301,2 milhões de atendimentos reais** de 75 instituições hospitalares, que permite aos gestores identificar onde intervir e quanto podem poupar."

### Objetivo Central

"O objetivo é responder a três perguntas fundamentais:
1. Onde estamos a desperdiçar recursos?
2. Porquê?
3. O que fazer para corrigir?"

---

## 2. CONTEXTO E MOTIVAÇÃO (1,5 minutos)

### O Problema

"As urgências hospitalares portuguesas enfrentam um problema estrutural que se agravou: **41,93% dos atendimentos são casos não urgentes**. Isto significa que **mais de 4 em cada 10 pessoas** que vão à urgência poderiam ser atendidas num centro de saúde.

Para contexto, a meta nacional é menos de 30%. Estamos **11,93 pontos percentuais acima** — uma situação crítica que se deteriorou nos últimos anos."

### Impacto Real

"Cada caso não urgente numa urgência custa 150 euros. O mesmo caso num centro de saúde custa 30 euros. São 120 euros de desperdício por pessoa. Multiplique isso por **126,3 milhões de casos não urgentes** em 9,75 anos. São **15,2 mil milhões de euros** desperdiçados — o equivalente a **1,55 mil milhões por ano**."

**[PAUSA BREVE PARA IMPACTO]**

"15,2 mil milhões de euros. É o equivalente a mais de 3 anos do orçamento completo para os cuidados de saúde primários."

### Por Que Este Projeto?

"Havia dados públicos no Portal da Transparência do SNS, mas dispersos, não normalizados, sem contexto. Ninguém conseguia ver o padrão. 

Transformei 70 mil linhas de dados brutos em informação acionável. Cada métrica que vão ver foi desenhada para responder a uma decisão específica de gestão."

---

## 3. METODOLOGIA E DESAFIOS TÉCNICOS (2 minutos)

### Origem dos Dados

"Trabalhei com três datasets principais:
- Atendimentos por triagem de Manchester (4.131 registos mensais)
- Recursos humanos por instituição (2.558 registos com dados)
- Monitorização diária de tempos de espera (32.641 registos)

**Total: cerca de 37 mil linhas** cobrindo 75 hospitais, 5 regiões, 10 anos."

### Desafio 1: Qualidade dos Dados

"O primeiro desafio foi a qualidade. Os nomes das instituições vinham corrompidos com caracteres especiais. Criei ** scripts Python** só para normalizar e garantir consistência.

Dados de custos? Apenas 5,3% de cobertura. Solução: estimativa fundamentada de 150 euros por episódio, baseada em valores médios nacionais publicados."

### Desafio 2: Contextualização

"2020 e 2021 apresentavam quedas anómalas. Não era melhoria - era COVID-19. Os confinamentos reduziram artificialmente os atendimentos não urgentes. 

Documentei isto explicitamente no modelo. Sem contexto, os dados mentem."

### Arquitetura: Star Schema

"Escolhi uma arquitetura star schema: duas tabelas factuais (atendimentos mensais e monitorização diária) ligadas a quatro dimensões (calendário, região, instituição, indicadores).

Porquê? Porque permite queries rápidas mesmo com 10 anos de dados. O tempo médio de resposta é inferior a 2 segundos."

### DAX: 50+ Medidas Estruturadas

"Implementei mais de 50 medidas DAX, organizadas em 10 categorias lógicas. Não são cálculos aleatórios - cada medida responde a uma questão de negócio específica.

A métrica central é o **Score de Ineficiência Global**, uma fórmula ponderada que combina:

Porquê esta ponderação? Porque urgências falsas e custos são os indicadores que os gestores podem controlar diretamente. RH e tempos são consequências."

- 40% não urgentes
- 30% tempo de espera
- 15% produtividade
- 15% custo desperdiçado

Porquê esta ponderação? Porque não urgentes e custos são os indicadores que os gestores podem controlar diretamente. Produtividade e tempos são consequências."

---

## 4. RESULTADOS E MÉTRICAS-CHAVE (3 minutos)

### Métrica 1: Taxa de Urgências Falsas - 41,93%

"Este é o indicador central. 41,93% dos atendimentos são verde, azul ou branco na triagem de Manchester - casos que não são urgentes.

Cada 10% de aumento nesta taxa aumenta o tempo de espera médio em 15 minutos. É um ciclo vicioso: mais não urgentes → mais espera → mais frustração → pior qualidade de serviço."

### Métrica 2: Custo Desperdiçado - €15,2 mil milhões

"O diferencial entre atender na urgência (150€) e no centro de saúde (30€) é de 120 euros por caso.

126,3 milhões de casos não urgentes × 120€ = **15,2 mil milhões** desperdiçados em dez anos.

Isto não é despesa inevitável. É ineficiência pura que pode ser corrigida com reencaminhamento e sensibilização."

### Métrica 3: Défice de Enfermeiros - 10.400

"A OMS recomenda um rácio mínimo de 2 enfermeiros por médico. A realidade portuguesa é 1,6.

Identifiquei um défice de **10.400 enfermeiros** face ao rácio ideal. Isto não é opinião - é matemática simples aplicada aos dados de RH de 75 hospitais."

### Métrica 4: Tempo Médio de Espera - 57 minutos

"O protocolo de Manchester define 60 minutos como tempo máximo aceitável para casos amarelos (urgentes). A média nacional é 57 minutos - dentro da meta global, mas com picos graves.

Em 35,5% dos dias analisados, o tempo de espera ultrapassou uma hora. Isto não é variabilidade estatística. É incumprimento sistemático."

### Variabilidade Regional: Até 40%

"Há hospitais com 25% de não urgentes e outros com 55%. Há regiões com 50 minutos de espera e outras com 120 minutos.

Esta variabilidade prova que o problema não é inevitável. Se alguns conseguem, todos podem. É questão de identificar boas práticas e replicá-las."

### Padrão Sazonal: Inverno Crítico

"Os picos de procura ocorrem consistentemente em dezembro-janeiro. O volume aumenta até 30% face ao verão.

Isto é previsível. Mas a maioria dos hospitais não ajusta recursos sazonalmente. Continuam com a mesma equipa no inverno e no verão."

### Impacto da COVID-19

"2020-2021 apresentam quedas artificiais. Não foi melhoria - foram confinamentos obrigatórios. 

Isto ensinou-nos algo importante: quando há alternativas acessíveis (telefonemas, linha SNS24), as pessoas **não** vão à urgência por trivialidades. O problema não é só cultural - é também de acessibilidade aos cuidados primários."

---

## 5. JUSTIFICAÇÃO DAS ESCOLHAS VISUAIS (1,5 minutos)

### Página Executiva: Cards, Tabela e Colunas Agrupadas

"Para a gestão superior, precisamos de **impacto visual imediato**. Por isso escolhi:

**KPI Cards** - Porque decisores não têm tempo para procurar. Os 4 números mais críticos (301M atendimentos, €15,2B desperdiçados, 57 min espera, 41,93% não urgentes) estão sempre visíveis, independentemente dos filtros aplicados.

**Tabela de Orçamentos** - Para contextualizar. Mostra que o orçamento da saúde cresceu 62% desde 2016, mas os atendimentos não urgentes continuam a subir. Isto prova que não é falta de investimento - é má alocação de recursos.

**Gráfico de Colunas Agrupadas** em vez de linhas - Porquê? Porque precisamos comparar 3 séries (Total, Urgentes, Não Urgentes) ano a ano. As colunas permitem essa comparação direta. Linhas sobrepõem-se e dificultam a leitura quando há muitas séries."

### Página Operacional: Tabela com Ícones e Bookmark para Alternância

"Na página operacional, implementei um **Bookmark interativo** que alterna entre duas tabelas detalhadas:

**Vista 1 - Foco em Recursos Humanos:** Mostra o rácio enfermeiro/médico por instituição com ícones de status (✅ Ideal, ⚠️ Excesso, ❌ Défice). Os gestores veem imediatamente quais hospitais têm défice de enfermeiros.

**Vista 2 - Foco em Urgências Falsas:** Exibe o volume de atendimentos não urgentes e o status crítico (❌ Crítico >40%, ⚠️ Atenção 30-40%).

Porquê bookmarks? Porque não conseguimos mostrar 76 instituições com 10 colunas numa só tabela sem perder legibilidade. Os bookmarks permitem ao utilizador focar-se num problema específico sem trocar de página. É como ter duas páginas operacionais num único ecrã.

Os **semáforos e ícones visuais** substituem números. O cérebro humano processa símbolos visuais 60.000 vezes mais rápido que texto. Um gestor identifica problemas críticos em 2 segundos, sem ler uma única linha."

### Página Financeira: Colunas Agrupadas e Barras Empilhadas

"Para auditores e gestores financeiros, a pergunta é sempre: **Quanto estamos a perder?**

**Gráfico de Colunas Agrupadas (Temporal):** Mostra a evolução anual de Despesa Total (azul) vs Desperdício Potencial (vermelho). Escolhi colunas em vez de linhas porque o objetivo é **comparar magnitudes** ano a ano. A altura relativa das colunas vermelhas em relação às azuis mostra visualmente a proporção de desperdício.

Observem: em 2025, a coluna vermelha representa €1,7B de desperdício. Isto não é abstrato - são 14.166 enfermeiros que poderíamos contratar.

**Barras Empilhadas Horizontais (Por Instituição):** Rankeia as instituições por volume de desperdício. O azul é despesa efetiva, o vermelho é desperdício. As barras estão ordenadas por desperdício total. Isto identifica onde auditar primeiro: Hospital Professor Doutor Fernando Fonseca EPE lidera com €421M desperdiçados.

Porquê barras horizontais? Porque temos 76 nomes de instituições. Nomes verticais são ilegíveis. Horizontais permitem leitura natural."

### Página Recursos Humanos: Linhas Temporais e Barras de Produtividade

"Esta página responde a duas perguntas críticas dos sindicatos e ACSS:

**Gráfico de Linhas Temporal:** Mostra a evolução de Médicos, Médicos Internos e Enfermeiros desde 2016. Escolhi linhas porque o objetivo é **ver tendências e taxas de crescimento**. Observem o salto em 2023 - contratações pós-COVID. As linhas permitem ver se as contratações de enfermeiros estão a acompanhar as de médicos (não estão - daí o rácio 1,80 vs meta 2,0).

**Gráfico de Barras Horizontal (Produtividade):** Cada barra representa atendimentos por médico numa instituição. A linha vertical vermelha marca a média nacional. Instituições à esquerda da linha estão abaixo da média - podem ter problemas operacionais. À direita, podem estar a sobrecarregar equipas.

Porquê este visual? Porque precisamos identificar **outliers** - tanto hospitais sub-produtivos (que precisam de otimização de processos) como super-produtivos (risco de burnout). Um simples número médio esconderia estes extremos."

### Página Sazonalidade: Bookmarks para Padrões Temporais e Picos

"O planeamento de recursos exige compreender **quando** ocorrem os picos. Implementei **2 bookmarks** nesta página:

**Bookmark 1 - Vista Temporal:** 
- **Gráfico de Linhas:** Tempo médio de espera mensal desde 2016. Mostra o padrão sazonal - picos no inverno (Dez/Jan) visíveis ano após ano.
- **Gráfico de Linhas por Região:** Compara as 5 regiões de saúde. Permite identificar quais regiões sofrem mais pressão sazonal.

**Bookmark 2 - Vista de Picos de Atendimentos:**
- **Pie Chart:** Distribuição por tipo de dia (Dias Úteis 44%, Feriados 23%, Fins de Semana 33%). Mostra que precisamos de reforço aos fins de semana.
- **Gráfico de Linhas:** Atendimentos por cor de triagem de Manchester ao longo do tempo. Identifica se os picos são de casos graves (vermelho/laranja) ou não urgentes (verde/azul).
- **Tabela de Picos Sazonais:** Consolida os volumes máximos por região e estação. Inverno vs Verão - variações de +25% no Alentejo.

Porquê bookmarks? Porque não podemos ter 5 gráficos numa página sem comprometer a legibilidade. Os bookmarks mantêm o foco: **1 pergunta = 1 vista**. Gestores de planeamento alternam conforme a análise - padrões temporais ou distribuição de tipos de atendimento."

### Página Qualidade de Dados: Validação e Transparência

"Esta página existe por uma razão crítica: **Decisões baseadas em dados ruins são piores que decisões baseadas em intuição.**

Com apenas 61,92% de cobertura de dados de RH, 20 instituições sem dados válidos, **não podemos calcular produtividade ou rácio enfermeiro/médico de forma fiável para todas**.

**4 Cards de KPI:** Mostram o estado da qualidade de forma transparente. Não escondemos problemas - exponho-los para serem corrigidos.

**Clustered Bar Chart:** Identifica visualmente as 20 instituições sem dados de RH. Isto não é para culpabilizar - é para **priorizar apoio técnico**. Estas instituições podem não ter sistemas de reporte adequados.

**Tabela de Métricas por Instituição:** Ordenada por taxa de cobertura (crescente). Com formatação condicional (🟢 >80%, 🟡 60-80%, 🟠 40-60%, 🔴 <40%). Permite monitorizar evolução trimestral. Se uma instituição passar de vermelho para amarelo, sabemos que as ações corretivas estão a funcionar.

Porquê esta página? **Transparência gera confiança.** Ao mostrar as limitações dos dados, aumentamos a credibilidade de todas as outras análises. E criamos um mecanismo de melhoria contínua - gestores técnicos sabem onde investir esforço de recolha de dados."

### Página Rankings: Gauge Chart e Heatmap para Benchmarking

"Esta é a página mais **sensível politicamente**, mas também a mais útil para consultores e investigadores.

**Gauge Chart (Velocímetro 0-100):** O Score Ineficiência Global combina 4 dimensões (40% Não Urgentes, 30% Tempo Espera, 15% Produtividade, 15% Custos). Um único número para comparar instituições. 

Porquê velocímetro? Porque é **universalmente compreendido**. Verde (<30) = eficiente, Amarelo (30-50) = atenção, Laranja (50-70) = intervenção necessária, Vermelho (>70) = crítico. Um político ou jornalista compreende instantaneamente.

**Tabela Heatmap:** Lista todas as 76 instituições com formatação condicional de fundo. Quanto mais vermelho, pior a performance. Isto cria um **mapa de calor visual** - padrões emergem imediatamente. Vemos clusters de instituições problemáticas em certas regiões.

Porquê heatmap em vez de gráfico de barras? Porque precisamos mostrar **múltiplas métricas simultaneamente** (Score, % Não Urgentes, Produtividade). Uma tabela comporta 5-6 colunas; um gráfico de barras apenas 1-2 séries sem ficar confuso.

O objetivo não é envergonhar instituições - é criar **pressão por boas práticas**. Instituições no topo verde tornam-se modelos a estudar. As no fundo vermelho recebem apoio direcionado."

---

## 6. CONCLUSÕES E IMPACTO (1 minuto)

### Três Conclusões Principais

"Primeiro: **O problema é sistémico, mas corrigível.** 41,93% de não urgentes não é inevitável. Alguns hospitais têm 25%. É possível.

Segundo: **O desperdício é quantificável e enorme.** 15,2 mil milhões não é retórica. São euros reais que poderiam tratar mais doentes ou contratar mais enfermeiros.

Terceiro: **Os dados existem, mas ninguém os estava a usar.** Este projeto prova que transformar dados em decisão é viável com as ferramentas certas."

### Recomendações Acionáveis

"Três ações imediatas:

1. **Auditoria urgente** aos 10 hospitais com score acima de 70.
2. **Contratação prioritária** de enfermeiros onde o rácio é inferior a 1,5.
3. **Campanhas de sensibilização** para reduzir não urgentes de 42% para 30% em três anos - isto poupa 4 mil milhões de euros."

### Impacto Esperado

"Se este dashboard for usado ativamente pelos gestores hospitalares:
- Redução de 10 pontos percentuais em não urgentes = **€4 mil milhões** poupados
- Rácio enfermeiro/médico ≥2,0 em todas as instituições = **melhoria de 25%** nos tempos de espera
- Ajuste sazonal de recursos = **redução de 30%** nos picos de espera no inverno"

### Encerramento

"Este relatório não é o fim. É o início de uma gestão hospitalar baseada em evidência.

Os dados estão aqui. As métricas estão validadas. As ferramentas estão prontas.

Agora, a decisão de agir é vossa.

Obrigado. Estou disponível para perguntas."

---

## NOTAS PARA O APRESENTADOR

### Ritmo e Tom
- **Minutos 0-2:** Tom enérgico, criar impacto emocional com os números grandes
- **Minutos 2-5:** Tom técnico mas acessível, demonstrar rigor metodológico
- **Minutos 5-8:** Tom analítico, explicar **porquê** cada escolha visual
- **Minutos 8-10:** Tom assertivo e inspirador, call to action claro

### Gestão do Tempo
- Se estiver a passar do tempo nos minutos 0-4, corte detalhes técnicos sobre Python/DAX
- Se estiver a passar do tempo nos minutos 5-7, corte justificações de visuais secundários
- **NUNCA** corte as métricas-chave (37,76%, €16,5B, 20.800 enfermeiros, 87 min)

### Pausas Estratégicas
- Após "16,5 mil milhões de euros" → PAUSA 2 segundos
- Após "20.800 enfermeiros em falta" → PAUSA 2 segundos
- Após "A decisão de agir é vossa" → PAUSA 3 segundos

### Linguagem Corporal
- Quando falar de desperdício (€16,5B): expressão séria, voz firme
- Quando falar de soluções: expressão confiante, voz assertiva
- Quando falar de variabilidade (25% vs 55%): usar gestos de mãos para mostrar distância

### Preparação para Perguntas
**Perguntas Prováveis:**

1. **"Como validou a estimativa de 150€?"**
   - "Cruzamento com valores médios publicados pela DGS e estudos internacionais. É conservadora - alguns estudos apontam 180-200€."

2. **"Por que Star Schema e não outro modelo?"**
   - "Performance. Com 70 mil linhas e 10 anos, queries em <2 segundos. Outros modelos seriam mais lentos ou mais complexos de manter."

3. **"Como garantir que os gestores usarão o dashboard?"**
   - "Três estratégias: formação obrigatória, relatórios mensais automáticos, e ligar KPIs a incentivos de gestão. Se não houver consequências, não há mudança."

4. **"E os hospitais com dados em falta?"**
   - "Documentado explicitamente. Cobertura de RH é 61,9%. Instituições sem dados têm sinalização visual clara no dashboard. Não escondemos limitações."

5. **"Qual o ROI deste projeto?"**
   - "Se reduzir não urgentes em apenas 5 pontos percentuais (de 41,93% para 36,93%), poupa €2 mil milhões em 5 anos. O projeto custou umas semanas de trabalho. ROI infinito."

---

## CHECKLIST PRÉ-APRESENTAÇÃO

- [ ] Laptop carregado + carregador de backup
- [ ] Ficheiro .pbix testado e a abrir corretamente
- [ ] Power BI Desktop atualizado
- [ ] Slides de backup com screenshots (caso Power BI não abra)
- [ ] Notas impressas deste roteiro
- [ ] Garrafa de água
- [ ] Telemóvel em modo avião
- [ ] Chegar 15 minutos antes para testar projetor
- [ ] Praticar apresentação 2x (cronometrar!)

---

**Boa sorte!**