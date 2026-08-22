import pandas as pd

# Ler o CSV
df = pd.read_csv('trabalhadores-por-grupo-profissional.csv', 
                 sep=';', 
                 encoding='utf-8-sig')

print(f"Total de linhas ANTES: {len(df)}")
print(f"Instituições únicas ANTES: {df['Instituição'].nunique()}")

# Lista de instituições a remover
instituicoes_remover = [
    # 3 IPO (Oncologia)
    'Instituto Português de Oncologia de Coimbra Francisco Gentil EPE',
    'Instituto Português de Oncologia de Lisboa Francisco Gentil EPE',
    'Instituto Português de Oncologia do Porto Francisco Gentil EPE',
    
    # 2 Hospitais Psiquiátricos
    'Centro Hospitalar Psiquiátrico de Lisboa',
    'Hospital de Magalhães Lemos EPE',
    
    # 4 Hospitais/Centros menores
    'Centro Medicina de Reabilitação da Região Centro - Rovisco Pais',
    'Hospital Arcebispo João Crisóstomo - Cantanhede',
    'Hospital Doutor Francisco Zagalo - Ovar',
    'Hospital José Luciano Castro - Anadia',
    
    # 1 Instituto Oftalmologia
    'Instituto de Oftalmologia Gama Pinto',
    
    # Duplicado (Centro Hospitalar do Médio Tejo aparece 2x)
    'Centro Hospitalar do Médio Tejo EPE'
]

print("\n=== Instituições a REMOVER: ===")
total_linhas_remover = 0
for inst in instituicoes_remover:
    count = (df['Instituição'] == inst).sum()
    if count > 0:
        print(f"  • {inst}: {count} linhas")
        total_linhas_remover += count
    else:
        print(f"  ⚠ {inst}: NÃO ENCONTRADA")

# Remover as linhas
df = df[~df['Instituição'].isin(instituicoes_remover)]

print(f"\n➜ Total de linhas removidas: {total_linhas_remover}")
print(f"Total de linhas APÓS remoção: {len(df)}")
print(f"Instituições únicas APÓS: {df['Instituição'].nunique()}")

# Mostrar instituições que restaram (sample)
print("\n=== Instituições finais (primeiras 10): ===")
for inst in sorted(df['Instituição'].unique())[:10]:
    count = (df['Instituição'] == inst).sum()
    print(f"  • {inst}: {count} linhas")

# Guardar o arquivo atualizado
df.to_csv('trabalhadores-por-grupo-profissional.csv', 
          sep=';', 
          index=False, 
          encoding='utf-8-sig')

print("\n✓ Arquivo atualizado com sucesso!")
print(f"  Removidas {len(instituicoes_remover)} instituições especializadas")
print(f"  Total de {total_linhas_remover} linhas removidas")
