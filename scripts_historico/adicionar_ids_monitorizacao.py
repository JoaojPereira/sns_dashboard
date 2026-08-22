import pandas as pd

print("="*80)
print("ADICIONANDO IDs À FACT MONITORIZAÇÃO")
print("="*80)

# Ler ficheiros
fact_mon = pd.read_csv('monitorizacao-sazonal-csh.csv', sep=';', encoding='utf-8-sig')
dim_regiao = pd.read_csv('DimRegiao.csv', sep=';', encoding='utf-8-sig')
dim_indicador = pd.read_csv('DimIndicador.csv', sep=';', encoding='utf-8-sig')

print(f"\n1. Ficheiros carregados:")
print(f"   FactMonitorizacao: {len(fact_mon)} linhas")
print(f"   DimRegiao: {len(dim_regiao)} linhas")
print(f"   DimIndicador: {len(dim_indicador)} linhas")

# Mostrar indicadores para debug
print(f"\n2. Indicadores na dimensão:")
for idx, row in dim_indicador.iterrows():
    print(f"   ID {row['IndicadorID']}: {row['IndicadorNome']}")

print(f"\n3. Indicadores únicos na factual:")
print(fact_mon['Indicador'].unique())

# Fazer merge para adicionar RegiaoID
print("\n4. Adicionando RegiaoID...")
fact_mon = fact_mon.merge(
    dim_regiao[['RegiaoNome', 'RegiaoID']],
    left_on='Região',
    right_on='RegiaoNome',
    how='left'
)
fact_mon = fact_mon.drop(columns=['RegiaoNome'])

print(f"   ✓ RegiaoID adicionado")
print(f"   Valores únicos: {fact_mon['RegiaoID'].nunique()}")
print(f"   Nulls: {fact_mon['RegiaoID'].isna().sum()}")

# Fazer merge para adicionar IndicadorID
print("\n5. Adicionando IndicadorID...")
fact_mon = fact_mon.merge(
    dim_indicador[['IndicadorNome', 'IndicadorID']],
    left_on='Indicador',
    right_on='IndicadorNome',
    how='left'
)
fact_mon = fact_mon.drop(columns=['IndicadorNome'])

print(f"   ✓ IndicadorID adicionado")
print(f"   Valores únicos: {fact_mon['IndicadorID'].nunique()}")
print(f"   Nulls: {fact_mon['IndicadorID'].isna().sum()}")

# Verificar se há NULLs em IndicadorID
if fact_mon['IndicadorID'].isna().sum() > 0:
    print("\n⚠️  ATENÇÃO: Há indicadores sem match!")
    sem_match = fact_mon[fact_mon['IndicadorID'].isna()]['Indicador'].unique()
    print(f"   Indicadores sem ID: {sem_match}")

# Reorganizar colunas: só IDs, sem nomes
colunas_ordenadas = [
    'Período',
    'RegiaoID',
    'IndicadorID',
    'Valor'
]

fact_mon = fact_mon[colunas_ordenadas]

# Converter IDs para inteiro (se não houver nulls)
if fact_mon['RegiaoID'].isna().sum() == 0:
    fact_mon['RegiaoID'] = fact_mon['RegiaoID'].astype(int)
if fact_mon['IndicadorID'].isna().sum() == 0:
    fact_mon['IndicadorID'] = fact_mon['IndicadorID'].astype(int)

print("\n6. Estrutura final:")
print(f"   Total de colunas: {len(fact_mon.columns)}")
print(f"   Colunas: {list(fact_mon.columns)}")

# Mostrar tipos
print("\n7. Tipos de dados:")
print(fact_mon.dtypes)

# Mostrar sample
print("\n8. Primeiras 5 linhas:")
print(fact_mon.head(5).to_string())

# Guardar
fact_mon.to_csv('monitorizacao-sazonal-csh.csv', sep=';', index=False, encoding='utf-8-sig')

print("\n" + "="*80)
print("✅ FACT MONITORIZAÇÃO ATUALIZADA COM SUCESSO!")
print("="*80)
print(f"\nAgora monitorizacao-sazonal-csh.csv tem:")
print(f"  • {len(fact_mon)} linhas")
print(f"  • {len(fact_mon.columns)} colunas (Período, RegiaoID, IndicadorID, Valor)")
print(f"  • SEM as colunas Região e Indicador (nome)")
print("\nRelacionamentos no Power BI:")
print("  DimRegiao[RegiaoID] → monitorizacao[RegiaoID]")
print("  DimIndicador[IndicadorID] → monitorizacao[IndicadorID]")
