#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para converter ficheiro Markdown para HTML com formatação de apresentação
"""

import markdown2
import os

def converter_markdown_para_html(ficheiro_md, ficheiro_html):
    """Converte ficheiro Markdown para HTML com estilos de apresentação"""
    
    # Ler conteúdo do ficheiro Markdown
    with open(ficheiro_md, 'r', encoding='utf-8') as f:
        conteudo_md = f.read()
    
    # Converter Markdown para HTML com extras
    html_body = markdown2.markdown(
        conteudo_md,
        extras=[
            'fenced-code-blocks',
            'tables',
            'break-on-newline',
            'header-ids',
            'strike',
            'task_list'
        ]
    )
    
    # Template HTML completo com CSS para apresentação
    html_completo = f"""<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roteiro de Apresentação Oral - Análise SNS</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }}
        
        h1 {{
            color: #2c3e50;
            border-bottom: 4px solid #3498db;
            padding-bottom: 15px;
            margin-bottom: 10px;
            font-size: 2.5em;
        }}
        
        h2 {{
            color: #2c3e50;
            border-bottom: 3px solid #e74c3c;
            padding-bottom: 10px;
            margin-top: 40px;
            margin-bottom: 20px;
            font-size: 2em;
        }}
        
        h3 {{
            color: #34495e;
            margin-top: 30px;
            margin-bottom: 15px;
            font-size: 1.5em;
            border-left: 5px solid #3498db;
            padding-left: 15px;
        }}
        
        h4 {{
            color: #7f8c8d;
            margin-top: 20px;
            margin-bottom: 10px;
            font-size: 1.2em;
        }}
        
        p {{
            margin-bottom: 15px;
            text-align: justify;
        }}
        
        strong, b {{
            color: #e74c3c;
            font-weight: 600;
        }}
        
        em, i {{
            color: #16a085;
        }}
        
        ul, ol {{
            margin-left: 30px;
            margin-bottom: 20px;
        }}
        
        li {{
            margin-bottom: 8px;
        }}
        
        hr {{
            border: none;
            border-top: 2px solid #ecf0f1;
            margin: 30px 0;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        th {{
            background: #3498db;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            padding: 10px;
            border-bottom: 1px solid #ecf0f1;
        }}
        
        tr:hover {{
            background: #f8f9fa;
        }}
        
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            color: #c7254e;
        }}
        
        pre {{
            background: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 20px 0;
        }}
        
        pre code {{
            background: none;
            color: #ecf0f1;
        }}
        
        blockquote {{
            border-left: 5px solid #3498db;
            padding-left: 20px;
            margin: 20px 0;
            color: #7f8c8d;
            font-style: italic;
            background: #ecf0f1;
            padding: 15px 20px;
            border-radius: 5px;
        }}
        
        /* Destaque para pausas e notas importantes */
        p:has(strong:only-child) {{
            background: #fff3cd;
            border-left: 5px solid #ffc107;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }}
        
        /* Checklist styling */
        input[type="checkbox"] {{
            margin-right: 10px;
            transform: scale(1.2);
        }}
        
        /* Seções de notas */
        h2:contains("NOTAS") {{
            background: #e8f5e9;
            padding: 15px;
            border-radius: 5px;
        }}
        
        /* Print styles */
        @media print {{
            body {{
                background: white;
                padding: 0;
            }}
            
            .container {{
                box-shadow: none;
                padding: 20px;
            }}
            
            h2 {{
                page-break-before: always;
            }}
            
            h2:first-of-type {{
                page-break-before: avoid;
            }}
        }}
        
        /* Emojis e ícones maiores */
        .container {{
            font-size: 16px;
        }}
        
        /* Metadata no topo */
        .metadata {{
            background: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 30px;
        }}
        
        .metadata p {{
            margin-bottom: 5px;
        }}
    </style>
</head>
<body>
    <div class="container">
        {html_body}
    </div>
    
    <script>
        // Adicionar target="_blank" a links externos
        document.querySelectorAll('a[href^="http"]').forEach(link => {{
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
        }});
        
        // Melhorar visualização de tabelas
        document.querySelectorAll('table').forEach(table => {{
            if (!table.querySelector('thead')) {{
                const firstRow = table.querySelector('tr');
                if (firstRow) {{
                    const thead = document.createElement('thead');
                    thead.appendChild(firstRow);
                    table.insertBefore(thead, table.firstChild);
                }}
            }}
        }});
    </script>
</body>
</html>"""
    
    # Guardar HTML
    with open(ficheiro_html, 'w', encoding='utf-8') as f:
        f.write(html_completo)
    
    print(f"✅ Conversão concluída!")
    print(f"📄 Ficheiro HTML criado: {ficheiro_html}")
    print(f"📊 Tamanho: {os.path.getsize(ficheiro_html) / 1024:.2f} KB")

if __name__ == "__main__":
    ficheiro_md = "roteiro-apresentacao-sns.md"
    ficheiro_html = "roteiro-apresentacao-sns.html"
    
    if os.path.exists(ficheiro_md):
        converter_markdown_para_html(ficheiro_md, ficheiro_html)
    else:
        print(f"❌ Erro: Ficheiro '{ficheiro_md}' não encontrado!")
