#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para converter Relatorio_SNS.md para HTML
"""

import markdown2
import os

ficheiro_md = 'Relatorio_SNS.md'
ficheiro_html = 'Relatorio_SNS.html'

# Ler conteúdo do ficheiro Markdown
with open(ficheiro_md, 'r', encoding='utf-8') as f:
    conteudo_md = f.read()

# Converter Markdown para HTML
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

# Template HTML completo
html_completo = f"""<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório Final Consolidado - Análise SNS</title>
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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }}
        
        h1 {{
            color: #1a237e;
            border-bottom: 4px solid #667eea;
            padding-bottom: 15px;
            margin-bottom: 10px;
            font-size: 2.5em;
            text-align: center;
        }}
        
        h2 {{
            color: #283593;
            border-bottom: 3px solid #5e35b1;
            padding-bottom: 10px;
            margin-top: 40px;
            margin-bottom: 20px;
            font-size: 2em;
        }}
        
        h3 {{
            color: #4a148c;
            margin-top: 30px;
            margin-bottom: 15px;
            font-size: 1.5em;
            border-left: 5px solid #9c27b0;
            padding-left: 15px;
        }}
        
        h4 {{
            color: #6a1b9a;
            margin-top: 20px;
            margin-bottom: 10px;
            font-size: 1.2em;
        }}
        
        p {{
            margin-bottom: 15px;
            text-align: justify;
        }}
        
        strong, b {{
            color: #d32f2f;
            font-weight: 600;
        }}
        
        em, i {{
            color: #00796b;
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
            border-top: 2px solid #e1bee7;
            margin: 30px 0;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        th {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            padding: 10px;
            border-bottom: 1px solid #e1bee7;
        }}
        
        tr:nth-child(even) {{
            background: #f3e5f5;
        }}
        
        tr:hover {{
            background: #e1bee7;
        }}
        
        code {{
            background: #f5f5f5;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            color: #c7254e;
        }}
        
        pre {{
            background: #37474f;
            color: #eceff1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 20px 0;
        }}
        
        pre code {{
            background: none;
            color: #eceff1;
        }}
        
        blockquote {{
            border-left: 5px solid #9c27b0;
            padding-left: 20px;
            margin: 20px 0;
            color: #6a1b9a;
            font-style: italic;
            background: #f3e5f5;
            padding: 15px 20px;
            border-radius: 5px;
        }}
        
        .metadata {{
            background: linear-gradient(135deg, #e8eaf6 0%, #f3e5f5 100%);
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 30px;
            border-left: 5px solid #5e35b1;
        }}
        
        .metadata p {{
            margin-bottom: 5px;
            font-weight: 500;
        }}
        
        .kpi-highlight {{
            background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%);
            border-left: 5px solid #fbc02d;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
            font-weight: 500;
        }}
        
        /* Estilo para emojis e ícones */
        h3::before {{
            margin-right: 10px;
        }}
        
        /* Navegação de topo */
        .toc {{
            background: #f5f5f5;
            padding: 20px;
            border-radius: 5px;
            margin: 20px 0;
        }}
        
        .toc a {{
            color: #5e35b1;
            text-decoration: none;
            display: block;
            padding: 5px 0;
        }}
        
        .toc a:hover {{
            color: #9c27b0;
            text-decoration: underline;
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
        
        // Smooth scroll para links internos
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                }}
            }});
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
