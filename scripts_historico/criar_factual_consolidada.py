import pandas as pd

print("="*80)
print("CRIANDO FACTUAL CONSOLIDADA: FactAtendimentosUrgência")
print("="*80)

# Ler os 3 ficheiros
print("\n1. Lendo ficheiros...")
df_atend = pd.read_csv('atendimentos-em-urgencia-triagem-manchester.csv', 
                       sep=';', encoding='utf-8-sig')
df_trab = pd.read_csv('trabalhadores-por-grupo-profissional.csv', 
                      sep=';', encoding='utf-8-sig')
df_custos = pd.read_csv('custo-de-tratamento-mensal-por-doente.csv', 
                        sep=';', encoding='utf-8-sig')

print(f"   Atendimentos: {len(df_atend)} linhas")
print(f"   Trabalhadores: {len(df_trab)} linhas")
print(f"   Custos: {len(df_custos)} linhas")

# Preparar colunas para join
print("\n2. Preparando dados para consolidação...")

# Renomear colunas para padronizar
df_custos = df_custos.rename(columns={'Instituição Hospitalar': 'Instituição'})

# Criar campo TotalAtendimentos
colunas_atend = [col for col in df_atend.columns if 'Nº Atendimentos' in col]
df_atend['TotalAtendimentos'] = df_atend[colunas_atend].sum(axis=1)

print(f"   ✓ Coluna TotalAtendimentos criada")

# Selecionar apenas colunas relevantes de Trabalhadores
cols_trab = ['Período', 'Região', 'Instituição', 
             'Médicos S/ Internos', 'Médicos Internos', 'Enfermeiros', 'Total Geral']
df_trab_resumido = df_trab[cols_trab].copy()
df_trab_resumido = df_trab_resumido.rename(columns={
    'Médicos S/ Internos': 'Médicos',
    'Médicos Internos': 'MedicosInternos',
    'Total Geral': 'TotalProfissionais'
})

print(f"   ✓ Trabalhadores: {len(cols_trab)} colunas selecionadas")

# Consolidar
print("\n3. Consolidando tabelas (LEFT JOIN)...")
print("   Base: Atendimentos")

# JOIN 1: Atendimentos + Trabalhadores
fact = df_atend.merge(
    df_trab_resumido,
    on=['Período', 'Região', 'Instituição'],
    how='left',
    suffixes=('', '_trab')
)
print(f"   ✓ JOIN com Trabalhadores: {len(fact)} linhas")

# JOIN 2: Resultado + Custos
fact = fact.merge(
    df_custos,
    on=['Período', 'Região', 'Instituição'],
    how='left',
    suffixes=('', '_custo')
)
print(f"   ✓ JOIN com Custos: {len(fact)} linhas")

# Renomear colunas para nomes mais claros
print("\n4. Renomeando colunas...")
fact = fact.rename(columns={
    'Triagem Vermelha': 'Atendimentos_Vermelha',
    'Triagem Laranja': 'Atendimentos_Laranja',
    'Triagem Amarela': 'Atendimentos_Amarela',
    'Triagem Verde': 'Atendimentos_Verde',
    'Triagem Azul': 'Atendimentos_Azul',
    'Triagem Branca': 'Atendimentos_Branca',
    'Sem Triagem': 'Atendimentos_SemTriagem',
    'N.º doentes': 'NumDoentes',
    'Custo Médio': 'CustoMedio'
})

# Selecionar e ordenar colunas finais
colunas_finais = [
    # Chaves
    'Período', 'Região', 'Instituição',
    # Atendimentos
    'Atendimentos_Vermelha', 'Atendimentos_Laranja', 'Atendimentos_Amarela',
    'Atendimentos_Verde', 'Atendimentos_Azul', 'Atendimentos_Branca',
    'Atendimentos_SemTriagem', 'TotalAtendimentos',
    # Recursos Humanos
    'Médicos', 'MedicosInternos', 'Enfermeiros',
    # Custos
    'Despesa', 'NumDoentes', 'CustoMedio'
]

fact = fact[colunas_finais]

print(f"   ✓ {len(colunas_finais)} colunas finais")

# Estatísticas
print("\n5. Estatísticas da tabela consolidada:")
print(f"   Total de linhas: {len(fact)}")
print(f"   Total de colunas: {len(fact.columns)}")
print(f"\n   Cobertura de dados:")
print(f"   • Atendimentos: {fact['TotalAtendimentos'].notna().sum()} linhas ({fact['TotalAtendimentos'].notna().sum()/len(fact)*100:.1f}%)")
print(f"   • RH (Médicos): {fact['Médicos'].notna().sum()} linhas ({fact['Médicos'].notna().sum()/len(fact)*100:.1f}%)")
print(f"   • Custos: {fact['Despesa'].notna().sum()} linhas ({fact['Despesa'].notna().sum()/len(fact)*100:.1f}%)")

# Mostrar sample
print("\n6. Primeiras 3 linhas (sample):")
print(fact.head(3).to_string())

# Guardar
print("\n7. Guardando ficheiro...")
fact.to_csv('FactAtendimentosUrgencia.csv', 
            sep=';', 
            index=False, 
            encoding='utf-8-sig')

print("\n" + "="*80)
print("✅ FACTUAL CONSOLIDADA CRIADA COM SUCESSO!")
print("="*80)
print(f"\nFicheiro: FactAtendimentosUrgencia.csv")
print(f"Linhas: {len(fact)}")
print(f"Colunas: {len(fact.columns)}")
print("\nPronta para importar no Power BI!")
print("\nPróximos passos:")
print("  1. Importar FactAtendimentosUrgencia.csv")
print("  2. Importar monitorizacao-sazonal-csh.csv (já está pronto)")
print("  3. Criar DimCalendar, DimRegião, DimInstituição, DimIndicador")
print("  4. Estabelecer relacionamentos")
print("="*80)
