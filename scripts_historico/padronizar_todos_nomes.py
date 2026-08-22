import pandas as pd

print("=== PADRONIZANDO NOMES DE INSTITUIÇÕES EM TODOS OS FICHEIROS ===\n")

# 1. ATENDIMENTOS - Remover vírgula do Hospital de Vila Franca de Xira
print("1. Corrigindo ATENDIMENTOS...")
df_atend = pd.read_csv('atendimentos-em-urgencia-triagem-manchester.csv', 
                       sep=';', encoding='utf-8-sig')

mapeamento_atend = {
    'Hospital de Vila Franca de Xira, EPE': 'Hospital de Vila Franca de Xira EPE'
}

for antigo, novo in mapeamento_atend.items():
    count = (df_atend['Instituição'] == antigo).sum()
    if count > 0:
        print(f"   {antigo} → {novo} ({count} ocorrências)")
        df_atend['Instituição'] = df_atend['Instituição'].replace(antigo, novo)

df_atend.to_csv('atendimentos-em-urgencia-triagem-manchester.csv', 
                sep=';', index=False, encoding='utf-8-sig')
print("   ✓ Arquivo atualizado\n")

# 2. TRABALHADORES - Padronizar nomes
print("2. Corrigindo TRABALHADORES...")
df_trab = pd.read_csv('trabalhadores-por-grupo-profissional.csv', 
                      sep=';', encoding='utf-8-sig')

mapeamento_trab = {
    # Adicionar "de" na Unidade Local de Saúde Castelo Branco
    'Unidade Local de Saúde Castelo Branco EPE': 'Unidade Local de Saúde de Castelo Branco EPE',
    
    # Corrigir Gaia/Espinho para incluir "Vila Nova de"
    'Unidade Local de Saúde de Gaia/Espinho EPE': 'Unidade Local de Saúde de Vila Nova de Gaia/Espinho EPE',
    
    # Padronizar IPO (formato mais recente sem hífen)
    'Instituto Português Oncologia Francisco Gentil - Coimbra EPE': 'Instituto Português de Oncologia de Coimbra Francisco Gentil EPE',
    'Instituto Português Oncologia Francisco Gentil - Lisboa EPE': 'Instituto Português de Oncologia de Lisboa Francisco Gentil EPE',
    'Instituto Português Oncologia Francisco Gentil - Porto EPE': 'Instituto Português de Oncologia do Porto Francisco Gentil EPE'
}

for antigo, novo in mapeamento_trab.items():
    count = (df_trab['Instituição'] == antigo).sum()
    if count > 0:
        print(f"   {antigo}")
        print(f"   → {novo} ({count} ocorrências)")
        df_trab['Instituição'] = df_trab['Instituição'].replace(antigo, novo)

df_trab.to_csv('trabalhadores-por-grupo-profissional.csv', 
               sep=';', index=False, encoding='utf-8-sig')
print("   ✓ Arquivo atualizado\n")

print("="*80)
print("VERIFICAÇÃO FINAL:")
print("="*80)

# Recarregar e verificar
df_atend = pd.read_csv('atendimentos-em-urgencia-triagem-manchester.csv', sep=';', encoding='utf-8-sig')
df_custos = pd.read_csv('custo-de-tratamento-mensal-por-doente.csv', sep=';', encoding='utf-8-sig')
df_trab = pd.read_csv('trabalhadores-por-grupo-profissional.csv', sep=';', encoding='utf-8-sig')

inst_atend = set(df_atend['Instituição'].unique())
inst_custos = set(df_custos['Instituição Hospitalar'].unique())
inst_trab = set(df_trab['Instituição'].unique())

# Instituições comuns
comum_todos = inst_atend & inst_custos & inst_trab
print(f"\nInstituições comuns aos 3 ficheiros: {len(comum_todos)}")

# Verificar se os problemas foram resolvidos
problemas = [
    'Hospital de Vila Franca de Xira EPE',
    'Unidade Local de Saúde de Vila Nova de Gaia/Espinho EPE',
    'Unidade Local de Saúde de Castelo Branco EPE'
]

print("\nVerificação de nomes corrigidos:")
for inst in problemas:
    em_atend = inst in inst_atend
    em_custos = inst in inst_custos
    em_trab = inst in inst_trab
    status = []
    if em_atend: status.append("Atendimentos")
    if em_custos: status.append("Custos")
    if em_trab: status.append("Trabalhadores")
    
    print(f"  {'✓' if len(status) >= 2 else '•'} {inst}")
    print(f"    Presente em: {', '.join(status) if status else 'NENHUM'}")

print("\n✓ Padronização concluída!")
