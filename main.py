import requests
from bs4 import BeautifulSoup

page = requests.get("http://www2.aneel.gov.br/aplicacoes/capacidadebrasil/capacidadebrasil.cfm")
soup = BeautifulSoup(page.content, 'html.parser')

# Seleciona todas as tabelas do site a partir da tag table e atribui cada uma a uma posição da lista
tabelas = soup.find_all("table")

# As três tabelas de interesse estão todas agrupadas no índice 3 da lista
indice_tabelas = 3

# Seleciona todas as linhas das três tabelas de interesse a partir da tag tr
linhas_tabelas = tabelas[indice_tabelas].find_all("tr")

print(len(linhas_tabelas))