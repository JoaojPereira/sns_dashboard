import pandas as pd

# Ler ficheiros
df_atend = pd.read_csv('atendimentos-em-urgencia-triagem-manchester.csv', sep=';', encoding='utf-8-sig')
df_trab = pd.read_csv('trabalhadores-por-grupo-profissional.csv', sep=';', encoding='utf-8-sig')

print("DIAGNÓSTICO DO PROBLEMA DE JOIN\n")
print("="*80)

# Verificar sample de dados de cada ficheiro
print("\n1. SAMPLE ATENDIMENTOS:")
print(df_atend[['Período', 'Região', 'Instituição']].head(3))

print("\n2. SAMPLE TRABALHADORES:")
print(df_trab[['Período', 'Região', 'Instituição']].head(3))

# Criar chave de join
df_atend['chave'] = df_atend['Período'] + '|' + df_atend['Região'] + '|' + df_atend['Instituição']
df_trab['chave'] = df_trab['Período'] + '|' + df_trab['Região'] + '|' + df_trab['Instituição']

print(f"\n3. ATENDIMENTOS: {df_atend['chave'].nunique()} chaves únicas")
print(f"   TRABALHADORES: {df_trab['chave'].nunique()} chaves únicas")

# Verificar quantos matches existem
chaves_atend = set(df_atend['chave'].unique())
chaves_trab = set(df_trab['chave'].unique())

matches = chaves_atend.intersection(chaves_trab)
print(f"\n4. MATCHES ENCONTRADOS: {len(matches)} chaves comuns")
print(f"   Taxa de match: {len(matches)/len(chaves_atend)*100:.1f}%")

# Verificar períodos diferentes
print("\n5. PERÍODOS:")
print(f"   Atendimentos: {sorted(df_atend['Período'].unique())[:5]} ... {sorted(df_atend['Período'].unique())[-3:]}")
print(f"   Trabalhadores: {sorted(df_trab['Período'].unique())[:5]} ... {sorted(df_trab['Período'].unique())[-3:]}")

# Sample de registros que não deram match
print("\n6. SAMPLE DE ATENDIMENTOS SEM MATCH em Trabalhadores:")
nao_match_atend = [k for k in chaves_atend if k not in chaves_trab]
for key in nao_match_atend[:5]:
    print(f"   {key}")

print("\n7. SAMPLE DE TRABALHADORES SEM MATCH em Atendimentos:")
nao_match_trab = [k for k in chaves_trab if k not in chaves_atend]
for key in nao_match_trab[:5]:
    print(f"   {key}")

# Verificar formato de Período
print("\n8. FORMATO DO PERÍODO:")
print(f"   Atendimentos - exemplo: '{df_atend['Período'].iloc[0]}' (tipo: {type(df_atend['Período'].iloc[0])})")
print(f"   Trabalhadores - exemplo: '{df_trab['Período'].iloc[0]}' (tipo: {type(df_trab['Período'].iloc[0])})")
