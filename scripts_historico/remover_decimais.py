import pandas as pd

# Ler o ficheiro
df = pd.read_csv('FactAtendimentosUrgencia.csv', sep=';', encoding='utf-8-sig')

print("Antes da conversão:")
print(df.head(3))
print("\nTipos de dados originais:")
print(df.dtypes)

# Colunas que devem ser inteiros (sem casas decimais)
colunas_inteiras = [
    'Atendimentos_Vermelha',
    'Atendimentos_Laranja', 
    'Atendimentos_Amarela',
    'Atendimentos_Verde',
    'Atendimentos_Azul',
    'Atendimentos_Branca',
    'Atendimentos_SemTriagem',
    'TotalAtendimentos',
    'Médicos',
    'MedicosInternos',
    'Enfermeiros',
    'TotalProfissionais',
    'NumDoentes'
]

# Converter para inteiro (substituindo NaN por 0 primeiro)
for col in colunas_inteiras:
    if col in df.columns:
        df[col] = df[col].fillna(0).astype(int)

print("\n\nDepois da conversão:")
print(df.head(3))
print("\nTipos de dados finais:")
print(df.dtypes)

# Guardar
df.to_csv('FactAtendimentosUrgencia.csv', sep=';', index=False, encoding='utf-8-sig')

print("\n✅ Ficheiro atualizado com números inteiros (sem casas decimais)!")
print(f"Total de linhas: {len(df)}")
