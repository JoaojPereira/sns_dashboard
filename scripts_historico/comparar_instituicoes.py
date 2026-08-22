import pandas as pd

# Ler ambos os CSV
df_custos = pd.read_csv('custo-de-tratamento-mensal-por-doente.csv', 
                        sep=';', 
                        encoding='utf-8-sig')

df_atendimentos = pd.read_csv('atendimentos-em-urgencia-triagem-manchester.csv', 
                              sep=';', 
                              encoding='utf-8-sig')

print(f"Total de linhas em custos: {len(df_custos)}")
print(f"Total de linhas em atendimentos: {len(df_atendimentos)}")

# Obter instituições únicas de cada ficheiro
inst_custos = set(df_custos['Instituição Hospitalar'].unique())
inst_atendimentos = set(df_atendimentos['Instituição'].unique())

print(f"\n=== ANÁLISE DE INSTITUIÇÕES ===")
print(f"\nTotal de instituições únicas em custos: {len(inst_custos)}")
print(f"Total de instituições únicas em atendimentos: {len(inst_atendimentos)}")

# Instituições que existem em custos mas NÃO em atendimentos
apenas_custos = inst_custos - inst_atendimentos
print(f"\n=== Instituições APENAS em custos ({len(apenas_custos)}): ===")
for inst in sorted(apenas_custos):
    print(f"  - {inst}")

# Instituições que existem em atendimentos mas NÃO em custos
apenas_atendimentos = inst_atendimentos - inst_custos
print(f"\n=== Instituições APENAS em atendimentos ({len(apenas_atendimentos)}): ===")
for inst in sorted(apenas_atendimentos):
    print(f"  - {inst}")

# Instituições em COMUM (nomes iguais)
em_comum = inst_custos & inst_atendimentos
print(f"\n=== Instituições em COMUM ({len(em_comum)}): ===")
for inst in sorted(em_comum):
    print(f"  - {inst}")

# Verificar possíveis correspondências por similaridade
print(f"\n=== POSSÍVEIS CORRESPONDÊNCIAS (nomes parecidos): ===")
for inst_c in sorted(apenas_custos):
    for inst_a in sorted(apenas_atendimentos):
        # Verificar se há palavras-chave em comum
        palavras_c = set(inst_c.lower().split())
        palavras_a = set(inst_a.lower().split())
        comum = palavras_c & palavras_a
        # Se tiverem pelo menos 3 palavras em comum (excluindo palavras comuns)
        palavras_ignore = {'de', 'do', 'da', 'epe', 'ppe', 'e'}
        comum_relevante = comum - palavras_ignore
        if len(comum_relevante) >= 3:
            print(f"\n  CUSTOS:       {inst_c}")
            print(f"  ATENDIMENTOS: {inst_a}")
            print(f"  Palavras em comum: {comum_relevante}")
