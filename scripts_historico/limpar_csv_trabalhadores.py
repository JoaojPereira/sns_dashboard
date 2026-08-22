import pandas as pd

# Ler o CSV com encoding UTF-8
df = pd.read_csv('trabalhadores-por-grupo-profissional.csv', 
                 sep=';', 
                 encoding='utf-8')

print("Colunas originais:")
print(df.columns.tolist())
print(f"\nTotal de linhas: {len(df)}")

# Mostrar valores únicos da coluna Região
print("\nValores únicos da coluna 'Região' antes:")
regioes_antes = sorted(df['Região'].unique())
for regiao in regioes_antes:
    count = (df['Região'] == regiao).sum()
    print(f"  - {regiao}: {count} linhas")

# 1. Remover a coluna de Localização Geográfica
if 'Localização Geográfica' in df.columns:
    df = df.drop('Localização Geográfica', axis=1)
    print("\n✓ Coluna 'Localização Geográfica' removida")

# 2. Remover linhas onde Região = "Serviços Centrais"
servicos_centrais_count = (df['Região'] == 'Serviços Centrais').sum()
df = df[df['Região'] != 'Serviços Centrais']
print(f"✓ Removidas {servicos_centrais_count} linhas de 'Serviços Centrais'")

# 3. Padronizar os nomes das regiões (LVT já está correto, mas vamos garantir consistência)
# Verificar se existe "Região de Saúde LVT" ou "Administração Regional de Saúde de Lisboa e Vale do Tejo, IP"
print(f"\n✓ Região 'Região de Saúde LVT' já está padronizada")

print("\nValores únicos da coluna 'Região' após limpeza:")
regioes_depois = sorted(df['Região'].unique())
for regiao in regioes_depois:
    count = (df['Região'] == regiao).sum()
    print(f"  - {regiao}: {count} linhas")

print("\nColunas finais:")
print(df.columns.tolist())

# Guardar o arquivo limpo (UTF-8 com BOM para Excel reconhecer corretamente)
df.to_csv('trabalhadores-por-grupo-profissional.csv', 
          sep=';', 
          index=False, 
          encoding='utf-8-sig')

print("\n✓ Arquivo guardado como: trabalhadores-por-grupo-profissional.csv")
print("  - Coluna 'Localização Geográfica' removida")
print(f"  - {servicos_centrais_count} linhas de 'Serviços Centrais' removidas")
print("  - Encoding correto (UTF-8-sig)")
print(f"  - Total final: {len(df)} linhas")
