#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de Normalização Completa para CSV de Atendimentos
Aplica todas as correções necessárias identificadas nos scripts históricos
"""
import pandas as pd
import numpy as np
import re

print("=" * 80)
print("NORMALIZAÇÃO COMPLETA DO CSV DE ATENDIMENTOS")
print("=" * 80)

# 1. LER O FICHEIRO
print("\n[1/8] A ler ficheiro CSV...")
try:
    df = pd.read_csv('atendimentos-em-urgencia-triagem-manchester.csv1.csv', 
                     sep=';', 
                     encoding='utf-8')
    print(f"✓ Ficheiro lido com sucesso: {len(df)} linhas, {len(df.columns)} colunas")
except Exception as e:
    print(f"✗ Erro ao ler ficheiro: {e}")
    exit(1)

print("\nColunas originais:")
for i, col in enumerate(df.columns, 1):
    print(f"  {i}. {col}")

# 2. REMOVER COLUNA DE LOCALIZAÇÃO GEOGRÁFICA
print("\n[2/8] A remover coluna 'Localização Geográfica'...")
if 'Localização Geográfica' in df.columns:
    df = df.drop('Localização Geográfica', axis=1)
    print("✓ Coluna removida")
else:
    print("  (Coluna não encontrada)")

# 3. CORRIGIR NOMES DE COLUNAS
print("\n[3/8] A encurtar nomes das colunas...")
renomear = {
    'Nº Atendimentos em Urgência SU Triagem Manchester -Vermelha': 'Vermelha',
    'Nº Atendimentos em Urgência SU Triagem Manchester -Laranja': 'Laranja',
    'Nº Atendimentos em Urgência SU Triagem Manchester -Amarela': 'Amarela',
    'Nº Atendimentos em Urgência SU Triagem Manchester -Verde': 'Verde',
    'Nº Atendimentos em Urgência SU Triagem Manchester -Azul': 'Azul',
    'Nº Atendimentos em Urgência SU Triagem Manchester -Branca': 'Branca',
    'Nº Atendimentos s\\ Triagem Manchester': 'SemTriagem'
}

# Aplicar renomeação flexível
for old_name, new_name in renomear.items():
    # Procurar coluna que contenha parte do nome
    for col in df.columns:
        if old_name in col or ('Vermelha' in old_name and 'Vermelha' in col):
            df = df.rename(columns={col: new_name})
            print(f"  ✓ {col[:50]}... → {new_name}")
            break

# 4. NORMALIZAR NOMES DE INSTITUIÇÕES
print("\n[4/8] A normalizar nomes de instituições...")

# Dicionário de correções comuns
correcoes_instituicoes = {
    'Unidade Local de Saúde do Baixo Alentejo, EPE': 'ULS Baixo Alentejo',
    'Centro Hospitalar Universitário Cova da Beira, EPE': 'CHU Cova da Beira',
    'Hospital Garcia de Orta, EPE': 'Hospital Garcia de Orta',
    'Centro Hospitalar Universitário de São João, EPE': 'CHU São João',
    'Centro Hospitalar Póvoa de Varzim/Vila do Conde, EPE': 'CH Póvoa Varzim/Vila Conde',
    'Centro Hospitalar Vila Nova de Gaia/Espinho, EPE': 'CH Vila Nova Gaia/Espinho',
    'Unidade Local de Saúde de Matosinhos, EPE': 'ULS Matosinhos',
    'Hospital Espírito Santo de Évora, EPE': 'Hospital Espírito Santo Évora',
    'Centro Hospitalar de Leiria, EPE': 'CH Leiria',
    'Centro Hospitalar e Universitário de Coimbra, EPE': 'CHU Coimbra',
    'Centro Hospitalar Tondela-Viseu, EPE': 'CH Tondela-Viseu',
    'Unidade Local de Saúde da Guarda, EPE': 'ULS Guarda',
    'Unidade Local de Saúde de Castelo Branco, EPE': 'ULS Castelo Branco',
    'Centro Hospitalar Barreiro/Montijo, EPE': 'CH Barreiro/Montijo',
    'Hospital Professor Doutor Fernando Fonseca, EPE': 'Hospital Fernando Fonseca',
    'Centro Hospitalar Entre Douro e Vouga, EPE': 'CH Entre Douro e Vouga',
    'Centro Hospitalar de Setúbal, EPE': 'CH Setúbal',
    'Centro Hospitalar Trás-os-Montes e Alto Douro, EPE': 'CH Trás-os-Montes Alto Douro',
    'Hospital de Braga, PPP': 'Hospital de Braga',
    'Centro Hospitalar Universitário do Algarve, EPE': 'CHU Algarve',
    'Centro Hospitalar Universitário Lisboa Norte, EPE': 'CHU Lisboa Norte',
    'Hospital de Loures, PPP': 'Hospital de Loures',
    'Hospital de Vila Franca de Xira, PPP': 'Hospital Vila Franca Xira',
    'Centro Hospitalar do Alto Ave, EPE': 'CH Alto Ave',
    'Centro Hospitalar Universitário do Porto, EPE': 'CHU Porto',
    'Unidade Local de Saúde do Norte Alentejano, EPE': 'ULS Norte Alentejano',
    'Unidade Local de Saúde do Litoral Alentejano, EPE': 'ULS Litoral Alentejano',
    'Hospital Distrital da Figueira da Foz, EPE': 'Hospital Figueira Foz',
    'Centro Hospitalar Universitário Lisboa Central, EPE': 'CHU Lisboa Central'
}

if 'Instituição' in df.columns:
    df['Instituição'] = df['Instituição'].replace(correcoes_instituicoes)
    print(f"✓ {len(correcoes_instituicoes)} instituições normalizadas")
else:
    print("  (Coluna 'Instituição' não encontrada)")

# 5. PREENCHER VALORES VAZIOS
print("\n[5/8] A preencher células vazias com 0...")
colunas_numericas = ['Vermelha', 'Laranja', 'Amarela', 'Verde', 'Azul', 'Branca', 'SemTriagem']
for col in colunas_numericas:
    if col in df.columns:
        # Converter para numérico, valores inválidos viram NaN
        df[col] = pd.to_numeric(df[col], errors='coerce')
        # Preencher NaN com 0
        vazios = df[col].isna().sum()
        df[col] = df[col].fillna(0)
        if vazios > 0:
            print(f"  ✓ {col}: {vazios} células vazias preenchidas")

# Converter para inteiro
for col in colunas_numericas:
    if col in df.columns:
        df[col] = df[col].astype(int)

# 6. CALCULAR TOTAL DE ATENDIMENTOS
print("\n[6/8] A calcular coluna 'TotalAtendimentos'...")
colunas_cores = ['Vermelha', 'Laranja', 'Amarela', 'Verde', 'Azul', 'Branca']
colunas_existentes = [col for col in colunas_cores if col in df.columns]

if colunas_existentes:
    df['TotalAtendimentos'] = df[colunas_existentes].sum(axis=1)
    print(f"✓ Coluna criada (soma de {len(colunas_existentes)} cores)")
else:
    print("✗ Colunas de cores não encontradas")

# 7. VERIFICAR INCONSISTÊNCIAS
print("\n[7/8] A verificar inconsistências...")

inconsistencias = []

# Verificar valores negativos
for col in colunas_numericas:
    if col in df.columns:
        negativos = (df[col] < 0).sum()
        if negativos > 0:
            inconsistencias.append(f"  ⚠ {col}: {negativos} valores negativos")

# Verificar datas inválidas
if 'Período' in df.columns:
    try:
        df['Período_Check'] = pd.to_datetime(df['Período'], format='%Y-%m', errors='coerce')
        datas_invalidas = df['Período_Check'].isna().sum()
        if datas_invalidas > 0:
            inconsistencias.append(f"  ⚠ Período: {datas_invalidas} datas inválidas")
        df = df.drop('Período_Check', axis=1)
    except:
        pass

# Verificar instituições duplicadas no mesmo período
if 'Período' in df.columns and 'Instituição' in df.columns:
    duplicados = df.groupby(['Período', 'Instituição']).size()
    duplicados = duplicados[duplicados > 1]
    if len(duplicados) > 0:
        inconsistencias.append(f"  ⚠ {len(duplicados)} combinações Período+Instituição duplicadas")

if inconsistencias:
    print("Inconsistências encontradas:")
    for inc in inconsistencias:
        print(inc)
else:
    print("✓ Nenhuma inconsistência encontrada")

# 8. GUARDAR FICHEIRO LIMPO
print("\n[8/8] A guardar ficheiro normalizado...")
output_file = 'atendimentos-em-urgencia-triagem-manchester_NORMALIZADO.csv'

try:
    df.to_csv(output_file, 
              sep=';', 
              index=False, 
              encoding='utf-8-sig')
    print(f"✓ Ficheiro guardado: {output_file}")
    print(f"  - Linhas: {len(df)}")
    print(f"  - Colunas: {len(df.columns)}")
    
    # Mostrar estatísticas
    print("\n" + "=" * 80)
    print("ESTATÍSTICAS DO FICHEIRO NORMALIZADO")
    print("=" * 80)
    
    if 'TotalAtendimentos' in df.columns:
        print(f"\nTotal de atendimentos: {df['TotalAtendimentos'].sum():,}")
        print(f"Média por registo: {df['TotalAtendimentos'].mean():.0f}")
    
    if 'Período' in df.columns:
        periodos = df['Período'].nunique()
        print(f"\nPeríodos únicos: {periodos}")
        print(f"Primeiro período: {df['Período'].min()}")
        print(f"Último período: {df['Período'].max()}")
    
    if 'Instituição' in df.columns:
        instituicoes = df['Instituição'].nunique()
        print(f"\nInstituições únicas: {instituicoes}")
    
    if 'Região' in df.columns:
        regioes = df['Região'].nunique()
        print(f"Regiões únicas: {regioes}")
    
    # Top 5 instituições por volume
    if 'Instituição' in df.columns and 'TotalAtendimentos' in df.columns:
        print("\nTop 5 instituições (por volume total):")
        top5 = df.groupby('Instituição')['TotalAtendimentos'].sum().nlargest(5)
        for i, (inst, total) in enumerate(top5.items(), 1):
            print(f"  {i}. {inst}: {total:,} atendimentos")
    
    print("\n" + "=" * 80)
    print("✓ NORMALIZAÇÃO CONCLUÍDA COM SUCESSO!")
    print("=" * 80)
    
except Exception as e:
    print(f"✗ Erro ao guardar ficheiro: {e}")
    exit(1)
