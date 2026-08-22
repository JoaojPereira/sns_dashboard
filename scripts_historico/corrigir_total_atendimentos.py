"""
Corrigir coluna TotalAtendimentos em FactAtendimentosUrgencia.csv
A coluna estava a 0 - deve ser a soma das 7 cores de triagem
"""

import pandas as pd
from datetime import datetime

# Configurações
INPUT_FILE = 'FactAtendimentosUrgencia.csv'
OUTPUT_FILE = 'FactAtendimentosUrgencia.csv'
BACKUP_FILE = f'FactAtendimentosUrgencia.csv.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'

print("=" * 80)
print("CORREÇÃO DE TOTALATENDIMENTOS")
print("=" * 80)

# ============================================================================
# 1. BACKUP
# ============================================================================
print("\n📁 PASSO 1: Criando backup")
import shutil
shutil.copy2(INPUT_FILE, BACKUP_FILE)
print(f"✅ Backup: {BACKUP_FILE}")

# ============================================================================
# 2. CARREGAR DADOS
# ============================================================================
print("\n📊 PASSO 2: Carregando dados")
df = pd.read_csv(INPUT_FILE, sep=';', encoding='utf-8-sig')
print(f"✅ {len(df)} linhas carregadas")

# ============================================================================
# 3. VERIFICAR PROBLEMA
# ============================================================================
print("\n🔍 PASSO 3: Verificando TotalAtendimentos atual")
total_atual = df['TotalAtendimentos'].sum()
print(f"  Soma de TotalAtendimentos: {total_atual:,.0f}")

if total_atual == 0:
    print("  ⚠️ PROBLEMA CONFIRMADO: TotalAtendimentos está a 0")
else:
    print(f"  ✅ TotalAtendimentos já tem dados")

# ============================================================================
# 4. CALCULAR NOVO TOTAL
# ============================================================================
print("\n🧮 PASSO 4: Calculando TotalAtendimentos correto")

colunas_triagem = [
    'Atendimentos_Vermelha',
    'Atendimentos_Laranja', 
    'Atendimentos_Amarela',
    'Atendimentos_Verde',
    'Atendimentos_Azul',
    'Atendimentos_Branca',
    'Atendimentos_SemTriagem'
]

# Calcular soma
df['TotalAtendimentos'] = df[colunas_triagem].sum(axis=1)

novo_total = df['TotalAtendimentos'].sum()
print(f"✅ Novo total calculado: {novo_total:,.0f}")

# ============================================================================
# 5. ANÁLISE POR ANO
# ============================================================================
print("\n📅 PASSO 5: Análise por ano")

df['Ano'] = df['Período'].str[:4]

print("\nTotal de atendimentos por ano:")
for ano in sorted(df['Ano'].unique()):
    df_ano = df[df['Ano'] == ano]
    total = df_ano['TotalAtendimentos'].sum()
    registos = len(df_ano)
    media_mensal = total / len(df_ano['Período'].str[:7].unique())
    print(f"  {ano}: {total:>15,} atendimentos ({registos:3d} registos, média {media_mensal:>10,.0f}/mês)")

# Análise de variação
print("\n📉 Variação anual:")
anos = sorted(df['Ano'].unique())
for i in range(1, len(anos)):
    ano_anterior = anos[i-1]
    ano_atual = anos[i]
    
    total_anterior = df[df['Ano'] == ano_anterior]['TotalAtendimentos'].sum()
    total_atual = df[df['Ano'] == ano_atual]['TotalAtendimentos'].sum()
    
    # Ajustar para 2025 (apenas 8 meses)
    if ano_atual == '2025':
        meses_2025 = len(df[df['Ano'] == '2025']['Período'].str[:7].unique())
        total_atual_projetado = total_atual * (12 / meses_2025)
        variacao = ((total_atual_projetado / total_anterior) - 1) * 100
        diferenca = total_atual_projetado - total_anterior
        print(f"  {ano_anterior} → {ano_atual}: {variacao:+.1f}% ({diferenca:+,.0f}) [PROJETADO para 12 meses]")
    else:
        variacao = ((total_atual / total_anterior) - 1) * 100
        diferenca = total_atual - total_anterior
        
        if abs(variacao) > 10:
            alerta = " ⚠️ VARIAÇÃO SIGNIFICATIVA"
        else:
            alerta = ""
        
        print(f"  {ano_anterior} → {ano_atual}: {variacao:+.1f}% ({diferenca:+,.0f}){alerta}")

# ============================================================================
# 6. VERIFICAR DADOS 2024-2025
# ============================================================================
print("\n🔍 PASSO 6: Investigação 2024-2025")

# Verificar instituições
inst_2022 = df[df['Ano'] == '2022']['InstituicaoID'].nunique()
inst_2023 = df[df['Ano'] == '2023']['InstituicaoID'].nunique()
inst_2024 = df[df['Ano'] == '2024']['InstituicaoID'].nunique()
inst_2025 = df[df['Ano'] == '2025']['InstituicaoID'].nunique()

print(f"\nNúmero de instituições:")
print(f"  2022: {inst_2022} instituições")
print(f"  2023: {inst_2023} instituições")
print(f"  2024: {inst_2024} instituições")
print(f"  2025: {inst_2025} instituições")

# Verificar se há instituições com dados zero em 2024
print("\n🔍 Verificando qualidade dos dados 2024:")
df_2024 = df[df['Ano'] == '2024']
inst_sem_dados = df_2024[df_2024['TotalAtendimentos'] == 0]['InstituicaoID'].nunique()
print(f"  Instituições com 0 atendimentos: {inst_sem_dados}")

# Comparar média por instituição
media_2022 = df[df['Ano'] == '2022']['TotalAtendimentos'].sum() / inst_2022 / 12
media_2023 = df[df['Ano'] == '2023']['TotalAtendimentos'].sum() / inst_2023 / 12
media_2024 = df[df['Ano'] == '2024']['TotalAtendimentos'].sum() / inst_2024 / 12
media_2025 = df[df['Ano'] == '2025']['TotalAtendimentos'].sum() / inst_2025 / 8

print(f"\nMédia mensal por instituição:")
print(f"  2022: {media_2022:>8,.0f} atendimentos/inst/mês")
print(f"  2023: {media_2023:>8,.0f} atendimentos/inst/mês")
print(f"  2024: {media_2024:>8,.0f} atendimentos/inst/mês ⚠️ Queda de {((media_2024/media_2023)-1)*100:.1f}%")
print(f"  2025: {media_2025:>8,.0f} atendimentos/inst/mês")

# ============================================================================
# 7. SALVAR DADOS CORRIGIDOS
# ============================================================================
print("\n💾 PASSO 7: Salvando dados corrigidos")

df = df.drop('Ano', axis=1)  # Remover coluna auxiliar
df.to_csv(OUTPUT_FILE, sep=';', index=False, encoding='utf-8-sig')
print(f"✅ Arquivo salvo: {OUTPUT_FILE}")

# ============================================================================
# RESUMO
# ============================================================================
print("\n" + "=" * 80)
print("✅ CORREÇÃO CONCLUÍDA")
print("=" * 80)

print(f"""
📊 RESUMO:
  • TotalAtendimentos corrigido (era 0, agora soma das 7 cores)
  • Total global: {novo_total:,.0f} atendimentos (2016-2025)
  • Backup criado: {BACKUP_FILE}

⚠️ ALERTA IDENTIFICADO:
  • 2024 apresenta QUEDA DRÁSTICA de atendimentos vs 2023
  • Possíveis causas:
    1. Dados incompletos ou não publicados pelo SNS
    2. Mudança de metodologia de reporte
    3. Fusão de instituições (reforma ULS 2023-2024)
    4. Filtros aplicados aos dados originais

🔍 PRÓXIMOS PASSOS:
  1. Verificar fonte original no Portal Transparência SNS
  2. Confirmar se 2024 tem todos os meses de todas as instituições
  3. Investigar mudanças no processo de reporte do SNS
  4. Considerar usar apenas 2016-2023 para análises históricas
""")
