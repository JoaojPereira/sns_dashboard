"""
ARQUITETURA DE MODELO DE DADOS PARA DASHBOARD SNS
Análise de Ineficiências nas Urgências Hospitalares
"""

print("="*80)
print("SUGESTÃO DE MODELO DE DADOS - STAR SCHEMA")
print("Análise de Ineficiências nas Urgências Hospitalares do SNS")
print("="*80)

print("\n" + "="*80)
print("TABELAS DIMENSÃO (4)")
print("="*80)

print("\n1. DimCalendar (Dimensão Temporal)")
print("   Fonte: Criar com script M (DimCalendar.m já existe)")
print("   Granularidade: Dia")
print("   Campos principais:")
print("   • Data (PK)")
print("   • Ano")
print("   • Mês")
print("   • MêsNome")
print("   • Trimestre")
print("   • Semestre")
print("   • AnoMês (YYYY-MM)")
print("   • DiaSemana")
print("   • ÉFimDeSemana")
print("   • ÉFeriado")
print("   Relacionamento: 1:N com todas as tabelas factuais")

print("\n2. DimRegião (Dimensão Geográfica)")
print("   Fonte: Extrair valores únicos dos CSV")
print("   Granularidade: Região")
print("   Campos principais:")
print("   • RegiãoID (PK) - surrogate key 1-5")
print("   • RegiãoNome")
print("   • RegiãoSigla (Norte, Centro, LVT, Alentejo, Algarve)")
print("   • Ordem (para ordenação visual)")
print("   Linhas: 5 registos")
print("   Relacionamento: 1:N com todas as tabelas factuais")

print("\n3. DimInstituição (Dimensão Hospitalar)")
print("   Fonte: Extrair valores únicos dos CSV")
print("   Granularidade: Instituição")
print("   Campos principais:")
print("   • InstituiçãoID (PK) - surrogate key")
print("   • InstituiçãoNome")
print("   • Tipo (Centro Hospitalar, ULS, Hospital, etc.)")
print("   • RegiãoID (FK para análises)")
print("   Linhas: ~75 registos (todas as instituições únicas)")
print("   Relacionamento: 1:N com FactAtendimentos, FactCustos, FactTrabalhadores")

print("\n4. DimIndicador (Dimensão de Métricas)")
print("   Fonte: Criar manualmente ou extrair de Monitorização")
print("   Granularidade: Indicador de monitorização")
print("   Campos principais:")
print("   • IndicadorID (PK)")
print("   • IndicadorNome")
print("   • IndicadorGrupo (Tempo Espera, Atendimentos, Episódios)")
print("   • Unidade (minutos, %, número)")
print("   Linhas: 4 registos")
print("   Relacionamento: 1:N com FactMonitorização")

print("\n" + "="*80)
print("TABELAS FACTUAIS (4)")
print("="*80)

print("\n1. FactAtendimentos (Tabela Factual)")
print("   Fonte: atendimentos-em-urgencia-triagem-manchester.csv")
print("   Granularidade: Instituição + Mês")
print("   Campos:")
print("   • Data (FK → DimCalendar)")
print("   • RegiãoID (FK → DimRegião)")
print("   • InstituiçãoID (FK → DimInstituição)")
print("   • Atendimentos_Vermelha (medida)")
print("   • Atendimentos_Laranja (medida)")
print("   • Atendimentos_Amarela (medida)")
print("   • Atendimentos_Verde (medida)")
print("   • Atendimentos_Azul (medida)")
print("   • Atendimentos_Branca (medida)")
print("   • Atendimentos_SemTriagem (medida)")
print("   Linhas: 6.020 registos")
print("   KPIs: Taxa urgentes vs não urgentes, % triagem")

print("\n2. FactCustos (Tabela Factual)")
print("   Fonte: custo-de-tratamento-mensal-por-doente.csv")
print("   Granularidade: Instituição + Mês")
print("   Campos:")
print("   • Data (FK → DimCalendar)")
print("   • RegiãoID (FK → DimRegião)")
print("   • InstituiçãoID (FK → DimInstituição)")
print("   • Despesa (medida)")
print("   • NumDoentes (medida)")
print("   • CustoMédio (medida calculada)")
print("   Linhas: 249 registos")
print("   KPIs: Custo médio por doente, variação temporal")

print("\n3. FactTrabalhadores (Tabela Factual)")
print("   Fonte: trabalhadores-por-grupo-profissional.csv")
print("   Granularidade: Instituição + Mês")
print("   Campos:")
print("   • Data (FK → DimCalendar)")
print("   • RegiãoID (FK → DimRegião)")
print("   • InstituiçãoID (FK → DimInstituição)")
print("   • Médicos (medida)")
print("   • MédicosInternos (medida)")
print("   • Enfermeiros (medida)")
print("   • TécnicosSaúde (medida)")
print("   • ... (outras categorias)")
print("   • TotalGeral (medida)")
print("   Linhas: 4.761 registos")
print("   KPIs: Rácio profissionais/atendimentos, evolução staffing")

print("\n4. FactMonitorização (Tabela Factual)")
print("   Fonte: monitorizacao-sazonal-csh.csv")
print("   Granularidade: Região + Dia + Indicador")
print("   Campos:")
print("   • Data (FK → DimCalendar)")
print("   • RegiãoID (FK → DimRegião)")
print("   • IndicadorID (FK → DimIndicador)")
print("   • Valor (medida)")
print("   Linhas: 64.816 registos")
print("   KPIs: Tempo espera médio, taxa internamento, episódios")

print("\n" + "="*80)
print("MEDIDAS DAX SUGERIDAS (Análise de Ineficiências)")
print("="*80)

medidas = {
    "EFICIÊNCIA OPERACIONAL": [
        "% Atendimentos Não Urgentes = (Verde + Azul + Branca) / Total",
        "Taxa Sem Triagem = Sem Triagem / Total Atendimentos",
        "Tempo Espera vs Meta = [Tempo Espera] - 60 minutos",
        "Desvio Custo Médio = [Custo Médio] - [Custo Médio Nacional]"
    ],
    "RECURSOS HUMANOS": [
        "Rácio Enfermeiro/Médico = Enfermeiros / Médicos",
        "Atendimentos por Médico = Total Atendimentos / Médicos",
        "Atendimentos por Enfermeiro = Total Atendimentos / Enfermeiros",
        "Variação Staffing YoY = ([Trabalhadores Ano] - [Trabalhadores Ano-1]) / [Ano-1]"
    ],
    "QUALIDADE ASSISTENCIAL": [
        "Taxa Internamento = Atendimentos c/ Internamento / Total",
        "% Casos Urgentes (Vermelho+Laranja) = (Vermelha + Laranja) / Total",
        "Tempo Espera Casos Urgentes = CALCULATE([Tempo Espera], Prioridade <= 2)",
        "Episódios Urgência per Capita = Total Episódios / População"
    ],
    "ANÁLISE FINANCEIRA": [
        "Custo Total por Região = SUM(Despesa)",
        "Custo Médio Ponderado = SUMX(Valores, [Despesa] * [Doentes]) / SUM([Doentes])",
        "Variação Custo YoY = ([Custo Ano] - [Custo Ano-1]) / [Custo Ano-1]",
        "ROI Staffing = [Atendimentos] / ([Custo Total Trabalhadores])"
    ],
    "BENCHMARKING": [
        "Ranking Eficiência = RANKX(ALL(Instituição), [Score Eficiência])",
        "vs Média Nacional = [Métrica Instituição] - [Métrica Nacional]",
        "Percentil Tempo Espera = PERCENTILEX.INC(ALL(Valores), [Tempo Espera], 0.9)",
        "Top 10% Performers = TOPN(10%, Instituições, [Score Global])"
    ]
}

for categoria, lista_medidas in medidas.items():
    print(f"\n{categoria}:")
    for medida in lista_medidas:
        print(f"   • {medida}")

print("\n" + "="*80)
print("PÁGINAS SUGERIDAS PARA O DASHBOARD")
print("="*80)

paginas = {
    "1. VISÃO GERAL EXECUTIVA": [
        "KPIs principais (cards)",
        "Mapa de Portugal com indicadores por região",
        "Tendência temporal de ineficiências",
        "Top 10 instituições com melhor/pior performance"
    ],
    "2. ANÁLISE DE ATENDIMENTOS": [
        "Distribuição por prioridade Manchester (gráfico pizza/barras)",
        "Taxa de atendimentos não urgentes por instituição",
        "Evolução temporal de triagens",
        "Análise sazonal (padrões mensais/semanais)"
    ],
    "3. ANÁLISE DE CUSTOS": [
        "Custo médio por doente por região",
        "Variação de custos YoY",
        "Scatter plot: Custo vs Atendimentos",
        "Ranking de instituições por eficiência de custo"
    ],
    "4. RECURSOS HUMANOS": [
        "Rácios profissionais por região",
        "Atendimentos per capita profissional",
        "Gap de recursos vs meta",
        "Evolução de staffing temporal"
    ],
    "5. TEMPO DE ESPERA": [
        "Tempo espera médio por região",
        "% instituições acima de meta (60min)",
        "Tempo espera por prioridade",
        "Heatmap: Tempo espera por dia/hora"
    ],
    "6. BENCHMARKING": [
        "Matriz de performance (quadrantes)",
        "Scorecard comparativo regional",
        "Análise de outliers",
        "Melhores práticas (instituições eficientes)"
    ]
}

for pagina, conteudo in paginas.items():
    print(f"\n{pagina}")
    for item in conteudo:
        print(f"   • {item}")

print("\n" + "="*80)
print("RESUMO DA ARQUITETURA")
print("="*80)
print("\nModelo: STAR SCHEMA")
print("Dimensões: 4 (Calendar, Região, Instituição, Indicador)")
print("Factuais: 4 (Atendimentos, Custos, Trabalhadores, Monitorização)")
print("Relacionamentos: 1:N (One-to-Many)")
print("Tipo: Snowflake simplificado")
print("\nVantagens:")
print("   ✓ Performance otimizada para DAX")
print("   ✓ Facilita drill-down e slicing")
print("   ✓ Estrutura escalável")
print("   ✓ Cálculos de Time Intelligence")
print("   ✓ Análises cross-tabela")
print("\n🎯 FOCO: Identificar ineficiências operacionais, de custos e de recursos!")
print("="*80)
