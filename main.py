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

# Armazena o título da tabela 1 que está na linha de índice 1 entre as tags b. Como o método find_all() 
# retorna uma string é necessário acessar o elemento [0]
titulo_tabela1 = linhas_tabelas[1].find_all('b')[0].get_text()

# Retirada de alguns espaços extras em branco e lineskips
titulo_tabela1 = " ".join(titulo_tabela1.split())

# Armazena a linha da tabela que contém o nome de cada coluna. Ela está entre as tags font
linha1_tabela1 = linhas_tabelas[2].find_all('font')

# Limpeza dos dados da segundo linha da tabela
linha1_tabela1 = [item.get_text() for item in linha1_tabela1]

# Retirada de alguns espaços extras em branco e lineskips
linha1_tabela1 = [" ".join(item.split()) for item in linha1_tabela1]

# Função que executa as três linhas acima. Também funciona para retirar o título da tabela
def armazena_linha_tabela (linha_tabela, tag):
    linha_tabela = linha_tabela.find_all(tag)
    linha_tabela = [item.get_text() for item in linha_tabela]
    linha_tabela = [" ".join(item.split()) for item in linha_tabela]

    return (linha_tabela)

linhas_tabelas[3] = armazena_linha_tabela(linhas_tabelas[3], "font")
print(len(linhas_tabelas[3]))

# Lista que contém em cada elemento informações sobre cada linha da tabela. Cada elemento é outra lista
# que contém o índice da sua posição na tabela e a tag para ser encontrado
# O primeiro elemento refere-se ao título, o segundo ao nome das colunas e ao restante os valores
info_tabela1 = [[1, "b"],
                [2, "font"],
                [3, "font"],
                [4, "font"],
                [5, "font"],
                [6, "font"],
                [7, "font"],
                [8, "font"],
                [9, "font"],
                [10, "font"],
                [11, "font"],              
]