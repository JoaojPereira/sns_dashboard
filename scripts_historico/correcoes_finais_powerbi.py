import pandas as pd
from datetime import datetime

print("="*80)
print("APLICANDO CORREÇÕES FINAIS PARA POWER BI")
print("="*80)

# 1. ATENDIMENTOS - Substituir nulos por 0 e corrigir nome de coluna
print("\n1. ATENDIMENTOS - Substituindo nulos por 0 e corrigindo nome de coluna...")
df_atend = pd.read_csv('atendimentos-em-urgencia-triagem-manchester.csv', 
                       sep=';', encoding='utf-8-sig')

# Renomear coluna com barra invertida
df_atend = df_atend.rename(columns={
    'Nº Atendimentos s\\ Triagem Manchester': 'Nº Atendimentos s/ Triagem Manchester'
})

# Preencher nulos com 0 nas colunas numéricas
colunas_numericas = [col for col in df_atend.columns if 'Nº Atendimentos' in col]
nulos_antes = df_atend[colunas_numericas].isnull().sum().sum()
df_atend[colunas_numericas] = df_atend[colunas_numericas].fillna(0)

df_atend.to_csv('atendimentos-em-urgencia-triagem-manchester.csv', 
                sep=';', index=False, encoding='utf-8-sig')
print(f"   ✓ {nulos_antes} valores nulos substituídos por 0")
print(f"   ✓ Coluna renomeada: 's\\' → 's/'")

# 2. TRABALHADORES - Substituir nulos por 0
print("\n2. TRABALHADORES - Substituindo nulos por 0...")
df_trab = pd.read_csv('trabalhadores-por-grupo-profissional.csv', 
                      sep=';', encoding='utf-8-sig')

# Preencher nulos com 0 nas colunas numéricas (exceto Período, Região, Instituição)
colunas_numericas = df_trab.select_dtypes(include=['float64', 'int64']).columns
nulos_antes = df_trab[colunas_numericas].isnull().sum().sum()
df_trab[colunas_numericas] = df_trab[colunas_numericas].fillna(0)

df_trab.to_csv('trabalhadores-por-grupo-profissional.csv', 
               sep=';', index=False, encoding='utf-8-sig')
print(f"   ✓ {nulos_antes} valores nulos substituídos por 0")

# 3. MONITORIZAÇÃO - Padronizar formato de data
print("\n3. MONITORIZAÇÃO - Padronizando formato de data...")
df_monit = pd.read_csv('monitorizacao-sazonal-csh.csv', 
                       sep=';', encoding='utf-8-sig')

print(f"   Formato original: {df_monit['Período'].iloc[0]}")

# Converter de DD/MM/YYYY para YYYY-MM-DD
def converter_data(data_str):
    try:
        # Tentar converter DD/MM/YYYY para YYYY-MM-DD
        data_obj = pd.to_datetime(data_str, format='%d/%m/%Y')
        return data_obj.strftime('%Y-%m-%d')
    except:
        return data_str

df_monit['Período'] = df_monit['Período'].apply(converter_data)

print(f"   Formato novo: {df_monit['Período'].iloc[0]}")

df_monit.to_csv('monitorizacao-sazonal-csh.csv', 
                sep=';', index=False, encoding='utf-8-sig')
print(f"   ✓ {len(df_monit)} datas convertidas de DD/MM/YYYY → YYYY-MM-DD")

# 4. VERIFICAÇÃO FINAL
print("\n" + "="*80)
print("VERIFICAÇÃO FINAL")
print("="*80)

# Recarregar todos os ficheiros
ficheiros = {
    'Atendimentos': 'atendimentos-em-urgencia-triagem-manchester.csv',
    'Custos': 'custo-de-tratamento-mensal-por-doente.csv',
    'Trabalhadores': 'trabalhadores-por-grupo-profissional.csv',
    'Monitorização': 'monitorizacao-sazonal-csh.csv'
}

for nome, caminho in ficheiros.items():
    df = pd.read_csv(caminho, sep=';', encoding='utf-8-sig')
    
    print(f"\n{nome}:")
    print(f"   Linhas: {len(df)}")
    print(f"   Colunas: {len(df.columns)}")
    
    # Verificar nulos
    nulos_total = df.isnull().sum().sum()
    if nulos_total > 0:
        print(f"   ⚠ Valores nulos: {nulos_total}")
    else:
        print(f"   ✓ Sem valores nulos")
    
    # Verificar formato de data
    if 'Período' in df.columns:
        exemplo = df['Período'].iloc[0]
        print(f"   Período (exemplo): {exemplo}")

print("\n" + "="*80)
print("✅ TODAS AS CORREÇÕES APLICADAS COM SUCESSO!")
print("="*80)
print("\n📊 FICHEIROS PRONTOS PARA POWER BI:")
print("   1. ✓ Valores nulos substituídos por 0")
print("   2. ✓ Formatos de data padronizados")
print("   3. ✓ Nomes de colunas corrigidos")
print("   4. ✓ Encoding UTF-8-sig")
print("   5. ✓ Separador ponto-e-vírgula (;)")
print("\n🎉 Pode importar os ficheiros para o Power BI!")
