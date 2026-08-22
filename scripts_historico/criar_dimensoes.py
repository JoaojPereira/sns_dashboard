import pandas as pd

print("="*80)
print("CRIANDO TABELAS DIMENSÃO")
print("="*80)

# 1. DimRegião
print("\n1. Criando DimRegião...")
dim_regiao = pd.DataFrame({
    'RegiaoID': [1, 2, 3, 4, 5],
    'RegiaoNome': [
        'Região de Saúde Norte',
        'Região de Saúde do Centro',
        'Região de Saúde LVT',
        'Região de Saúde do Alentejo',
        'Região de Saúde do Algarve'
    ],
    'RegiaoSigla': ['Norte', 'Centro', 'LVT', 'Alentejo', 'Algarve'],
    'Ordem': [1, 2, 3, 4, 5]
})

dim_regiao.to_csv('DimRegiao.csv', sep=';', index=False, encoding='utf-8-sig')
print(f"   ✓ {len(dim_regiao)} regiões criadas")
print(dim_regiao.to_string(index=False))

# 2. DimInstituição
print("\n2. Criando DimInstituição...")

# Ler as instituições da factual consolidada
df_fact = pd.read_csv('FactAtendimentosUrgencia.csv', sep=';', encoding='utf-8-sig')

# Extrair instituições únicas com região
inst_unicas = df_fact[['Instituição', 'Região']].drop_duplicates().sort_values('Instituição').reset_index(drop=True)

# Criar DimInstituição
dim_instituicao = pd.DataFrame({
    'InstituicaoID': range(1, len(inst_unicas) + 1),
    'InstituicaoNome': inst_unicas['Instituição'].values,
    'Regiao': inst_unicas['Região'].values
})

# Adicionar coluna Tipo (classificação)
def classificar_tipo(nome):
    if 'Unidade Local de Saúde' in nome or 'ULS' in nome:
        return 'ULS'
    elif 'Centro Hospitalar Universitário' in nome:
        return 'CHU'
    elif 'Centro Hospitalar' in nome:
        return 'CH'
    elif 'Hospital' in nome:
        return 'Hospital'
    else:
        return 'Outro'

dim_instituicao['Tipo'] = dim_instituicao['InstituicaoNome'].apply(classificar_tipo)

# Mapear Região para RegiaoID
mapa_regiao = {
    'Região de Saúde Norte': 1,
    'Região de Saúde do Centro': 2,
    'Região de Saúde LVT': 3,
    'Região de Saúde do Alentejo': 4,
    'Região de Saúde do Algarve': 5
}
dim_instituicao['RegiaoID'] = dim_instituicao['Regiao'].map(mapa_regiao)

# Reorganizar colunas
dim_instituicao = dim_instituicao[['InstituicaoID', 'InstituicaoNome', 'Tipo', 'RegiaoID']]

dim_instituicao.to_csv('DimInstituicao.csv', sep=';', index=False, encoding='utf-8-sig')
print(f"   ✓ {len(dim_instituicao)} instituições criadas")
print(f"\n   Distribuição por tipo:")
print(dim_instituicao['Tipo'].value_counts().to_string())

# 3. DimIndicador
print("\n3. Criando DimIndicador...")
dim_indicador = pd.DataFrame({
    'IndicadorID': [1, 2, 3, 4],
    'IndicadorNome': [
        'Tempo Médio Espera Triagem-Observação',
        'Taxa Atendimentos Verde/Azul',
        'Taxa Atendimentos c/ Internamento',
        'Nº Episódios Urgência'
    ],
    'IndicadorGrupo': [
        'Tempo de Espera',
        'Prioridade',
        'Internamento',
        'Volume'
    ],
    'Unidade': ['minutos', '%', '%', 'número']
})

dim_indicador.to_csv('DimIndicador.csv', sep=';', index=False, encoding='utf-8-sig')
print(f"   ✓ {len(dim_indicador)} indicadores criados")
print(dim_indicador.to_string(index=False))

print("\n" + "="*80)
print("✅ TODAS AS TABELAS DIMENSÃO CRIADAS!")
print("="*80)
print("\nFicheiros criados:")
print("  • DimRegiao.csv (5 linhas)")
print("  • DimInstituicao.csv (75 linhas)")
print("  • DimIndicador.csv (4 linhas)")
print("\n📋 RESUMO DO MODELO:")
print("\nDIMENSÕES (4):")
print("  1. DimCalendar - usar DimCalendar.m no Power BI")
print("  2. DimRegiao.csv - 5 regiões")
print("  3. DimInstituicao.csv - 75 instituições")
print("  4. DimIndicador.csv - 4 indicadores")
print("\nFACTUAIS (2):")
print("  1. FactAtendimentosUrgencia.csv - 6.020 linhas")
print("  2. monitorizacao-sazonal-csh.csv - 64.816 linhas")
print("\n🎯 Modelo Star Schema completo e pronto para Power BI!")
print("="*80)
