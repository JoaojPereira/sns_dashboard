import pandas as pd

print("=== COMPARAÇÃO DE INSTITUIÇÕES ENTRE TODOS OS FICHEIROS ===\n")

# Ler todos os ficheiros
ficheiros = {
    'Atendimentos': 'atendimentos-em-urgencia-triagem-manchester.csv',
    'Custos': 'custo-de-tratamento-mensal-por-doente.csv',
    'Trabalhadores': 'trabalhadores-por-grupo-profissional.csv'
}

# Dicionário para guardar as instituições de cada ficheiro
instituicoes_por_ficheiro = {}
colunas_instituicao = {
    'Atendimentos': 'Instituição',
    'Custos': 'Instituição Hospitalar',
    'Trabalhadores': 'Instituição'
}

# Ler e extrair instituições de cada ficheiro
for nome, caminho in ficheiros.items():
    df = pd.read_csv(caminho, sep=';', encoding='utf-8-sig')
    coluna = colunas_instituicao[nome]
    instituicoes = set(df[coluna].unique())
    instituicoes_por_ficheiro[nome] = instituicoes
    print(f"{nome} ({caminho}):")
    print(f"  Total de linhas: {len(df)}")
    print(f"  Coluna: '{coluna}'")
    print(f"  Instituições únicas: {len(instituicoes)}")
    print()

# Encontrar instituições comuns a todos os ficheiros
comum_todos = instituicoes_por_ficheiro['Atendimentos'] & instituicoes_por_ficheiro['Custos'] & instituicoes_por_ficheiro['Trabalhadores']
print(f"=== INSTITUIÇÕES COMUNS A TODOS OS 3 FICHEIROS ({len(comum_todos)}): ===")
for inst in sorted(comum_todos):
    print(f"  ✓ {inst}")

# Instituições APENAS em Atendimentos
apenas_atendimentos = instituicoes_por_ficheiro['Atendimentos'] - instituicoes_por_ficheiro['Custos'] - instituicoes_por_ficheiro['Trabalhadores']
print(f"\n=== APENAS em ATENDIMENTOS ({len(apenas_atendimentos)}): ===")
for inst in sorted(apenas_atendimentos):
    print(f"  • {inst}")

# Instituições APENAS em Custos
apenas_custos = instituicoes_por_ficheiro['Custos'] - instituicoes_por_ficheiro['Atendimentos'] - instituicoes_por_ficheiro['Trabalhadores']
print(f"\n=== APENAS em CUSTOS ({len(apenas_custos)}): ===")
for inst in sorted(apenas_custos):
    print(f"  • {inst}")

# Instituições APENAS em Trabalhadores
apenas_trabalhadores = instituicoes_por_ficheiro['Trabalhadores'] - instituicoes_por_ficheiro['Atendimentos'] - instituicoes_por_ficheiro['Custos']
print(f"\n=== APENAS em TRABALHADORES ({len(apenas_trabalhadores)}): ===")
for inst in sorted(apenas_trabalhadores):
    print(f"  • {inst}")

# Instituições em Atendimentos E Custos (mas não em Trabalhadores)
atend_custos = (instituicoes_por_ficheiro['Atendimentos'] & instituicoes_por_ficheiro['Custos']) - instituicoes_por_ficheiro['Trabalhadores']
print(f"\n=== em ATENDIMENTOS + CUSTOS (mas não em Trabalhadores) ({len(atend_custos)}): ===")
for inst in sorted(atend_custos):
    print(f"  • {inst}")

# Instituições em Atendimentos E Trabalhadores (mas não em Custos)
atend_trab = (instituicoes_por_ficheiro['Atendimentos'] & instituicoes_por_ficheiro['Trabalhadores']) - instituicoes_por_ficheiro['Custos']
print(f"\n=== em ATENDIMENTOS + TRABALHADORES (mas não em Custos) ({len(atend_trab)}): ===")
for inst in sorted(atend_trab):
    print(f"  • {inst}")

# Instituições em Custos E Trabalhadores (mas não em Atendimentos)
custos_trab = (instituicoes_por_ficheiro['Custos'] & instituicoes_por_ficheiro['Trabalhadores']) - instituicoes_por_ficheiro['Atendimentos']
print(f"\n=== em CUSTOS + TRABALHADORES (mas não em Atendimentos) ({len(custos_trab)}): ===")
for inst in sorted(custos_trab):
    print(f"  • {inst}")

# Resumo
print("\n" + "="*80)
print("RESUMO:")
print(f"  Total instituições únicas em Atendimentos: {len(instituicoes_por_ficheiro['Atendimentos'])}")
print(f"  Total instituições únicas em Custos: {len(instituicoes_por_ficheiro['Custos'])}")
print(f"  Total instituições únicas em Trabalhadores: {len(instituicoes_por_ficheiro['Trabalhadores'])}")
print(f"  Instituições comuns aos 3 ficheiros: {len(comum_todos)}")
print(f"  Instituições exclusivas de cada ficheiro: {len(apenas_atendimentos)} + {len(apenas_custos)} + {len(apenas_trabalhadores)}")
