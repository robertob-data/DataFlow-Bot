import requests
from bs4 import BeautifulSoup
import time
import random

estrelas = {'One' : 1, 'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5}
meus_headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
objeto_sessao = requests.Session()

def coletar_html(url):
    try:
        resposta = requests.get(url, headers=meus_headers)
        time.sleep(random.randint(3,7))
        if resposta.status_code == 200:
            print('[SISTEMA] Coneçao Estabelecida..')
            return resposta.text
        else:
            print(f'[SISTEMA] Erro HTTP: Código {resposta.status_code}')
            return ''
    except requests.exceptions.RequestException as erro_conexao:
            print(f'[SISTEMA] Falha na Coneçao {erro_conexao}')
            return ''

def limpesa_extrutura(html_bruto, lista_livros):
     html_limpo = BeautifulSoup(html_bruto, 'html.parser')
     card = html_limpo.find_all('article', class_='product_pod')

     for livro in card:
          
          #nome do livro
          nome = livro.h3.a['title']
          
          #preço
          preco_sujo = livro.find('p', class_='price_color').get_text(strip=True)
          preco = float(preco_sujo.replace('Â£', '').replace('£', '').replace(',', '.'))
          
          #avaliaçao
          estrelas_tag = livro.find('p', class_='star-rating')
          avaliaçao = estrelas[estrelas_tag['class'][1]]
          
          #estoque
          #capturando link
          link = livro.h3.a['href']
          link_completo = f'https://books.toscrape.com/catalogue/' + link

          #pegando o html
          try:
                valor_estoque = 0
                html_estoque = objeto_sessao.get(link_completo, headers=meus_headers)
                time.sleep(random.uniform(0.2, 0.7))
                if html_estoque.status_code == 200:
                    sopa_estoque = BeautifulSoup(html_estoque.text, 'html.parser')
                    tabela = sopa_estoque.find('div', class_='product_main')
                    in_stock = tabela.find('p', class_='instock availability').get_text(strip=True)
                    valor_estoque = int(in_stock.replace('In stock (', '').replace(' available)', ''))
                else:
                    print(f'[SISTEMA] Erro HTTP: Código {html_estoque.status_code}')
          except requests.exceptions.RequestException as erro:
                print(f'[SISTEMA] Falha na Coneçao {erro}')
                
          #link de compra
          link_compra = link_completo

          #Modelo Final
          modelo = {
               'Titulo Do Livro' : nome,
               'Preço Do Livro (£)' : preco,
               'Estrelas' : avaliaçao,
               'Quantidade em Estoque' : valor_estoque,
               'Link Do Livro' : link_compra
          }
          print(f"[{len(lista_livros)}] {nome}")
          
          lista_livros.append(modelo)
     return lista_livros

def scraper(qty_paginas):
    lista_livros = []
    url = 'https://books.toscrape.com'
    for i in range(1, qty_paginas+1):
         link_completo = url + f'/catalogue/page-{i}.html'
         html_livros = coletar_html(link_completo)
         if html_livros != '':
            limpesa_extrutura(html_livros, lista_livros)
            print(f"\n📄 Página {i} finalizada\n")
         else:
             print('[SISTEMA][FALHA] Erro na Coneçao...')
             
        
    return lista_livros
     