import pandas as pd

# Carregar o arquivo CSV acumulado com separador correto
df = pd.read_csv('FactAtendimentosUrgencia.csv', sep=';')

# Extrair Ano e Mes da coluna 'Período'
df['Ano'] = df['Período'].str[:4].astype(int)
df['Mes'] = df['Período'].str[5:7].astype(int)

# Ordenar por Ano e Mes para garantir a ordem correta
df = df.sort_values(['Ano', 'Mes'])

# Definir as colunas acumuladas conforme o seu arquivo
colunas_acumuladas = ['TotalAtendimentos', 'Atendimentos_Verde', 'Atendimentos_Azul', 'Atendimentos_Branca']

# Calcular os valores mensais reais a partir dos acumulados
for col in colunas_acumuladas:
    df[col + '_Mensal'] = df.groupby(['RegiaoID', 'InstituicaoID'])[col].diff().fillna(df[col])

# Salvar o resultado em um novo arquivo CSV
df.to_csv('FactAtendimentosUrgencia_Mensal.csv', sep=';', index=False)

print('Arquivo FactAtendimentosUrgencia_Mensal.csv gerado com valores mensais.')
