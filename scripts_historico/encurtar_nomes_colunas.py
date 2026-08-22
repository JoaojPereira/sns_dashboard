import pandas as pd

# Ler o ficheiro
df = pd.read_csv('atendimentos-em-urgencia-triagem-manchester.csv', sep=';', encoding='utf-8-sig')

print("Nomes originais:")
print(df.columns.tolist())

# Renomear colunas para nomes mais curtos
novos_nomes = {
    'Nº Atendimentos em Urgência SU Triagem Manchester -Vermelha': 'Triagem Vermelha',
    'Nº Atendimentos em Urgência SU Triagem Manchester -Laranja': 'Triagem Laranja',
    'Nº Atendimentos em Urgência SU Triagem Manchester -Amarela': 'Triagem Amarela',
    'Nº Atendimentos em Urgência SU Triagem Manchester -Verde': 'Triagem Verde',
    'Nº Atendimentos em Urgência SU Triagem Manchester -Azul': 'Triagem Azul',
    'Nº Atendimentos em Urgência SU Triagem Manchester -Branca': 'Triagem Branca',
    'Nº Atendimentos s/ Triagem Manchester': 'Sem Triagem'
}

df = df.rename(columns=novos_nomes)

print("\n\nNovos nomes:")
print(df.columns.tolist())

# Guardar
df.to_csv('atendimentos-em-urgencia-triagem-manchester.csv', sep=';', index=False, encoding='utf-8-sig')

print("\n✅ Nomes de colunas encurtados!")
print(f"Total de linhas: {len(df)}")
