import requests
import os
import zipfile
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}
pagina = requests.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos', headers=headers)
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')
links = dados_pagina.find_all("a", href=lambda href: href and ("Anexo_I" in href or "Anexo_II" in href) and href.endswith('.pdf'))

if not links: 
    print('Nenhum link foi encontrado.')
    exit()

os.makedirs('downloads', exist_ok=True)
arquivos_baixados = []
for link in links:
    if 'href' in link.attrs:
        file_url = link['href']

        if not file_url.startswith('http'):
            file_url = 'https://www.gov.br' + file_url

        file_name = file_url.split('/')[-1]
        file_path = os.path.join('downloads', file_name)

        response = requests.get(file_url, headers=headers)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f'Arquivo baixado: {file_name}')
            arquivos_baixados.append(file_path)
        else:
            print(f'Erro ao baixar: {file_url}')

zip_path = 'downloads/arquivos_compactados.zip'
with zipfile.ZipFile(zip_path, 'w') as zipf:
     for file in arquivos_baixados:
          zipf.write(file, os.path.basename(file))

print(f'Arquivos compactados em: {zip_path}')
