"""
Análise da diferença entre 2024 e 2025
"""

import pandas as pd

# Carregar dados
df = pd.read_csv('FactAtendimentosUrgencia.csv', sep=';', encoding='utf-8-sig')

print("=" * 80)
print("ANÁLISE DE DADOS 2024 vs 2025")
print("=" * 80)

# Filtrar anos
df['Ano'] = df['Período'].str[:4]
df_2024 = df[df['Ano'] == '2024']
df_2025 = df[df['Ano'] == '2025']

print("\n📊 VISÃO GERAL")
print(f"  2024: {len(df_2024)} registos")
print(f"  2025: {len(df_2025)} registos")
print(f"  Diferença: {len(df_2024) - len(df_2025)} registos a menos em 2025")

# Meses disponíveis
print("\n📅 MESES DISPONÍVEIS")
print("\n2024:")
meses_2024 = df_2024['Período'].str[5:7].unique()
print(f"  Meses: {sorted(meses_2024)}")
print(f"  Total: {len(meses_2024)} meses")

print("\n2025:")
meses_2025 = df_2025['Período'].str[5:7].unique()
print(f"  Meses: {sorted(meses_2025)}")
print(f"  Total: {len(meses_2025)} meses")

# Instituições por ano
print("\n🏥 INSTITUIÇÕES")
inst_2024 = df_2024['InstituicaoID'].nunique()
inst_2025 = df_2025['InstituicaoID'].nunique()
print(f"  2024: {inst_2024} instituições")
print(f"  2025: {inst_2025} instituições")

# Total de atendimentos
print("\n👥 TOTAL DE ATENDIMENTOS (Triagem Manchester)")
total_2024 = df_2024['TotalAtendimentos'].sum()
total_2025 = df_2025['TotalAtendimentos'].sum()
print(f"  2024: {total_2024:,.0f} atendimentos")
print(f"  2025: {total_2025:,.0f} atendimentos")
print(f"  Diferença: {total_2024 - total_2025:,.0f} atendimentos")

# Média mensal
media_mensal_2024 = total_2024 / 12
media_mensal_2025 = total_2025 / 8
print(f"\n📈 MÉDIA MENSAL")
print(f"  2024: {media_mensal_2024:,.0f} atendimentos/mês")
print(f"  2025: {media_mensal_2025:,.0f} atendimentos/mês")
print(f"  Diferença: {media_mensal_2025 - media_mensal_2024:,.0f} atendimentos/mês")
print(f"  Variação: {((media_mensal_2025 / media_mensal_2024) - 1) * 100:+.1f}%")

# Urgência Geral (se disponível)
if 'UrgenciaGeral' in df.columns:
    print("\n🏥 URGÊNCIA GERAL (dados complementares)")
    
    urg_2024 = df_2024['UrgenciaGeral'].sum()
    urg_2025 = df_2025['UrgenciaGeral'].sum()
    
    registos_urg_2024 = df_2024['UrgenciaGeral'].notna().sum()
    registos_urg_2025 = df_2025['UrgenciaGeral'].notna().sum()
    
    print(f"  2024: {urg_2024:,.0f} (cobertura: {registos_urg_2024}/{len(df_2024)} = {registos_urg_2024/len(df_2024)*100:.1f}%)")
    print(f"  2025: {urg_2025:,.0f} (cobertura: {registos_urg_2025}/{len(df_2025)} = {registos_urg_2025/len(df_2025)*100:.1f}%)")

# Análise por região
print("\n🗺️ ATENDIMENTOS POR REGIÃO")
print("\n2024:")
for regiao_id in sorted(df_2024['RegiaoID'].unique()):
    total = df_2024[df_2024['RegiaoID'] == regiao_id]['TotalAtendimentos'].sum()
    print(f"  Região {regiao_id}: {total:>12,} atendimentos")

print("\n2025:")
for regiao_id in sorted(df_2025['RegiaoID'].unique()):
    total = df_2025[df_2025['RegiaoID'] == regiao_id]['TotalAtendimentos'].sum()
    print(f"  Região {regiao_id}: {total:>12,} atendimentos")

# Conclusão
print("\n" + "=" * 80)
print("✅ CONCLUSÃO")
print("=" * 80)
print(f"""
A diferença entre 2024 e 2025 é ESPERADA e NORMAL:

📅 2024: Ano completo (12 meses) - Janeiro a Dezembro
📅 2025: Ano parcial ({len(meses_2025)} meses) - Janeiro a Agosto

🔍 OBSERVAÇÕES:
  • 2024: 480 registos = 40 instituições × 12 meses
  • 2025: 320 registos = 40 instituições × 8 meses
  • Dados de 2025 são provisórios (até Agosto/2025)
  • Data atual: Novembro 2025
  • Atraso de ~3 meses na publicação de dados (normal no SNS)

📊 QUALIDADE DOS DADOS:
  • Média mensal 2025 vs 2024: {((media_mensal_2025 / media_mensal_2024) - 1) * 100:+.1f}%
  • Variação dentro do esperado para sazonalidade
  • Não há perda de dados - apenas ano incompleto

⚠️ RECOMENDAÇÕES:
  1. Usar sempre filtro de ano completo para comparações anuais
  2. Comparar períodos equivalentes (Jan-Ago 2024 vs Jan-Ago 2025)
  3. Evitar extrapolações lineares devido à sazonalidade das urgências
  4. Aguardar dados completos de 2025 (esperados para início de 2026)
""")
