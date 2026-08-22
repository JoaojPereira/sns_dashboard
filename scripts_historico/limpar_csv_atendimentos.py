import pandas as pd

# Ler o CSV com encoding UTF-8
df = pd.read_csv('atendimentos-em-urgencia-triagem-manchester.csv', 
                 sep=';', 
                 encoding='utf-8')

print("Colunas originais:")
print(df.columns.tolist())
print(f"\nTotal de linhas: {len(df)}")

# Remover a coluna de Localização Geográfica
if 'Localização Geográfica' in df.columns:
    df = df.drop('Localização Geográfica', axis=1)
    print("\nColuna 'Localização Geográfica' removida com sucesso!")

print("\nColunas após limpeza:")
print(df.columns.tolist())

# Guardar o arquivo limpo (UTF-8 com BOM para Excel reconhecer corretamente)
df.to_csv('atendimentos-em-urgencia-triagem-manchester_limpo.csv', 
          sep=';', 
          index=False, 
          encoding='utf-8-sig')

print("\n✓ Arquivo guardado como: atendimentos-em-urgencia-triagem-manchester_limpo.csv")
print("  (Este arquivo abrirá corretamente no Excel sem caracteres estranhos)")
