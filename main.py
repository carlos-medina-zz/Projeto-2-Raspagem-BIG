import requests
from bs4 import BeautifulSoup

page = requests.get("http://www2.aneel.gov.br/aplicacoes/capacidadebrasil/capacidadebrasil.cfm")
soup = BeautifulSoup(page.content, 'html.parser')

# Seleciona as tabelas do site e atribui cada uma a uma posição da lista
tabelas = soup.select("table")

# As tabelas de interesse estão todas agrupadas no índice 3 
indice_tabelas = 3

print(tabelas[indice_tabelas])

'''
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find_all('p')[0].get_text())
'''