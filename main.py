import requests
from bs4 import BeautifulSoup

# Download da página e leitura do seu conteúdo html
page = requests.get("http://www2.aneel.gov.br/aplicacoes/capacidadebrasil/capacidadebrasil.cfm")
soup = BeautifulSoup(page.content, 'html.parser')

# Seleciona todas as tabelas do site a partir da tag table e atribui cada uma a uma posição da lista
tabelas = soup.find_all("table")

# As três tabelas de interesse estão todas agrupadas no índice 3 da lista
indice_tabelas = 3

# Seleciona todas as linhas das três tabelas de interesse a partir da tag tr
linhas_tabelas = tabelas[indice_tabelas].find_all("tr")

# Título da tabela 1 que está na linha de índice 1 entre as tags b
titulo_tabela1 = linhas_tabelas[1].find_all('b')[0].get_text()

# Retirada de alguns espaços extras em branco e lineskips
titulo_tabela1 = " ".join(titulo_tabela1.split())

# Dados da segundo linha da tabela que está entre as tags font
linha1_tabela1 = linhas_tabelas[2].find_all('font')

# Limpeza dos dados da segundo linha da tabela
linha1_tabela1 = [item.get_text() for item in linha1_tabela1]
print(linha1_tabela1)

# Retirada de alguns espaços extras em branco e lineskips
linha1_tabela1 = [" ".join(item.split()) for item in linha1_tabela1]
print(linha1_tabela1)

# Título da tabela 1 -> linhas_tabelas[1]
# Índice da tabela 1 -> linhas_tabelas[2]
# Valores da tabela 1 -> linhas_tabelas[3] a linhas_tabelas[11]

''' # Mostra todas as linhas das tabelas de interesse
contador_de_linha = 0
for item in linhas_tabelas:
    print("Essa é a linha", contador_de_linha)
    print(item, "\n")
    contador_de_linha += 1
'''