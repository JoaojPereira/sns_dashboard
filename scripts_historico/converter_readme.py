#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para converter README.md para HTML
"""

import markdown2
import os

ficheiro_md = 'README.md'
ficheiro_html = 'README.html'

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
        'task_list',
        'code-friendly'
    ]
)

# Template HTML completo
html_completo = f"""<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Report de Ineficiências SNS</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #24292e;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            padding: 20px;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            padding: 50px;
            border-radius: 12px;
            box-shadow: 0 15px 50px rgba(0,0,0,0.3);
        }}
        
        /* Header */
        h1 {{
            color: #0366d6;
            border-bottom: 4px solid #0366d6;
            padding-bottom: 15px;
            margin-bottom: 20px;
            font-size: 3em;
            display: flex;
            align-items: center;
            gap: 15px;
        }}
        
        h2 {{
            color: #24292e;
            border-bottom: 3px solid #e1e4e8;
            padding-bottom: 10px;
            margin-top: 50px;
            margin-bottom: 25px;
            font-size: 2.2em;
        }}
        
        h3 {{
            color: #0366d6;
            margin-top: 35px;
            margin-bottom: 18px;
            font-size: 1.6em;
            border-left: 5px solid #0366d6;
            padding-left: 15px;
        }}
        
        h4 {{
            color: #586069;
            margin-top: 25px;
            margin-bottom: 12px;
            font-size: 1.3em;
        }}
        
        p {{
            margin-bottom: 15px;
            color: #24292e;
        }}
        
        /* Links */
        a {{
            color: #0366d6;
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        /* Code blocks */
        code {{
            background: #f6f8fa;
            padding: 3px 6px;
            border-radius: 4px;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            color: #e83e8c;
            font-size: 0.9em;
        }}
        
        pre {{
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 20px;
            border-radius: 6px;
            overflow-x: auto;
            margin: 20px 0;
            border-left: 5px solid #0366d6;
        }}
        
        pre code {{
            background: none;
            color: #f8f8f2;
            padding: 0;
        }}
        
        /* Lists */
        ul, ol {{
            margin-left: 35px;
            margin-bottom: 20px;
        }}
        
        li {{
            margin-bottom: 10px;
        }}
        
        /* Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            box-shadow: 0 2px 15px rgba(0,0,0,0.1);
            font-size: 0.95em;
        }}
        
        th {{
            background: linear-gradient(135deg, #0366d6 0%, #0256c4 100%);
            color: white;
            padding: 14px;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            padding: 12px 14px;
            border-bottom: 1px solid #e1e4e8;
        }}
        
        tr:nth-child(even) {{
            background: #f6f8fa;
        }}
        
        tr:hover {{
            background: #e1f5ff;
        }}
        
        /* Horizontal line */
        hr {{
            border: none;
            border-top: 2px solid #e1e4e8;
            margin: 40px 0;
        }}
        
        /* Strong/Bold */
        strong, b {{
            color: #d73a49;
            font-weight: 600;
        }}
        
        /* Emphasis/Italic */
        em, i {{
            color: #22863a;
        }}
        
        /* Blockquote */
        blockquote {{
            border-left: 5px solid #dfe2e5;
            padding-left: 20px;
            margin: 20px 0;
            color: #6a737d;
            font-style: italic;
            background: #f6f8fa;
            padding: 15px 20px;
            border-radius: 5px;
        }}
        
        /* Badges/Tags */
        .badge {{
            display: inline-block;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: 600;
            margin: 5px;
        }}
        
        /* Info boxes */
        .info-box {{
            background: #e7f3ff;
            border-left: 5px solid #0366d6;
            padding: 20px;
            margin: 25px 0;
            border-radius: 5px;
        }}
        
        .warning-box {{
            background: #fff3cd;
            border-left: 5px solid #ffc107;
            padding: 20px;
            margin: 25px 0;
            border-radius: 5px;
        }}
        
        .success-box {{
            background: #d4edda;
            border-left: 5px solid #28a745;
            padding: 20px;
            margin: 25px 0;
            border-radius: 5px;
        }}
        
        /* Emojis larger */
        h1, h2, h3 {{
            font-size: 1.1em;
        }}
        
        /* Navigation TOC */
        .toc {{
            background: #f6f8fa;
            padding: 25px;
            border-radius: 8px;
            margin: 30px 0;
            border: 1px solid #e1e4e8;
        }}
        
        .toc h3 {{
            margin-top: 0;
            border: none;
            padding: 0;
        }}
        
        .toc a {{
            display: block;
            padding: 8px 0;
            color: #0366d6;
        }}
        
        .toc a:hover {{
            color: #024c91;
        }}
        
        /* Sections */
        section {{
            margin-bottom: 50px;
        }}
        
        /* Print styles */
        @media print {{
            body {{
                background: white;
                padding: 0;
            }}
            
            .container {{
                box-shadow: none;
                padding: 30px;
            }}
            
            h2 {{
                page-break-before: always;
            }}
            
            h2:first-of-type {{
                page-break-before: avoid;
            }}
            
            pre, table {{
                page-break-inside: avoid;
            }}
        }}
        
        /* Scroll behavior */
        html {{
            scroll-behavior: smooth;
        }}
        
        /* Back to top button */
        #back-to-top {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: #0366d6;
            color: white;
            padding: 15px 20px;
            border-radius: 50px;
            cursor: pointer;
            display: none;
            box-shadow: 0 5px 20px rgba(0,0,0,0.2);
            z-index: 1000;
        }}
        
        #back-to-top:hover {{
            background: #024c91;
        }}
    </style>
</head>
<body>
    <div class="container">
        {html_body}
    </div>
    
    <div id="back-to-top" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})">
        ⬆ Topo
    </div>
    
    <script>
        // Back to top button
        window.addEventListener('scroll', function() {{
            const backToTop = document.getElementById('back-to-top');
            if (window.pageYOffset > 300) {{
                backToTop.style.display = 'block';
            }} else {{
                backToTop.style.display = 'none';
            }}
        }});
        
        // External links
        document.querySelectorAll('a[href^="http"]').forEach(link => {{
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
        }});
        
        // Table improvements
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
        
        // Smooth scroll for internal links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                }}
            }});
        }});
        
        // Highlight code syntax (basic)
        document.querySelectorAll('pre code').forEach(block => {{
            // Simple keyword highlighting for DAX
            let html = block.innerHTML;
            const keywords = ['VAR', 'RETURN', 'IF', 'CALCULATE', 'SWITCH', 'TRUE', 'FALSE', 'DIVIDE', 'SUM', 'AVERAGE', 'ALL'];
            keywords.forEach(keyword => {{
                const regex = new RegExp('\\\\b' + keyword + '\\\\b', 'g');
                html = html.replace(regex, '<span style="color: #66d9ef">' + keyword + '</span>');
            }});
            block.innerHTML = html;
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
