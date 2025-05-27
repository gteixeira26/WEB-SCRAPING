PROJETO - TESTE DE WEB SCRAPING

Este script em Python acessa o site oficial da ANS (Agência Nacional de Saúde Suplementar)
e faz o download automático dos arquivos Anexo I e Anexo II no formato PDF.

Depois que os arquivos são baixados, eles são salvos em uma pasta chamada "downloads"
e compactados em um único arquivo ZIP chamado "arquivos_compactados.zip".

Basta rodar o arquivo Intuitivecareteste1.py com Python instalado.

Não é necessário criar pastas ou baixar os PDFs manualmente — o código faz tudo automaticamente.

Bibliotecas utilizadas:
- requests
- beautifulsoup4
- os
- zipfile
