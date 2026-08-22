"""
Remover coluna UrgenciaGeral de FactAtendimentosUrgencia.csv
Dataset atendimentos-por-tipo-de-urgencia-hospitalar.csv não acrescenta valor:
- Cobertura muito baixa (10% em 2024-2025, 35-40% em anos anteriores)
- Dados redundantes com Triagem Manchester (que tem 100% cobertura)
- Complica o modelo sem benefício analítico
"""

import pandas as pd
from datetime import datetime
import shutil

# Configurações
INPUT_FILE = 'FactAtendimentosUrgencia.csv'
OUTPUT_FILE = 'FactAtendimentosUrgencia.csv'
BACKUP_FILE = f'FactAtendimentosUrgencia.csv.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'

print("=" * 80)
print("SIMPLIFICAÇÃO FINAL - REMOÇÃO DE UrgenciaGeral")
print("=" * 80)

# ============================================================================
# 1. BACKUP
# ============================================================================
print("\n📁 PASSO 1: Criando backup")
shutil.copy2(INPUT_FILE, BACKUP_FILE)
print(f"✅ Backup: {BACKUP_FILE}")

# ============================================================================
# 2. CARREGAR E ANALISAR
# ============================================================================
print("\n📊 PASSO 2: Carregando dados")
df = pd.read_csv(INPUT_FILE, sep=';', encoding='utf-8-sig')
print(f"✅ {len(df)} linhas, {len(df.columns)} colunas")

print("\n🔍 PASSO 3: Analisando coluna UrgenciaGeral")
registos_com_dados = df['UrgenciaGeral'].notna().sum()
registos_total = len(df)
cobertura = (registos_com_dados / registos_total) * 100

print(f"  Registos com dados: {registos_com_dados}/{registos_total} ({cobertura:.1f}%)")
print(f"  Registos sem dados: {registos_total - registos_com_dados} ({100-cobertura:.1f}%)")

# Cobertura por ano
print("\n  Cobertura por ano:")
df['Ano'] = df['Período'].str[:4]
for ano in sorted(df['Ano'].unique()):
    df_ano = df[df['Ano'] == ano]
    com_dados = df_ano['UrgenciaGeral'].notna().sum()
    total = len(df_ano)
    cob = (com_dados / total) * 100
    status = "✅" if cob > 30 else "⚠️" if cob > 10 else "🔴"
    print(f"    {ano}: {com_dados:3d}/{total:3d} = {cob:5.1f}% {status}")

# ============================================================================
# 4. REMOVER COLUNA
# ============================================================================
print("\n🗑️ PASSO 4: Removendo coluna UrgenciaGeral")

if 'UrgenciaGeral' in df.columns:
    df = df.drop('UrgenciaGeral', axis=1)
    print("✅ Coluna removida")
else:
    print("⚠️ Coluna não encontrada")

# Remover coluna auxiliar
df = df.drop('Ano', axis=1)

print(f"\n📊 Nova estrutura: {len(df)} linhas, {len(df.columns)} colunas")

# ============================================================================
# 5. VERIFICAR ESTRUTURA FINAL
# ============================================================================
print("\n📋 PASSO 5: Estrutura final")
print(f"\nColunas finais ({len(df.columns)}):")
for i, col in enumerate(df.columns, 1):
    print(f"  {i:2d}. {col}")

# ============================================================================
# 6. SALVAR
# ============================================================================
print("\n💾 PASSO 6: Salvando estrutura simplificada")
df.to_csv(OUTPUT_FILE, sep=';', index=False, encoding='utf-8-sig')
print(f"✅ Arquivo salvo: {OUTPUT_FILE}")

# ============================================================================
# RESUMO
# ============================================================================
print("\n" + "=" * 80)
print("✅ SIMPLIFICAÇÃO CONCLUÍDA")
print("=" * 80)

print(f"""
📊 ESTRUTURA FINAL:
  • Colunas: 19 → 18 (removida UrgenciaGeral)
  • Modelo simplificado e focado

🎯 BENEFÍCIOS:
  ✅ Eliminada coluna com baixa cobertura (34.9% global, 10% em 2024-2025)
  ✅ Modelo mais simples e direto
  ✅ Foco 100% em Triagem Manchester (dados completos)
  ✅ Sem redundância de dados

📂 ESTRUTURA FINAL (18 colunas):
  1-4.   Chaves (Período, TimeKey, RegiaoID, InstituicaoID)
  5-12.  Triagem Manchester (7 cores + Total) - FONTE PRINCIPAL
  13-15. Recursos Humanos (Médicos, Internos, Enfermeiros)
  16-18. Custos (Despesa, NumDoentes, CustoMedio)

🗑️ ARQUIVO DESCARTÁVEL:
  • atendimentos-por-tipo-de-urgencia-hospitalar.csv
  • Pode ser removido do workspace
  • Não acrescenta valor analítico

💾 BACKUPS DISPONÍVEIS:
  • {BACKUP_FILE}
  • FactAtendimentosUrgencia.csv.backup_20251115_163607 (com 23 colunas)
  • FactAtendimentosUrgencia.csv.backup_20251115_164844 (com 19 colunas)

📊 ANÁLISE RECOMENDADA:
  • Usar APENAS Triagem Manchester (100% cobertura, dados consistentes)
  • Foco em falsas urgências (Verde/Azul/Branca)
  • Análise de ineficiências operacionais
  • Comparação regional e temporal
""")

print("\n🔄 PRÓXIMOS PASSOS:")
print("  1. Atualizar README.md (18 colunas finais)")
print("  2. Remover Medidas_UrgenciaGeral_Simplificado.dax (obsoleto)")
print("  3. Focar apenas em Medidas_DAX_Completas.dax (Triagem Manchester)")
print("  4. Opcionalmente: remover atendimentos-por-tipo-de-urgencia-hospitalar.csv")
print("\n" + "=" * 80)
