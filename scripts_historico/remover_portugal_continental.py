import pandas as pd

# Ler o CSV
df = pd.read_csv('monitorizacao-sazonal-csh.csv', 
                 sep=';', 
                 encoding='utf-8-sig')

print(f"Total de linhas ANTES: {len(df)}")

# Mostrar valores únicos da coluna Região
print("\nRegiões atuais:")
for regiao in sorted(df['Região'].unique()):
    count = (df['Região'] == regiao).sum()
    print(f"  - {regiao}: {count} linhas")

# Contar quantas linhas têm "Portugal Continental"
portugal_count = (df['Região'] == 'Portugal Continental').sum()
print(f"\n➜ Linhas com 'Portugal Continental' a remover: {portugal_count}")

# Remover linhas com "Portugal Continental"
df = df[df['Região'] != 'Portugal Continental']

print(f"\nTotal de linhas APÓS remoção: {len(df)}")

print("\nRegiões finais:")
for regiao in sorted(df['Região'].unique()):
    count = (df['Região'] == regiao).sum()
    print(f"  - {regiao}: {count} linhas")

# Guardar o arquivo atualizado
df.to_csv('monitorizacao-sazonal-csh.csv', 
          sep=';', 
          index=False, 
          encoding='utf-8-sig')

print("\n✓ Arquivo atualizado com sucesso!")
print(f"  Removidas {portugal_count} linhas de 'Portugal Continental'")
