import pandas as pd

print("=== COMPARAÇÃO DE INSTITUIÇÕES ENTRE OS 4 FICHEIROS ===\n")

# Verificar se o ficheiro de monitorização tem coluna de instituição
df_monit = pd.read_csv('monitorizacao-sazonal-csh.csv', sep=';', encoding='utf-8-sig')
print("Colunas do ficheiro MONITORIZACAO:")
print(df_monit.columns.tolist())
print()

# Ler todos os ficheiros
ficheiros = {
    'Atendimentos': ('atendimentos-em-urgencia-triagem-manchester.csv', 'Instituição'),
    'Custos': ('custo-de-tratamento-mensal-por-doente.csv', 'Instituição Hospitalar'),
    'Trabalhadores': ('trabalhadores-por-grupo-profissional.csv', 'Instituição'),
    'Monitorização': ('monitorizacao-sazonal-csh.csv', None)  # verificar se existe
}

# Dicionário para guardar as instituições de cada ficheiro
instituicoes_por_ficheiro = {}

# Ler e extrair instituições de cada ficheiro
for nome, (caminho, coluna) in ficheiros.items():
    df = pd.read_csv(caminho, sep=';', encoding='utf-8-sig')
    
    print(f"{nome} ({caminho}):")
    print(f"  Total de linhas: {len(df)}")
    print(f"  Colunas: {df.columns.tolist()}")
    
    if coluna and coluna in df.columns:
        instituicoes = set(df[coluna].unique())
        instituicoes_por_ficheiro[nome] = instituicoes
        print(f"  Coluna instituição: '{coluna}'")
        print(f"  Instituições únicas: {len(instituicoes)}")
    else:
        print(f"  ⚠ Não tem coluna de instituição")
        instituicoes_por_ficheiro[nome] = set()
    print()

# Se Monitorização não tem instituições, comparar apenas os 3 ficheiros
ficheiros_com_inst = [nome for nome, inst in instituicoes_por_ficheiro.items() if len(inst) > 0]

print(f"Ficheiros com coluna de instituição: {', '.join(ficheiros_com_inst)}")
print()

if len(ficheiros_com_inst) == 3:
    print("="*80)
    print("ANÁLISE DOS 3 FICHEIROS COM INSTITUIÇÕES:")
    print("="*80)
    
    # Encontrar instituições comuns aos 3 ficheiros
    comum_todos = instituicoes_por_ficheiro['Atendimentos'] & instituicoes_por_ficheiro['Custos'] & instituicoes_por_ficheiro['Trabalhadores']
    print(f"\n=== INSTITUIÇÕES COMUNS AOS 3 FICHEIROS ({len(comum_todos)}): ===")
    for inst in sorted(comum_todos)[:10]:
        print(f"  ✓ {inst}")
    if len(comum_todos) > 10:
        print(f"  ... e mais {len(comum_todos) - 10} instituições")
    
    # Todas as instituições únicas (união)
    todas_inst = instituicoes_por_ficheiro['Atendimentos'] | instituicoes_por_ficheiro['Custos'] | instituicoes_por_ficheiro['Trabalhadores']
    print(f"\n=== TOTAL DE INSTITUIÇÕES ÚNICAS (união): {len(todas_inst)} ===")
    
    # Instituições que NÃO estão em todos os ficheiros
    nao_comuns = todas_inst - comum_todos
    print(f"\n=== INSTITUIÇÕES NÃO COMUNS A TODOS ({len(nao_comuns)}): ===")
    
    for inst in sorted(nao_comuns):
        presenca = []
        if inst in instituicoes_por_ficheiro['Atendimentos']:
            presenca.append('Atend')
        if inst in instituicoes_por_ficheiro['Custos']:
            presenca.append('Custos')
        if inst in instituicoes_por_ficheiro['Trabalhadores']:
            presenca.append('Trab')
        
        ausencia = []
        if inst not in instituicoes_por_ficheiro['Atendimentos']:
            ausencia.append('Atend')
        if inst not in instituicoes_por_ficheiro['Custos']:
            ausencia.append('Custos')
        if inst not in instituicoes_por_ficheiro['Trabalhadores']:
            ausencia.append('Trab')
        
        print(f"  • {inst}")
        print(f"    Presente: {', '.join(presenca)} | Ausente: {', '.join(ausencia)}")
    
    print("\n" + "="*80)
    print("RESUMO FINAL:")
    print(f"  Atendimentos: {len(instituicoes_por_ficheiro['Atendimentos'])} instituições")
    print(f"  Custos: {len(instituicoes_por_ficheiro['Custos'])} instituições")
    print(f"  Trabalhadores: {len(instituicoes_por_ficheiro['Trabalhadores'])} instituições")
    print(f"  Comuns aos 3: {len(comum_todos)} instituições")
    print(f"  Não comuns: {len(nao_comuns)} instituições")
    print(f"  Total único: {len(todas_inst)} instituições")
    
    # Percentagem de cobertura
    pct = (len(comum_todos) / len(todas_inst)) * 100
    print(f"\n  Cobertura: {pct:.1f}% das instituições estão nos 3 ficheiros")
