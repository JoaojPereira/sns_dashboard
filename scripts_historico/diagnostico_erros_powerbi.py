import pandas as pd
import numpy as np

print("="*80)
print("DIAGNÓSTICO DE PROBLEMAS DE CONVERSÃO")
print("="*80)

# Ler ficheiro
df = pd.read_csv('FactAtendimentosUrgencia.csv', sep=';', encoding='utf-8-sig')

print(f"\n1. Total de linhas: {len(df)}")
print(f"   Total de colunas: {len(df.columns)}")

print("\n2. Tipos de dados atuais:")
print(df.dtypes)

print("\n3. Verificando valores problemáticos por coluna:")

for col in df.columns:
    # Contar valores vazios, NaN, infinitos
    total = len(df)
    nulls = df[col].isna().sum()
    
    # Verificar se há valores não-numéricos em colunas que deveriam ser numéricas
    if col not in ['Período']:
        try:
            # Tentar converter para numérico
            pd.to_numeric(df[col], errors='coerce')
            nao_numericos = df[col][pd.to_numeric(df[col], errors='coerce').isna() & df[col].notna()]
            
            if len(nao_numericos) > 0:
                print(f"\n❌ {col}:")
                print(f"   Valores não-numéricos encontrados: {len(nao_numericos)}")
                print(f"   Exemplos: {nao_numericos.unique()[:5]}")
        except:
            pass
    
    if nulls > 0:
        print(f"\n⚠️  {col}: {nulls} valores NULL")

print("\n4. Verificando linhas com problemas:")

# Verificar se há caracteres especiais ou espaços extras
for col in ['RegiaoID', 'InstituicaoID', 'Médicos', 'Enfermeiros']:
    valores_unicos = df[col].unique()
    print(f"\n   {col}: {len(valores_unicos)} valores únicos")
    print(f"   Tipo dos valores: {type(valores_unicos[0])}")
    print(f"   Sample: {valores_unicos[:5]}")

print("\n5. Verificando se há espaços ou caracteres estranhos:")
# Verificar colunas numéricas
cols_numericas = ['RegiaoID', 'InstituicaoID', 'Atendimentos_Vermelha', 'Médicos', 'Enfermeiros']

for col in cols_numericas:
    # Converter para string e verificar se há espaços
    df_str = df[col].astype(str)
    com_espacos = df_str[df_str.str.contains(' ', na=False)]
    
    if len(com_espacos) > 0:
        print(f"\n❌ {col}: {len(com_espacos)} valores com espaços")
        print(f"   Exemplos: {com_espacos.head(3).tolist()}")

print("\n6. Sample das primeiras 3 linhas completas:")
print(df.head(3).to_string())
