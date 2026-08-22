import pandas as pd

# Ler o CSV com encoding UTF-8
df = pd.read_csv('monitorizacao-sazonal-csh.csv', 
                 sep=';', 
                 encoding='utf-8')

print("Colunas originais:")
print(df.columns.tolist())
print(f"\nTotal de linhas: {len(df)}")

# Mostrar valores únicos da coluna Região/ARS
print("\nValores únicos da coluna 'Região/ARS' antes:")
print(sorted(df['Região/ARS'].unique()))

# Padronizar os nomes das regiões para ficarem iguais aos outros ficheiros
mapeamento_regioes = {
    'ARS Lisboa e Vale do Tejo': 'Região de Saúde LVT',
    'ARS Centro': 'Região de Saúde do Centro',
    'ARS Norte': 'Região de Saúde Norte',
    'ARS Alentejo': 'Região de Saúde do Alentejo',
    'ARS Algarve': 'Região de Saúde do Algarve'
}

df['Região/ARS'] = df['Região/ARS'].replace(mapeamento_regioes)

# Renomear a coluna para 'Região' (sem /ARS)
df = df.rename(columns={'Região/ARS': 'Região'})

print("\nValores únicos da coluna 'Região' após padronização:")
print(sorted(df['Região'].unique()))

print("\nColunas finais:")
print(df.columns.tolist())

# Arredondar valores para 2 casas decimais
df['Valor'] = df['Valor'].round(2)

print("\nExemplo de dados após tratamento:")
print(df.head(5))

# Guardar o arquivo limpo (UTF-8 com BOM para Excel reconhecer corretamente)
df.to_csv('monitorizacao-sazonal-csh.csv', 
          sep=';', 
          index=False, 
          encoding='utf-8-sig')

print("\n✓ Arquivo guardado como: monitorizacao-sazonal-csh.csv")
print("  - Coluna renomeada: 'Região/ARS' → 'Região'")
print("  - Região padronizada para o formato dos outros ficheiros")
print("  - Coluna 'Valor' arredondada para 2 casas decimais")
print("  - Encoding correto (UTF-8-sig)")
