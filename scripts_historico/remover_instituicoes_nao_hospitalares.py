import pandas as pd

# Ler o CSV
df = pd.read_csv('trabalhadores-por-grupo-profissional.csv', 
                 sep=';', 
                 encoding='utf-8-sig')

print(f"Total de linhas ANTES: {len(df)}")

# Mostrar instituições únicas
print("\n=== Instituições atuais: ===")
instituicoes = df['Instituição'].unique()
for inst in sorted(instituicoes):
    count = (df['Instituição'] == inst).sum()
    print(f"  - {inst}: {count} linhas")

# Identificar instituições a remover (que contêm certas palavras-chave)
palavras_remover = [
    'Administração Regional de Saúde',
    'Administração Central',
    'Infarmed',
    'Ação Governativa',
    'Instituto Nacional',
    'Agência de'
]

# Contar quantas linhas serão removidas
linhas_remover = df['Instituição'].str.contains('|'.join(palavras_remover), case=False, na=False)
count_remover = linhas_remover.sum()

print(f"\n=== Instituições a REMOVER (não hospitalares): ===")
inst_remover = df[linhas_remover]['Instituição'].unique()
for inst in sorted(inst_remover):
    count = (df['Instituição'] == inst).sum()
    print(f"  - {inst}: {count} linhas")

# Remover as linhas
df = df[~linhas_remover]

print(f"\n➜ Total de linhas removidas: {count_remover}")
print(f"Total de linhas APÓS remoção: {len(df)}")

# Mostrar instituições finais
print("\n=== Instituições FINAIS (apenas hospitalares): ===")
instituicoes_finais = df['Instituição'].unique()
print(f"Total de instituições únicas: {len(instituicoes_finais)}")
for inst in sorted(instituicoes_finais):
    count = (df['Instituição'] == inst).sum()
    print(f"  - {inst}: {count} linhas")

# Guardar o arquivo atualizado
df.to_csv('trabalhadores-por-grupo-profissional.csv', 
          sep=';', 
          index=False, 
          encoding='utf-8-sig')

print("\n✓ Arquivo atualizado com sucesso!")
print(f"  Removidas {count_remover} linhas de instituições não hospitalares")
print(f"  Restam apenas {len(instituicoes_finais)} instituições hospitalares")
