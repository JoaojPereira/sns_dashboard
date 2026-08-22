import pandas as pd

# Ler o CSV limpo
df = pd.read_csv('atendimentos-em-urgencia-triagem-manchester_limpo.csv', 
                 sep=';', 
                 encoding='utf-8-sig')

print(f"Total de linhas: {len(df)}")

# Contar quantas instituições têm PPP
ppp_count = df['Instituição'].str.contains('PPP', na=False).sum()
print(f"\nInstituições com PPP encontradas: {ppp_count}")

if ppp_count > 0:
    # Mostrar algumas instituições com PPP
    print("\nExemplos de instituições com PPP:")
    print(df[df['Instituição'].str.contains('PPP', na=False)]['Instituição'].unique())

# Substituir PPP por EPE na coluna Instituição
df['Instituição'] = df['Instituição'].str.replace('PPP', 'EPE', regex=False)

# Verificar se a substituição foi feita
ppp_remaining = df['Instituição'].str.contains('PPP', na=False).sum()
print(f"\nInstituições com PPP após alteração: {ppp_remaining}")

# Guardar o arquivo atualizado
df.to_csv('atendimentos-em-urgencia-triagem-manchester_limpo.csv', 
          sep=';', 
          index=False, 
          encoding='utf-8-sig')

print("\n✓ Arquivo atualizado com sucesso!")
print("  Todas as ocorrências de 'PPP' foram substituídas por 'EPE' na coluna Instituição")
