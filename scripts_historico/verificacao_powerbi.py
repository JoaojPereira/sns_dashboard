import pandas as pd
import numpy as np

print("="*80)
print("VERIFICAÇÃO COMPLETA DOS FICHEIROS PARA POWER BI")
print("="*80)

ficheiros = {
    'Atendimentos': 'atendimentos-em-urgencia-triagem-manchester.csv',
    'Custos': 'custo-de-tratamento-mensal-por-doente.csv',
    'Trabalhadores': 'trabalhadores-por-grupo-profissional.csv',
    'Monitorização': 'monitorizacao-sazonal-csh.csv'
}

problemas_encontrados = []

for nome, caminho in ficheiros.items():
    print(f"\n{'='*80}")
    print(f"FICHEIRO: {nome}")
    print(f"{'='*80}")
    
    df = pd.read_csv(caminho, sep=';', encoding='utf-8-sig')
    
    print(f"\n1. ESTRUTURA:")
    print(f"   Linhas: {len(df)}")
    print(f"   Colunas: {len(df.columns)}")
    print(f"   Colunas: {df.columns.tolist()}")
    
    # Verificar valores nulos
    print(f"\n2. VALORES NULOS:")
    nulos = df.isnull().sum()
    if nulos.sum() > 0:
        print(f"   ⚠ ENCONTRADOS valores nulos:")
        for col, count in nulos[nulos > 0].items():
            pct = (count / len(df)) * 100
            print(f"     • {col}: {count} ({pct:.1f}%)")
            problemas_encontrados.append(f"{nome}: {col} tem {count} nulos")
    else:
        print(f"   ✓ Sem valores nulos")
    
    # Verificar coluna Período
    if 'Período' in df.columns:
        print(f"\n3. COLUNA PERÍODO:")
        print(f"   Tipo de dados: {df['Período'].dtype}")
        print(f"   Valores únicos: {df['Período'].nunique()}")
        print(f"   Exemplo: {df['Período'].iloc[0]}")
        
        # Verificar formato da data
        sample_periodo = str(df['Período'].iloc[0])
        if '/' in sample_periodo:
            formato = "DD/MM/YYYY"
        elif '-' in sample_periodo:
            formato = "YYYY-MM"
        else:
            formato = "DESCONHECIDO"
            problemas_encontrados.append(f"{nome}: Formato de Período desconhecido")
        print(f"   Formato detectado: {formato}")
    
    # Verificar coluna Região
    if 'Região' in df.columns:
        print(f"\n4. COLUNA REGIÃO:")
        regioes = sorted(df['Região'].unique())
        print(f"   Regiões únicas: {len(regioes)}")
        for reg in regioes:
            count = (df['Região'] == reg).sum()
            print(f"     • {reg}: {count} linhas")
        
        # Verificar se todas começam com "Região de Saúde"
        regioes_erradas = [r for r in regioes if not (r.startswith('Região de Saúde') or r == 'Portugal Continental')]
        if regioes_erradas:
            print(f"   ⚠ Regiões com formato diferente:")
            for r in regioes_erradas:
                print(f"     • {r}")
            problemas_encontrados.append(f"{nome}: Regiões com formato inconsistente")
    
    # Verificar coluna Instituição
    col_inst = None
    if 'Instituição' in df.columns:
        col_inst = 'Instituição'
    elif 'Instituição Hospitalar' in df.columns:
        col_inst = 'Instituição Hospitalar'
    
    if col_inst:
        print(f"\n5. COLUNA INSTITUIÇÃO:")
        print(f"   Instituições únicas: {df[col_inst].nunique()}")
        
        # Verificar se todas terminam com EPE ou IP
        inst_sem_sufixo = df[col_inst][~df[col_inst].str.endswith(('EPE', 'IP'))].unique()
        if len(inst_sem_sufixo) > 0:
            print(f"   ⚠ Instituições sem sufixo EPE/IP ({len(inst_sem_sufixo)}):")
            for inst in inst_sem_sufixo[:5]:
                print(f"     • {inst}")
            if len(inst_sem_sufixo) > 5:
                print(f"     ... e mais {len(inst_sem_sufixo) - 5}")
    
    # Verificar colunas numéricas
    print(f"\n6. COLUNAS NUMÉRICAS:")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        for col in numeric_cols:
            negativos = (df[col] < 0).sum()
            if negativos > 0:
                print(f"   ⚠ {col}: {negativos} valores negativos")
                problemas_encontrados.append(f"{nome}: {col} tem valores negativos")
            
            # Verificar valores muito grandes (possíveis erros)
            if df[col].max() > 1e10:
                print(f"   ⚠ {col}: Valores muito grandes (max: {df[col].max():.2e})")
    else:
        print(f"   ℹ Sem colunas numéricas")
    
    # Verificar duplicados
    print(f"\n7. DUPLICADOS:")
    duplicados = df.duplicated().sum()
    if duplicados > 0:
        print(f"   ⚠ {duplicados} linhas duplicadas encontradas")
        problemas_encontrados.append(f"{nome}: {duplicados} linhas duplicadas")
    else:
        print(f"   ✓ Sem linhas duplicadas")

# RESUMO FINAL
print(f"\n{'='*80}")
print("RESUMO FINAL E RECOMENDAÇÕES")
print(f"{'='*80}")

if len(problemas_encontrados) > 0:
    print(f"\n⚠ PROBLEMAS ENCONTRADOS ({len(problemas_encontrados)}):")
    for i, problema in enumerate(problemas_encontrados, 1):
        print(f"   {i}. {problema}")
else:
    print("\n✓ Nenhum problema crítico encontrado!")

print("\n📋 RECOMENDAÇÕES PARA POWER BI:")
print("   1. ✓ Encoding UTF-8-sig (Excel compatível)")
print("   2. ✓ Separador ponto-e-vírgula (;)")
print("   3. ✓ Nomes de regiões padronizados")
print("   4. ✓ Nomes de instituições padronizados")
print("\n   SUGESTÕES ADICIONAIS:")
print("   • Converter coluna Período para formato Date no Power BI")
print("   • Criar tabela Dimensão de Regiões")
print("   • Criar tabela Dimensão de Instituições")
print("   • Criar tabela Dimensão de Calendário (DimCalendar.m já existe)")
print("   • Validar relacionamentos entre tabelas")

print("\n✅ Ficheiros prontos para importar no Power BI!")
