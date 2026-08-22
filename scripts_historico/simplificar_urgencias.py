"""
Script para simplificar FactAtendimentosUrgencia.csv
Remove colunas: UrgenciaPediatrica, UrgenciaObstetricia, UrgenciaPsiquiatrica, TotalUrgencias
Mantém apenas: UrgenciaGeral
"""

import pandas as pd
from datetime import datetime

# Configurações
INPUT_FILE = 'FactAtendimentosUrgencia.csv'
OUTPUT_FILE = 'FactAtendimentosUrgencia.csv'
BACKUP_FILE = f'FactAtendimentosUrgencia.csv.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'

print("=" * 80)
print("SIMPLIFICAÇÃO DE FACTATENIMENTOSURGENCIA")
print("=" * 80)
print(f"\nArquivo de entrada: {INPUT_FILE}")
print(f"Backup será criado: {BACKUP_FILE}")

# ============================================================================
# 1. BACKUP DO ARQUIVO ORIGINAL
# ============================================================================
print("\n" + "=" * 80)
print("PASSO 1: Criando backup do arquivo original")
print("=" * 80)

import shutil
shutil.copy2(INPUT_FILE, BACKUP_FILE)
print(f"✅ Backup criado: {BACKUP_FILE}")

# ============================================================================
# 2. CARREGAR DADOS
# ============================================================================
print("\n" + "=" * 80)
print("PASSO 2: Carregando dados")
print("=" * 80)

df = pd.read_csv(INPUT_FILE, sep=';', encoding='utf-8-sig')
print(f"✅ Arquivo carregado: {len(df)} linhas, {len(df.columns)} colunas")
print(f"\nColunas atuais: {list(df.columns)}")

# ============================================================================
# 3. ANÁLISE DAS COLUNAS A REMOVER
# ============================================================================
print("\n" + "=" * 80)
print("PASSO 3: Analisando colunas a remover")
print("=" * 80)

colunas_remover = ['UrgenciaPediatrica', 'UrgenciaObstetricia', 'UrgenciaPsiquiatrica', 'TotalUrgencias']

for col in colunas_remover:
    if col in df.columns:
        total_valores = df[col].notna().sum()
        total_nao_vazios = (df[col].notna() & (df[col] != '') & (df[col] != 0)).sum()
        print(f"  {col}:")
        print(f"    - Valores preenchidos: {total_valores}")
        print(f"    - Valores não-zero: {total_nao_vazios}")
    else:
        print(f"  ⚠️ {col} não encontrada no arquivo")

# ============================================================================
# 4. ANÁLISE DA COLUNA A MANTER
# ============================================================================
print("\n" + "=" * 80)
print("PASSO 4: Analisando coluna a manter (UrgenciaGeral)")
print("=" * 80)

if 'UrgenciaGeral' in df.columns:
    total_valores = df['UrgenciaGeral'].notna().sum()
    total_nao_vazios = (df['UrgenciaGeral'].notna() & (df['UrgenciaGeral'] != '') & (df['UrgenciaGeral'] != 0)).sum()
    print(f"  UrgenciaGeral:")
    print(f"    - Valores preenchidos: {total_valores}")
    print(f"    - Valores não-zero: {total_nao_vazios}")
    print(f"    - % cobertura: {(total_nao_vazios / len(df) * 100):.1f}%")
else:
    print("  ⚠️ UrgenciaGeral não encontrada no arquivo")

# ============================================================================
# 5. REMOVER COLUNAS
# ============================================================================
print("\n" + "=" * 80)
print("PASSO 5: Removendo colunas desnecessárias")
print("=" * 80)

colunas_existentes_remover = [col for col in colunas_remover if col in df.columns]

if colunas_existentes_remover:
    df_simplificado = df.drop(columns=colunas_existentes_remover)
    print(f"✅ Removidas {len(colunas_existentes_remover)} colunas: {colunas_existentes_remover}")
    print(f"\nNova estrutura: {len(df_simplificado)} linhas, {len(df_simplificado.columns)} colunas")
else:
    df_simplificado = df.copy()
    print("⚠️ Nenhuma coluna para remover encontrada")

# ============================================================================
# 6. VERIFICAR RESULTADO
# ============================================================================
print("\n" + "=" * 80)
print("PASSO 6: Verificando resultado")
print("=" * 80)

print(f"\nColunas finais ({len(df_simplificado.columns)}):")
for i, col in enumerate(df_simplificado.columns, 1):
    print(f"  {i:2d}. {col}")

# ============================================================================
# 7. SALVAR ARQUIVO SIMPLIFICADO
# ============================================================================
print("\n" + "=" * 80)
print("PASSO 7: Salvando arquivo simplificado")
print("=" * 80)

df_simplificado.to_csv(OUTPUT_FILE, sep=';', index=False, encoding='utf-8-sig')
print(f"✅ Arquivo salvo: {OUTPUT_FILE}")
print(f"   - {len(df_simplificado)} linhas")
print(f"   - {len(df_simplificado.columns)} colunas")

# ============================================================================
# RESUMO FINAL
# ============================================================================
print("\n" + "=" * 80)
print("✅ SIMPLIFICAÇÃO CONCLUÍDA COM SUCESSO!")
print("=" * 80)

print("\n📊 RESUMO DAS ALTERAÇÕES:")
print(f"  • Colunas originais: {len(df.columns)}")
print(f"  • Colunas removidas: {len(colunas_existentes_remover)}")
print(f"  • Colunas finais: {len(df_simplificado.columns)}")
print(f"\n  • Estrutura final: 23 → 19 colunas")
print(f"  • Mantido: UrgenciaGeral (dados complementares de especialização)")
print(f"  • Removido: UrgenciaPediatrica, UrgenciaObstetricia, UrgenciaPsiquiatrica, TotalUrgencias")

print(f"\n💾 BACKUP DISPONÍVEL:")
print(f"  {BACKUP_FILE}")

print(f"\n📁 PRÓXIMOS PASSOS:")
print(f"  1. Revisar Medidas_TipoUrgencia.dax (remover medidas pediátricas/obstétricas)")
print(f"  2. Atualizar README.md (19 colunas, apenas UrgenciaGeral)")
print(f"  3. Importar FactAtendimentosUrgencia.csv atualizado no Power BI")

print("\n" + "=" * 80)
