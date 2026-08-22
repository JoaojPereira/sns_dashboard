import pandas as pd

# Ler o CSV
df = pd.read_csv('trabalhadores-por-grupo-profissional.csv', 
                 sep=';', 
                 encoding='utf-8-sig')

print(f"Total de linhas ANTES: {len(df)}")

# Identificar instituições a remover (Administração Regional de Saúde)
palavras_remover = [
    'Administração Regional de Saúde'
]

# Contar quantas linhas serão removidas
linhas_remover = df['Instituição'].str.contains('|'.join(palavras_remover), case=False, na=False)
count_remover = linhas_remover.sum()

print(f"\n=== Instituições a REMOVER: ===")
inst_remover = df[linhas_remover]['Instituição'].unique()
for inst in sorted(inst_remover):
    count = (df['Instituição'] == inst).sum()
    print(f"  - {inst}: {count} linhas")

# Remover as linhas
df = df[~linhas_remover]

print(f"\n➜ Total de linhas removidas: {count_remover}")
print(f"Total de linhas APÓS remoção: {len(df)}")

# Guardar com nome diferente para evitar conflito
df.to_csv('trabalhadores-por-grupo-profissional_temp.csv', 
          sep=';', 
          index=False, 
          encoding='utf-8-sig')

print("\n✓ Arquivo guardado temporariamente como: trabalhadores-por-grupo-profissional_temp.csv")
print("  Por favor, feche o ficheiro original no editor e depois renomeie este ficheiro.")
