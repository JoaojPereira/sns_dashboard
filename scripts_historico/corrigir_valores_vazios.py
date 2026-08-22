import pandas as pd
import numpy as np

# Ler o ficheiro
df = pd.read_csv('FactAtendimentosUrgencia.csv', sep=';', encoding='utf-8-sig')

print("Verificando valores vazios...")
print("\nResumo de valores nulos/vazios por coluna:")
print(df.isnull().sum())

# Colunas numéricas que devem ser inteiros
colunas_inteiras = [
    'Atendimentos_Vermelha', 'Atendimentos_Laranja', 'Atendimentos_Amarela',
    'Atendimentos_Verde', 'Atendimentos_Azul', 'Atendimentos_Branca',
    'Atendimentos_SemTriagem', 'TotalAtendimentos',
    'Médicos', 'MedicosInternos', 'Enfermeiros', 'TotalProfissionais',
    'NumDoentes'
]

# Colunas decimais
colunas_decimais = ['Despesa', 'CustoMedio']

# Substituir NaN e valores vazios por 0 nas colunas inteiras
for col in colunas_inteiras:
    if col in df.columns:
        df[col] = df[col].fillna(0).replace('', 0).replace(' ', 0)
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

# Substituir NaN e valores vazios nas colunas decimais (manter como float, mas sem NaN)
for col in colunas_decimais:
    if col in df.columns:
        df[col] = df[col].fillna(0).replace('', 0).replace(' ', 0)
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).round(2)

print("\n\nDepois da correção:")
print(df.head(5))
print("\n\nTipos de dados:")
print(df.dtypes)
print("\n\nVerificando se ainda existem NaN:")
print(df.isnull().sum())

# Guardar
df.to_csv('FactAtendimentosUrgencia.csv', sep=';', index=False, encoding='utf-8-sig')

print("\n✅ Ficheiro corrigido! Todos os valores vazios substituídos por 0")
print(f"Total de linhas: {len(df)}")
