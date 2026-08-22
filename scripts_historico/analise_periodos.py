import pandas as pd

print("="*80)
print("ANÁLISE DE PERÍODOS DISPONÍVEIS EM TODOS OS FICHEIROS")
print("="*80)

# Ler todos os ficheiros
ficheiros = {
    'Atendimentos': 'atendimentos-em-urgencia-triagem-manchester.csv',
    'Trabalhadores': 'trabalhadores-por-grupo-profissional.csv',
    'Custos': 'custo-de-tratamento-mensal-por-doente.csv',
    'Monitorização': 'monitorizacao-sazonal-csh.csv'
}

analise = {}

for nome, ficheiro in ficheiros.items():
    df = pd.read_csv(ficheiro, sep=';', encoding='utf-8-sig')
    
    # Extrair período (pode ser YYYY-MM ou YYYY-MM-DD)
    periodos = df['Período'].unique()
    
    # Extrair apenas ano-mês
    if '-' in str(periodos[0]):
        anos_meses = sorted([p[:7] for p in periodos])  # YYYY-MM
    else:
        anos_meses = sorted(periodos)
    
    anos_meses = sorted(set(anos_meses))
    
    analise[nome] = {
        'total_linhas': len(df),
        'primeiro_periodo': anos_meses[0],
        'ultimo_periodo': anos_meses[-1],
        'total_periodos': len(anos_meses),
        'periodos': anos_meses
    }
    
    print(f"\n{nome}:")
    print(f"  📊 Total de linhas: {len(df):,}")
    print(f"  📅 Primeiro período: {anos_meses[0]}")
    print(f"  📅 Último período: {anos_meses[-1]}")
    print(f"  📅 Total de períodos: {len(anos_meses)}")

# Encontrar período comum
print("\n" + "="*80)
print("ANÁLISE DE SOBREPOSIÇÃO")
print("="*80)

# Converter para sets
sets_periodos = {nome: set(info['periodos']) for nome, info in analise.items()}

# Interseção de todos
periodos_comuns = sets_periodos['Atendimentos'].intersection(
    sets_periodos['Trabalhadores'],
    sets_periodos['Custos'],
    sets_periodos['Monitorização']
)

print(f"\n✅ Períodos COMUNS a todos os ficheiros: {len(periodos_comuns)}")
if periodos_comuns:
    periodos_comuns_ordenados = sorted(periodos_comuns)
    print(f"   Do {periodos_comuns_ordenados[0]} até {periodos_comuns_ordenados[-1]}")

# Verificar desde 2016
periodos_desde_2016 = {nome: [p for p in info['periodos'] if p >= '2016-01'] 
                       for nome, info in analise.items()}

print(f"\n📅 DESDE 2016-01:")
for nome, periodos in periodos_desde_2016.items():
    if periodos:
        print(f"   {nome}: {periodos[0]} até {periodos[-1]} ({len(periodos)} períodos)")

# Interseção desde 2016
sets_2016 = {nome: set(p) for nome, p in periodos_desde_2016.items()}
comuns_2016 = sets_2016['Atendimentos'].intersection(
    sets_2016['Trabalhadores'],
    sets_2016['Custos'],
    sets_2016['Monitorização']
)

print(f"\n✅ Períodos COMUNS desde 2016: {len(comuns_2016)}")
if comuns_2016:
    comuns_2016_ordenados = sorted(comuns_2016)
    print(f"   Do {comuns_2016_ordenados[0]} até {comuns_2016_ordenados[-1]}")

# Contar registros que seriam mantidos desde 2016
print("\n" + "="*80)
print("IMPACTO DE FILTRAR DESDE 2016-01")
print("="*80)

for nome, ficheiro in ficheiros.items():
    df = pd.read_csv(ficheiro, sep=';', encoding='utf-8-sig')
    
    # Extrair ano-mês para comparação
    df['AnoMes'] = df['Período'].str[:7]
    
    antes_2016 = len(df[df['AnoMes'] < '2016-01'])
    desde_2016 = len(df[df['AnoMes'] >= '2016-01'])
    percentagem_perda = (antes_2016 / len(df) * 100) if len(df) > 0 else 0
    
    print(f"\n{nome}:")
    print(f"  📉 Antes de 2016: {antes_2016:,} linhas ({percentagem_perda:.1f}%)")
    print(f"  ✅ Desde 2016: {desde_2016:,} linhas ({100-percentagem_perda:.1f}%)")

print("\n" + "="*80)
print("RECOMENDAÇÃO: Filtrar todos os ficheiros para >= 2016-01")
print("="*80)
