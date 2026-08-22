import pandas as pd

# Ler o CSV de custos
df = pd.read_csv('custo-de-tratamento-mensal-por-doente.csv', 
                 sep=';', 
                 encoding='utf-8-sig')

print(f"Total de linhas: {len(df)}")

# Mostrar as instituições que vamos alterar
print("\n=== Instituições a serem alteradas: ===")
instituicoes_alterar = [
    'Unidade Local de Saúde de Gaia/Espinho EPE',
    'Centro Hospitalar Universitário Lisboa Central EPE',
    'Centro Hospitalar Universitário Lisboa Norte EPE'
]

for inst in instituicoes_alterar:
    count = (df['Instituição Hospitalar'] == inst).sum()
    if count > 0:
        print(f"  - {inst} ({count} ocorrências)")

# Criar dicionário de mapeamento
mapeamento = {
    'Unidade Local de Saúde de Gaia/Espinho EPE': 'Unidade Local de Saúde de Vila Nova de Gaia/Espinho EPE',
    'Centro Hospitalar Universitário Lisboa Central EPE': 'Centro Hospitalar Universitário de Lisboa Central EPE',
    'Centro Hospitalar Universitário Lisboa Norte EPE': 'Centro Hospitalar Universitário de Lisboa Norte EPE'
}

# Aplicar as alterações
df['Instituição Hospitalar'] = df['Instituição Hospitalar'].replace(mapeamento)

print("\n=== Após alteração: ===")
for inst_nova in mapeamento.values():
    count = (df['Instituição Hospitalar'] == inst_nova).sum()
    print(f"  - {inst_nova} ({count} ocorrências)")

# Guardar o arquivo atualizado
df.to_csv('custo-de-tratamento-mensal-por-doente.csv', 
          sep=';', 
          index=False, 
          encoding='utf-8-sig')

print("\n✓ Arquivo atualizado com sucesso!")
print("  Nomes das instituições padronizados para corresponder ao ficheiro de atendimentos")
