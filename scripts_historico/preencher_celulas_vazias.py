#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para preencher células vazias com média dos 3 valores antes e 3 depois
Aplica-se apenas a colunas numéricas
"""

import csv
import shutil
from datetime import datetime
import statistics

def is_numeric(value):
    """Verifica se um valor pode ser convertido para float"""
    if not value or value.strip() == '':
        return False
    try:
        float(value.replace(',', '.'))
        return True
    except ValueError:
        return False

def get_average_around(data, row_idx, col_idx, window=3):
    """
    Calcula a média de até 3 valores antes e 3 depois na mesma coluna
    Ignora valores vazios e não numéricos
    """
    values = []
    
    # Coletar valores antes (máximo 3)
    for i in range(max(1, row_idx - window), row_idx):  # Começa em 1 para pular cabeçalho
        if i < len(data):
            cell = data[i][col_idx].strip()
            if is_numeric(cell):
                values.append(float(cell.replace(',', '.')))
    
    # Coletar valores depois (máximo 3)
    for i in range(row_idx + 1, min(len(data), row_idx + window + 1)):
        cell = data[i][col_idx].strip()
        if is_numeric(cell):
            values.append(float(cell.replace(',', '.')))
    
    # Calcular média se houver valores
    if values:
        return round(statistics.mean(values), 2)
    return None

def fill_empty_cells(filepath):
    """
    Preenche células vazias com a média das 3 células antes e 3 depois
    Aplica-se apenas a colunas numéricas
    """
    print(f"\n{'='*80}")
    print(f"PREENCHIMENTO DE CÉLULAS VAZIAS - {filepath}")
    print(f"{'='*80}\n")
    
    # Criar backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = f"{filepath}.fill_backup_{timestamp}"
    shutil.copy2(filepath, backup_path)
    print(f"✓ Backup criado: {backup_path}")
    
    # Ler dados
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        data = list(reader)
    
    if len(data) < 2:
        print("⚠️ Ficheiro vazio ou sem dados")
        return
    
    header = data[0]
    total_filled = 0
    filled_by_column = {}
    
    # Identificar colunas numéricas (examinar primeiras 10 linhas)
    numeric_columns = set()
    for col_idx in range(len(header)):
        sample_values = [data[i][col_idx] for i in range(1, min(11, len(data)))]
        numeric_count = sum(1 for v in sample_values if is_numeric(v))
        if numeric_count > len(sample_values) / 2:  # Mais de 50% numéricos
            numeric_columns.add(col_idx)
    
    print(f"\n📊 Colunas numéricas identificadas: {len(numeric_columns)}")
    for col_idx in sorted(numeric_columns):
        print(f"   - {header[col_idx]} (coluna {col_idx})")
    
    # Processar cada linha (começando da linha 1, pular cabeçalho)
    for row_idx in range(1, len(data)):
        row = data[row_idx]
        
        for col_idx in range(len(row)):
            cell = row[col_idx].strip()
            
            # Preencher se:
            # 1. Célula está vazia
            # 2. Coluna é numérica
            if cell == '' and col_idx in numeric_columns:
                avg = get_average_around(data, row_idx, col_idx, window=3)
                
                if avg is not None:
                    # Substituir vírgula por ponto se necessário (manter formato original)
                    # Verificar formato dos valores existentes na coluna
                    uses_comma = False
                    for i in range(1, min(len(data), 10)):
                        if ',' in data[i][col_idx]:
                            uses_comma = True
                            break
                    
                    filled_value = str(avg).replace('.', ',') if uses_comma else str(avg)
                    data[row_idx][col_idx] = filled_value
                    total_filled += 1
                    
                    # Contar por coluna
                    col_name = header[col_idx]
                    filled_by_column[col_name] = filled_by_column.get(col_name, 0) + 1
    
    # Escrever dados atualizados
    if total_filled > 0:
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(data)
        
        print(f"\n✓ Total de células preenchidas: {total_filled}")
        print(f"\n📋 Detalhes por coluna:")
        for col_name, count in sorted(filled_by_column.items(), key=lambda x: x[1], reverse=True):
            print(f"   • {col_name}: {count} células")
        
        print(f"\n✅ Ficheiro atualizado com sucesso!")
    else:
        print(f"\n✓ Nenhuma célula vazia encontrada em colunas numéricas")
    
    return total_filled

if __name__ == "__main__":
    # Processar ficheiro de custos
    filepath = "custo-de-tratamento-mensal-por-doente.csv"
    
    try:
        total = fill_empty_cells(filepath)
        print(f"\n{'='*80}")
        print(f"✅ CONCLUÍDO - {total} células preenchidas")
        print(f"{'='*80}\n")
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
