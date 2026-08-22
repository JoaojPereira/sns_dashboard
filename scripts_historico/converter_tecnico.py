# -*- coding: utf-8 -*-
"""
Conversor de RELATÓRIO TÉCNICO.txt para HTML
Com formatação profissional para documentação técnica
"""

import re
from pathlib import Path

def convert_technical_report_to_html(input_file, output_file):
    """Converte o relatório técnico TXT para HTML estilizado"""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Processar o conteúdo
    html_content = process_content(content)
    
    # Template HTML com estilo técnico
    html_template = f"""<!DOCTYPE html>
<html lang="pt-PT">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório Técnico Completo - SNS Portugal</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #2c3e50;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        }}
        
        h1 {{
            color: #003DA5;
            font-size: 2.5em;
            margin-bottom: 10px;
            padding-bottom: 15px;
            border-bottom: 4px solid #003DA5;
        }}
        
        h2 {{
            color: #2E8B57;
            font-size: 1.8em;
            margin-top: 40px;
            margin-bottom: 20px;
            padding-left: 15px;
            border-left: 5px solid #2E8B57;
        }}
        
        h3 {{
            color: #FF8C00;
            font-size: 1.4em;
            margin-top: 30px;
            margin-bottom: 15px;
        }}
        
        h4 {{
            color: #DC143C;
            font-size: 1.2em;
            margin-top: 20px;
            margin-bottom: 10px;
        }}
        
        p {{
            margin-bottom: 15px;
            text-align: justify;
        }}
        
        .subtitle {{
            color: #7f8c8d;
            font-size: 1.2em;
            margin-bottom: 30px;
        }}
        
        .metadata {{
            background: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 30px;
            font-size: 0.95em;
        }}
        
        .box {{
            background: #f8f9fa;
            border-left: 4px solid #003DA5;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
        }}
        
        .box-success {{
            background: #d4edda;
            border-left-color: #28a745;
        }}
        
        .box-warning {{
            background: #fff3cd;
            border-left-color: #ffc107;
        }}
        
        .box-danger {{
            background: #f8d7da;
            border-left-color: #dc3545;
        }}
        
        .box-info {{
            background: #d1ecf1;
            border-left-color: #17a2b8;
        }}
        
        .tree {{
            font-family: 'Courier New', monospace;
            background: #2c3e50;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 20px 0;
            line-height: 1.5;
        }}
        
        .metrics {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        
        .metric-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        .metric-card h4 {{
            color: white;
            margin-bottom: 10px;
            font-size: 0.9em;
            text-transform: uppercase;
        }}
        
        .metric-value {{
            font-size: 2em;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        
        .metric-label {{
            font-size: 0.85em;
            opacity: 0.9;
        }}
        
        ul, ol {{
            margin-left: 30px;
            margin-bottom: 15px;
        }}
        
        li {{
            margin-bottom: 8px;
        }}
        
        .checklist {{
            list-style: none;
            margin-left: 0;
        }}
        
        .checklist li:before {{
            content: "✓ ";
            color: #28a745;
            font-weight: bold;
            margin-right: 8px;
        }}
        
        .emoji {{
            font-size: 1.2em;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        th {{
            background: #003DA5;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            padding: 10px 12px;
            border-bottom: 1px solid #ddd;
        }}
        
        tr:hover {{
            background: #f5f5f5;
        }}
        
        .toc {{
            background: #f8f9fa;
            padding: 25px;
            border-radius: 8px;
            margin: 30px 0;
        }}
        
        .toc h3 {{
            color: #003DA5;
            margin-top: 0;
        }}
        
        .toc ul {{
            list-style: none;
            margin-left: 0;
        }}
        
        .toc li {{
            padding: 8px 0;
        }}
        
        .toc a {{
            color: #003DA5;
            text-decoration: none;
            transition: all 0.3s;
        }}
        
        .toc a:hover {{
            color: #2E8B57;
            padding-left: 10px;
        }}
        
        .back-to-top {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: #003DA5;
            color: white;
            padding: 15px 20px;
            border-radius: 50px;
            text-decoration: none;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            transition: all 0.3s;
            font-weight: bold;
        }}
        
        .back-to-top:hover {{
            background: #2E8B57;
            transform: translateY(-3px);
        }}
        
        .status-critical {{ color: #dc3545; font-weight: bold; }}
        .status-warning {{ color: #ffc107; font-weight: bold; }}
        .status-success {{ color: #28a745; font-weight: bold; }}
        .status-info {{ color: #17a2b8; font-weight: bold; }}
        
        @media print {{
            body {{
                background: white;
                padding: 0;
            }}
            .container {{
                box-shadow: none;
                padding: 20px;
            }}
            .back-to-top {{
                display: none;
            }}
        }}
        
        @media (max-width: 768px) {{
            .container {{
                padding: 20px;
            }}
            h1 {{
                font-size: 2em;
            }}
            .metrics {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        {html_content}
    </div>
    <a href="#top" class="back-to-top">↑ Topo</a>
</body>
</html>"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    return output_file

def process_content(text):
    """Processa o conteúdo do relatório técnico"""
    
    lines = text.split('\n')
    html = ['<div id="top">']
    
    in_tree = False
    in_box = False
    current_section = ""
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Título principal
        if i == 0 and 'RELATÓRIO TÉCNICO' in stripped:
            html.append(f'<h1>{stripped}</h1>')
            continue
        
        # Subtítulo
        if i == 1 and 'Relatório de Ineficiências' in stripped:
            html.append(f'<p class="subtitle">{stripped}</p>')
            continue
        
        # Metadata
        if 'Projeto Business Intelligence' in stripped or 'Versão Final' in stripped:
            if not any('<div class="metadata">' in h for h in html[-3:]):
                html.append('<div class="metadata">')
            html.append(f'<p>{stripped}</p>')
            if 'Versão Final' in stripped:
                html.append('</div>')
            continue
        
        # Índice
        if stripped == 'ÍNDICE':
            html.append('<div class="toc"><h3>📋 ' + stripped + '</h3><ul>')
            continue
        
        if stripped and stripped[0].isdigit() and '.' in stripped[:2] and 'FASE' in stripped:
            section_num = stripped.split('.')[0]
            section_name = stripped.split('.', 1)[1].strip()
            html.append(f'<li><a href="#section{section_num}">{section_num}. {section_name}</a></li>')
            continue
        
        # Fechar índice
        if html and '<ul>' in html[-10:] and not stripped:
            if '</ul>' not in html[-5:]:
                html.append('</ul></div>')
        
        # Seções principais (1. FASE, 2. FASE, etc.)
        if re.match(r'^\d+\.\s+FASE\s+\d+', stripped):
            section_num = stripped.split('.')[0]
            html.append(f'<h2 id="section{section_num}">{stripped}</h2>')
            current_section = stripped
            continue
        
        # Subseções (###)
        if stripped.startswith('###'):
            html.append(f'<h3>{stripped.replace("###", "").strip()}</h3>')
            continue
        
        # PÁGINA X (dashboards)
        if re.match(r'^PÁGINA\s+\d+:', stripped):
            html.append(f'<h3 class="emoji">{stripped}</h3>')
            continue
        
        # Boxes especiais
        if any(keyword in stripped for keyword in ['PROBLEMA', 'ACHADO', 'LIÇÃO', 'RISCO']):
            box_type = 'danger' if 'PROBLEMA' in stripped or 'RISCO' in stripped else 'warning' if 'ACHADO' in stripped else 'info'
            html.append(f'<div class="box box-{box_type}"><h4>{stripped}</h4>')
            in_box = True
            continue
        
        # Árvores e estruturas (com caracteres especiais)
        # Detectar início de diagrama (linhas com estruturas visuais)
        has_tree_chars = any(char in line for char in ['├', '└', '│', '─', '┌', '┐', '▼', '┼'])
        has_diagram = 'DimCalendário' in stripped or 'FactAten' in stripped or 'FactMonit' in stripped
        
        if has_tree_chars or (in_tree and (line.startswith(' ' * 4) or has_diagram)):
            if not in_tree:
                html.append('<pre class="tree">')
                in_tree = True
            html.append(line)
            # Continuar árvore se próxima linha também tiver estrutura
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                if not any(char in next_line for char in ['├', '└', '│', '─']) and not next_line.strip().startswith('Dim') and not next_line.strip().startswith('Fact'):
                    if next_line.strip() and not next_line.strip().startswith('###'):
                        html.append('</pre>')
                        in_tree = False
            continue
        else:
            if in_tree and stripped:
                html.append('</pre>')
                in_tree = False
        
        # Listas com checkmark
        if stripped.startswith('✓'):
            if '</ul>' not in html[-1]:
                html.append('<ul class="checklist">')
            html.append(f'<li>{stripped[1:].strip()}</li>')
            # Fechar lista se próxima linha não for item
            if i + 1 < len(lines) and not lines[i+1].strip().startswith('✓'):
                html.append('</ul>')
            continue
        
        # Métricas especiais (com emojis de status)
        if any(emoji in stripped for emoji in ['🔴', '🟡', '🟢', '🟠', '⚠️', '❌', '✅']):
            status_class = ''
            if '🔴' in stripped or '❌' in stripped:
                status_class = 'status-critical'
            elif '🟡' in stripped or '⚠️' in stripped:
                status_class = 'status-warning'
            elif '🟢' in stripped or '✅' in stripped:
                status_class = 'status-success'
            
            html.append(f'<p class="{status_class}">{stripped}</p>')
            continue
        
        # Fechar box se linha vazia após box
        if in_box and not stripped:
            html.append('</div>')
            in_box = False
            continue
        
        # Parágrafos normais
        if stripped:
            # Destacar números importantes (valores, percentagens, euros)
            if re.search(r'(\d+[,.]?\d*\s*(milhões|mil|%|€|M))', stripped):
                stripped = re.sub(r'(\d+[,.]?\d*\s*(milhões|mil|%|€|M|min|minutos))', r'<strong>\1</strong>', stripped)
            
            html.append(f'<p>{stripped}</p>')
        else:
            html.append('<br>')
    
    # Fechar tags pendentes
    if in_tree:
        html.append('</pre>')
    if in_box:
        html.append('</div>')
    
    html.append('</div>')
    
    return '\n'.join(html)

if __name__ == '__main__':
    input_file = 'RELATÓRIO TÉCNICO.txt'
    output_file = 'RELATÓRIO TÉCNICO.html'
    
    result = convert_technical_report_to_html(input_file, output_file)
    file_size = Path(result).stat().st_size / 1024  # KB
    
    print(f"✅ Conversão completa!")
    print(f"📄 Arquivo: {result}")
    print(f"📊 Tamanho: {file_size:.2f} KB")
    print(f"\n🎨 Features incluídas:")
    print("  • Formatação técnica profissional")
    print("  • Gradient roxo para documentação técnica")
    print("  • Índice interativo com links")
    print("  • Boxes coloridos para problemas/achados")
    print("  • Árvores de dados com fundo escuro")
    print("  • Cards de métricas destacados")
    print("  • Botão voltar ao topo")
    print("  • Responsivo e pronto para impressão")
