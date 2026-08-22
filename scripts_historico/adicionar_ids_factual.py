import pandas as pd

print("="*80)
print("ADICIONANDO IDs DE REGIÃO E INSTITUIÇÃO À FACTUAL")
print("="*80)

# Ler os ficheiros
fact = pd.read_csv('FactAtendimentosUrgencia.csv', sep=';', encoding='utf-8-sig')
dim_regiao = pd.read_csv('DimRegiao.csv', sep=';', encoding='utf-8-sig')
dim_instituicao = pd.read_csv('DimInstituicao.csv', sep=';', encoding='utf-8-sig')

print(f"\n1. Ficheiros carregados:")
print(f"   FactAtendimentosUrgencia: {len(fact)} linhas")
print(f"   DimRegiao: {len(dim_regiao)} linhas")
print(f"   DimInstituicao: {len(dim_instituicao)} linhas")

# Fazer merge para adicionar RegiaoID
print("\n2. Adicionando RegiaoID...")
fact = fact.merge(
    dim_regiao[['RegiaoNome', 'RegiaoID']],
    left_on='Região',
    right_on='RegiaoNome',
    how='left'
)
fact = fact.drop(columns=['RegiaoNome'])

print(f"   ✓ RegiaoID adicionado")
print(f"   Valores únicos: {fact['RegiaoID'].nunique()}")
print(f"   Nulls: {fact['RegiaoID'].isna().sum()}")

# Fazer merge para adicionar InstituicaoID
print("\n3. Adicionando InstituicaoID...")
fact = fact.merge(
    dim_instituicao[['InstituicaoNome', 'InstituicaoID']],
    left_on='Instituição',
    right_on='InstituicaoNome',
    how='left'
)
fact = fact.drop(columns=['InstituicaoNome'])

print(f"   ✓ InstituicaoID adicionado")
print(f"   Valores únicos: {fact['InstituicaoID'].nunique()}")
print(f"   Nulls: {fact['InstituicaoID'].isna().sum()}")

# Reorganizar colunas: IDs primeiro, depois remover nomes de Região e Instituição
colunas_ordenadas = [
    'Período', 'RegiaoID', 'InstituicaoID',
    'Atendimentos_Vermelha', 'Atendimentos_Laranja', 'Atendimentos_Amarela',
    'Atendimentos_Verde', 'Atendimentos_Azul', 'Atendimentos_Branca',
    'Atendimentos_SemTriagem', 'TotalAtendimentos',
    'Médicos', 'MedicosInternos', 'Enfermeiros',
    'Despesa', 'NumDoentes', 'CustoMedio'
]

fact = fact[colunas_ordenadas]

print("\n4. Estrutura final:")
print(f"   Total de colunas: {len(fact.columns)}")
print(f"   Colunas: {list(fact.columns)}")

# Converter IDs para inteiro
fact['RegiaoID'] = fact['RegiaoID'].astype(int)
fact['InstituicaoID'] = fact['InstituicaoID'].astype(int)

# Mostrar sample
print("\n5. Primeiras 3 linhas:")
print(fact.head(3).to_string())

# Guardar
fact.to_csv('FactAtendimentosUrgencia.csv', sep=';', index=False, encoding='utf-8-sig')

print("\n" + "="*80)
print("✅ FACTUAL ATUALIZADA COM SUCESSO!")
print("="*80)
print(f"\nAgora a FactAtendimentosUrgencia tem:")
print(f"  • {len(fact)} linhas")
print(f"  • {len(fact.columns)} colunas")
print(f"  • RegiaoID (1-5)")
print(f"  • InstituicaoID (1-75)")
print(f"  • SEM as colunas Região e Instituição (nome)")
print("\nRelacionamentos no Power BI:")
print("  DimRegiao[RegiaoID] → FactAtendimentosUrgencia[RegiaoID]")
print("  DimInstituicao[InstituicaoID] → FactAtendimentosUrgencia[InstituicaoID]")
