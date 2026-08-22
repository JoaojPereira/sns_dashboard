"""
Script para filtrar tabelas Fact apenas com período 2016-2025
Criado em: 08/12/2025
Objetivo: Remover dados de 2013-2015 das tabelas factuais
"""

import pandas as pd
from datetime import datetime
import os

print("=" * 80)
print("FILTRO DE PERÍODO - TABELAS FACT (2016-2025)")
print("=" * 80)
print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")

# ============================================================================
# FILTRAR FACTATENDIIMENTOURGENCIA
# ============================================================================

print("📊 A processar FactAtendimentosUrgencia...")

try:
    # Carregar dados
    fact_atend = pd.read_csv('FactAtendimentosUrgencia.csv', sep=';', encoding='utf-8-sig')
    
    print(f"  📥 Registos originais: {len(fact_atend)}")
    print(f"  📅 Período original: {fact_atend['Período'].min()} até {fact_atend['Período'].max()}")
    
    # Extrair ano do período
    fact_atend['Ano'] = fact_atend['Período'].str[:4].astype(int)
    
    # Filtrar apenas 2016-2025
    fact_atend_filtrado = fact_atend[fact_atend['Ano'] >= 2016].copy()
    
    # Remover coluna auxiliar
    fact_atend_filtrado = fact_atend_filtrado.drop(columns=['Ano'])
    
    # Criar backup do original
    if os.path.exists('FactAtendimentosUrgencia.csv'):
        backup_name = f"FactAtendimentosUrgencia.csv.backup_pre2016_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.rename('FactAtendimentosUrgencia.csv', backup_name)
        print(f"  ✓ Backup criado: {backup_name}")
    
    # Salvar dados filtrados
    fact_atend_filtrado.to_csv('FactAtendimentosUrgencia.csv', sep=';', index=False, encoding='utf-8-sig')
    
    print(f"  ✅ FactAtendimentosUrgencia filtrada")
    print(f"     • Registos após filtro: {len(fact_atend_filtrado)}")
    print(f"     • Período final: {fact_atend_filtrado['Período'].min()} até {fact_atend_filtrado['Período'].max()}")
    print(f"     • Registos removidos: {len(fact_atend) - len(fact_atend_filtrado)}")
    print(f"     • Total atendimentos: {fact_atend_filtrado['TotalAtendimentos'].sum():,.0f}")

except Exception as e:
    print(f"  ❌ ERRO ao processar FactAtendimentosUrgencia: {e}")

# ============================================================================
# FILTRAR FACTMONITORIZACAOSAZONAL
# ============================================================================

print("\n📊 A processar FactMonitorizacaosazonal...")

try:
    # Carregar dados
    fact_monit = pd.read_csv('FactMonitorizacaosazonal.csv', sep=';', encoding='utf-8-sig')
    
    print(f"  📥 Registos originais: {len(fact_monit)}")
    print(f"  📅 Período original: {fact_monit['Período'].min()} até {fact_monit['Período'].max()}")
    
    # Extrair ano do período (formato YYYY-MM-DD)
    fact_monit['Ano'] = pd.to_datetime(fact_monit['Período']).dt.year
    
    # Filtrar apenas 2016-2025
    fact_monit_filtrado = fact_monit[fact_monit['Ano'] >= 2016].copy()
    
    # Remover coluna auxiliar
    fact_monit_filtrado = fact_monit_filtrado.drop(columns=['Ano'])
    
    # Criar backup do original
    if os.path.exists('FactMonitorizacaosazonal.csv'):
        backup_name = f"FactMonitorizacaosazonal.csv.backup_pre2016_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.rename('FactMonitorizacaosazonal.csv', backup_name)
        print(f"  ✓ Backup criado: {backup_name}")
    
    # Salvar dados filtrados
    fact_monit_filtrado.to_csv('FactMonitorizacaosazonal.csv', sep=';', index=False, encoding='utf-8-sig')
    
    print(f"  ✅ FactMonitorizacaosazonal filtrada")
    print(f"     • Registos após filtro: {len(fact_monit_filtrado)}")
    print(f"     • Período final: {fact_monit_filtrado['Período'].min()} até {fact_monit_filtrado['Período'].max()}")
    print(f"     • Registos removidos: {len(fact_monit) - len(fact_monit_filtrado)}")

except Exception as e:
    print(f"  ❌ ERRO ao processar FactMonitorizacaosazonal: {e}")

# ============================================================================
# RESUMO FINAL
# ============================================================================

print("\n" + "=" * 80)
print("RESUMO DO FILTRO")
print("=" * 80)
print("✅ Período aplicado: 2016-2025")
print("✅ FactAtendimentosUrgencia: Filtrada")
print("✅ FactMonitorizacaosazonal: Filtrada")
print("\n" + "=" * 80)
print("✓ FILTRO CONCLUÍDO")
print("=" * 80)
print("\nOs backups dos ficheiros originais foram criados com sufixo '_pre2016'.")
print("As tabelas Fact agora contêm apenas dados de 2016-2025.")
print("Pode atualizar o Power BI clicando em 'Atualizar'.")
