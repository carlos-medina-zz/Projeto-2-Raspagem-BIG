import requests
from bs4 import BeautifulSoup

# Função que armazena uma linha da tabela. Ela recebe a linha a ser armazenada e a tag na qual ela se encontra
# Ela também limpa os dados que não são de interesse e retira espaços extras em branco e lineskips
def armazena_linha_tabela (linha_tabela, tag):
    linha_tabela = linha_tabela.find_all(tag)
    linha_tabela = [item.get_text() for item in linha_tabela]
    linha_tabela = [" ".join(item.split()) for item in linha_tabela]

    return (linha_tabela)

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

info_tabela2 = [[29, "b"],
                [30, "font"],
                [31, "font"],
                [32, "font"],
                [33, "font"],
                [34, "font"],
                [35, "font"],
                [36, "font"],
                [37, "font"],
                [38, "font"],             
]

info_tabela2 = [[56, "b"],
                [57, "font"],
                [58, "font"],
                [59, "font"],
                [60, "font"],
                [61, "font"],
                [62, "font"],
                [63, "font"],
                [64, "font"],          
]

# Download da página e leitura do seu conteúdo html
page = requests.get("http://www2.aneel.gov.br/aplicacoes/capacidadebrasil/capacidadebrasil.cfm")
soup = BeautifulSoup(page.content, 'html.parser')

# Seleciona todas as tabelas do site a partir da tag table e atribui cada uma a uma posição da lista
tabelas = soup.find_all("table")

# As três tabelas de interesse estão todas agrupadas no índice 3 da lista
indice_tabelas = 3

# Seleciona todas as linhas das três tabelas de interesse a partir da tag tr
linhas_tabelas = tabelas[indice_tabelas].find_all("tr")


'''
for item in info_tabela2:
    linhas_tabelas[item[0]] = armazena_linha_tabela(linhas_tabelas[item[0]], item[1])

for item in info_tabela2:
    print(linhas_tabelas[item[0]])
'''


contador = 0
for item in linhas_tabelas:
    print("Está é a linha ", contador)
    print(item)
    contador += 1
