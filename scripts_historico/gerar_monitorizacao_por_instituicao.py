# Script para gerar FactMonitorizacaosazonal.csv por instituição
# Requer pandas instalado

import pandas as pd

# Carregar dados factuais
fact = pd.read_csv(r"d:/Ambiente de trabalho/TransformacaoBi/Report de Ineficiências nas Urgências Hospitalares/FactAtendimentosUrgencia.csv", sep=';')

# Exemplo de indicadores: Total Atendimentos, Tempo Médio (se existir), etc.
# Adapte conforme os indicadores que deseja calcular

# Agrupar por Período, TimeKey, RegiaoID, InstituicaoID
result = fact.groupby(['Período', 'TimeKey', 'RegiaoID', 'InstituicaoID']).agg({
    'TotalAtendimentos': 'sum',
    # Adicione outros indicadores aqui
}).reset_index()

# Gerar formato para FactMonitorizacaosazonal.csv
rows = []
for _, row in result.iterrows():
    # IndicadorID 1 = Total Atendimentos (exemplo)
    rows.append({
        'Período': row['Período'],
        'TimeKey': row['TimeKey'],
        'RegiaoID': row['RegiaoID'],
        'InstituicaoID': row['InstituicaoID'],
        'IndicadorID': 1,
        'Valor': row['TotalAtendimentos']
    })
    # Adicione outros indicadores conforme necessário

# Converter para DataFrame e exportar
out = pd.DataFrame(rows)
out.to_csv(r"d:/Ambiente de trabalho/TransformacaoBi/Report de Ineficiências nas Urgências Hospitalares/FactMonitorizacaosazonal_por_instituicao.csv", sep=';', index=False)

print("Ficheiro gerado: FactMonitorizacaosazonal_por_instituicao.csv")
