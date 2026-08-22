import pandas as pd

# Ler o CSV
df = pd.read_csv('monitorizacao-sazonal-csh.csv', 
                 sep=';', 
                 encoding='utf-8-sig')

print(f"Total de linhas: {len(df)}")

# Mostrar indicadores únicos atuais
print("\n=== INDICADORES ATUAIS: ===")
indicadores_atuais = df['Indicador'].unique()
for i, ind in enumerate(sorted(indicadores_atuais), 1):
    count = (df['Indicador'] == ind).sum()
    print(f"{i}. {ind}")
    print(f"   ({count} ocorrências)")
    print()

# Criar mapeamento para versões mais curtas
mapeamento_indicadores = {
    'Tempo médio de espera entre a triagem e a primeira observação médica (rede de urgência hospitalar)': 
        'Tempo Médio Espera Triagem-Observação',
    
    'Taxa diária de atendimentos urgentes com prioridade verde ou azul': 
        'Taxa Atendimentos Verde/Azul',
    
    'Taxa diária de atendimentos urgentes com internamento': 
        'Taxa Atendimentos c/ Internamento',
    
    'Número estimado de episódios de urgência': 
        'Nº Episódios Urgência'
}

# Aplicar as alterações
df['Indicador'] = df['Indicador'].replace(mapeamento_indicadores)

print("\n=== INDICADORES APÓS ENCURTAMENTO: ===")
indicadores_novos = df['Indicador'].unique()
for i, ind in enumerate(sorted(indicadores_novos), 1):
    count = (df['Indicador'] == ind).sum()
    print(f"{i}. {ind} ({count} ocorrências)")

# Guardar o arquivo atualizado
df.to_csv('monitorizacao-sazonal-csh.csv', 
          sep=';', 
          index=False, 
          encoding='utf-8-sig')

print("\n✓ Arquivo atualizado com sucesso!")
print("  Descrições dos indicadores encurtadas mantendo o sentido")
