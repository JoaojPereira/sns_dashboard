import pandas as pd

print("="*80)
print("NORMALIZANDO TODOS OS FICHEIROS PARA >= 2016-01")
print("="*80)

# Lista de ficheiros a processar
ficheiros = [
    'atendimentos-em-urgencia-triagem-manchester.csv',
    'trabalhadores-por-grupo-profissional.csv',
    'custo-de-tratamento-mensal-por-doente.csv',
    'monitorizacao-sazonal-csh.csv',
    'FactAtendimentosUrgencia.csv'
]

for ficheiro in ficheiros:
    print(f"\n📁 Processando: {ficheiro}")
    
    # Ler ficheiro
    df = pd.read_csv(ficheiro, sep=';', encoding='utf-8-sig')
    linhas_antes = len(df)
    
    # Extrair ano-mês (primeiros 7 caracteres)
    df['AnoMes'] = df['Período'].str[:7]
    
    # Filtrar >= 2016-01
    df_filtrado = df[df['AnoMes'] >= '2016-01'].copy()
    
    # Remover coluna auxiliar
    df_filtrado = df_filtrado.drop(columns=['AnoMes'])
    
    linhas_depois = len(df_filtrado)
    linhas_removidas = linhas_antes - linhas_depois
    percentagem_removida = (linhas_removidas / linhas_antes * 100) if linhas_antes > 0 else 0
    
    # Guardar
    df_filtrado.to_csv(ficheiro, sep=';', index=False, encoding='utf-8-sig')
    
    print(f"   ✅ Antes: {linhas_antes:,} linhas")
    print(f"   ✅ Depois: {linhas_depois:,} linhas")
    print(f"   🗑️  Removidas: {linhas_removidas:,} linhas ({percentagem_removida:.1f}%)")

print("\n" + "="*80)
print("✅ NORMALIZAÇÃO CONCLUÍDA!")
print("="*80)
print("\nTodos os ficheiros agora começam em 2016-01")

# Verificar períodos finais
print("\n" + "="*80)
print("VERIFICAÇÃO FINAL - PERÍODOS POR FICHEIRO")
print("="*80)

for ficheiro in ficheiros:
    df = pd.read_csv(ficheiro, sep=';', encoding='utf-8-sig')
    periodos = sorted(df['Período'].str[:7].unique())
    print(f"\n{ficheiro}:")
    print(f"  📅 De {periodos[0]} até {periodos[-1]}")
    print(f"  📊 {len(df):,} linhas, {len(periodos)} períodos")
