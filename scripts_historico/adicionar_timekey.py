import pandas as pd
from datetime import datetime

print("="*80)
print("ADICIONANDO TIMEKEY ÀS TABELAS FACTUAIS")
print("="*80)

# ===== FACT ATENDIMENTOS =====
print("\n1. Processando FactAtendimentosUrgencia...")
fact_atend = pd.read_csv('FactAtendimentosUrgencia.csv', sep=';', encoding='utf-8-sig')

print(f"   Linhas: {len(fact_atend)}")
print(f"   Período exemplo: {fact_atend['Período'].iloc[0]}")

# Converter Período (YYYY-MM) para TimeKey (YYYYMMDD)
# Assumir dia 1 de cada mês
def periodo_to_timekey(periodo):
    # periodo = "2016-01"
    ano, mes = periodo.split('-')
    dia = 1
    timekey = int(ano) * 10000 + int(mes) * 100 + dia
    return timekey

fact_atend['TimeKey'] = fact_atend['Período'].apply(periodo_to_timekey)

print(f"   ✓ TimeKey criado: {fact_atend['TimeKey'].iloc[0]} (de {fact_atend['Período'].iloc[0]})")

# Reorganizar colunas: TimeKey depois do Período
colunas_atend = ['Período', 'TimeKey', 'RegiaoID', 'InstituicaoID',
                 'Atendimentos_Vermelha', 'Atendimentos_Laranja', 'Atendimentos_Amarela',
                 'Atendimentos_Verde', 'Atendimentos_Azul', 'Atendimentos_Branca',
                 'Atendimentos_SemTriagem', 'TotalAtendimentos',
                 'Médicos', 'MedicosInternos', 'Enfermeiros',
                 'Despesa', 'NumDoentes', 'CustoMedio']

fact_atend = fact_atend[colunas_atend]
fact_atend['TimeKey'] = fact_atend['TimeKey'].astype(int)

print(f"   ✓ Colunas: {len(fact_atend.columns)}")
print(f"   ✓ TimeKeys únicos: {fact_atend['TimeKey'].nunique()}")

# Guardar
fact_atend.to_csv('FactAtendimentosUrgencia.csv', sep=';', index=False, encoding='utf-8-sig')
print(f"   ✅ FactAtendimentosUrgencia.csv atualizado")

# ===== FACT MONITORIZAÇÃO =====
print("\n2. Processando monitorizacao-sazonal-csh...")
fact_mon = pd.read_csv('monitorizacao-sazonal-csh.csv', sep=';', encoding='utf-8-sig')

print(f"   Linhas: {len(fact_mon)}")
print(f"   Período exemplo: {fact_mon['Período'].iloc[0]}")

# Converter Período (YYYY-MM-DD) para TimeKey (YYYYMMDD)
def data_to_timekey(data_str):
    # data_str = "2016-11-01"
    ano, mes, dia = data_str.split('-')
    timekey = int(ano) * 10000 + int(mes) * 100 + int(dia)
    return timekey

fact_mon['TimeKey'] = fact_mon['Período'].apply(data_to_timekey)

print(f"   ✓ TimeKey criado: {fact_mon['TimeKey'].iloc[0]} (de {fact_mon['Período'].iloc[0]})")

# Reorganizar colunas: TimeKey depois do Período
colunas_mon = ['Período', 'TimeKey', 'RegiaoID', 'IndicadorID', 'Valor']

fact_mon = fact_mon[colunas_mon]
fact_mon['TimeKey'] = fact_mon['TimeKey'].astype(int)

print(f"   ✓ Colunas: {len(fact_mon.columns)}")
print(f"   ✓ TimeKeys únicos: {fact_mon['TimeKey'].nunique()}")

# Guardar
fact_mon.to_csv('monitorizacao-sazonal-csh.csv', sep=';', index=False, encoding='utf-8-sig')
print(f"   ✅ monitorizacao-sazonal-csh.csv atualizado")

# ===== VERIFICAÇÃO FINAL =====
print("\n" + "="*80)
print("VERIFICAÇÃO FINAL")
print("="*80)

print("\n3. FactAtendimentosUrgencia:")
print(f"   Colunas: {list(fact_atend.columns)}")
print(f"   Sample TimeKeys: {sorted(fact_atend['TimeKey'].unique())[:5]}")
print("\n   Primeiras 3 linhas:")
print(fact_atend[['Período', 'TimeKey', 'RegiaoID', 'InstituicaoID']].head(3).to_string())

print("\n4. monitorizacao-sazonal-csh:")
print(f"   Colunas: {list(fact_mon.columns)}")
print(f"   Sample TimeKeys: {sorted(fact_mon['TimeKey'].unique())[:5]}")
print("\n   Primeiras 3 linhas:")
print(fact_mon.head(3).to_string())

print("\n" + "="*80)
print("✅ TIMEKEY ADICIONADO COM SUCESSO!")
print("="*80)
print("\nRelacionamentos no Power BI:")
print("  DimCalendar[TimeKey] → FactAtendimentosUrgencia[TimeKey]")
print("  DimCalendar[TimeKey] → monitorizacao[TimeKey]")
print("\nCardinalidade: 1:N (One to Many)")
print("Direção: DimCalendar → Factuais")
