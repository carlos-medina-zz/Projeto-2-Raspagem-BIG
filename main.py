import requests
from bs4 import BeautifulSoup

# Função que armazena uma linha da tabela. Ela recebe a linha a ser armazenada e a tag na qual ela se encontra
# Ela também limpa os dados que não são de interesse e retira espaços extras em branco e lineskips
def armazena_linha_tabela (linha_tabela, tag):
    linha_tabela = linha_tabela.find_all(tag)
    linha_tabela = [item.get_text() for item in linha_tabela]
    linha_tabela = [" ".join(item.split()) for item in linha_tabela]

    return (linha_tabela)

# Função similar a armazena_linha_tabela mas que recebe duas tags. Criada para ler 1) a primeira coluna das linhas
# de dados das tabelas 2 e 3 que possuia uma tag distinta dos outros dados 2) as outras colunas com tags iguais e
# depois juntar as duas
def armazena_linha_tabela2 (linha_tabela, tag1, tag2):
    linha_tabela1 = armazena_linha_tabela(linha_tabela, tag1)
    linha_tabela2 = armazena_linha_tabela(linha_tabela, tag2)
    linha_tabela = linha_tabela2
    linha_tabela.insert(0, linha_tabela1[0])
    
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
                [11, "font"]]

# Similar a info_tabela1, porém, com listas que possuem três itens.
# O segundo item é a tag da primeira coluna das linhas de dados enquanto o terceiro item é a tag das outras colunas
info_tabela2 = [[29, "b"],
                [30, "font"],
                [31, "a", "font"],
                [32, "a", "font"],
                [33, "a", "font"],
                [34, "a", "font"],
                [35, "a", "font"],
                [36, "a", "font"],
                [37, "a", "font"],
                [38, "font"]]

# Igual a info_tabela2
info_tabela3 = [[56, "b"],
                [57, "font"],
                [58, "a", "font"],
                [59, "a", "font"],
                [60, "a", "font"],
                [61, "a", "font"],
                [62, "a", "font"],
                [63, "a", "font"],
                [64, "font"]]

# Criação de uma lista as informações de todas as tabelas
info_tabelas = [info_tabela1, info_tabela2, info_tabela3]

# Download da página e leitura do seu conteúdo html
page = requests.get("http://www2.aneel.gov.br/aplicacoes/capacidadebrasil/capacidadebrasil.cfm")
soup = BeautifulSoup(page.content, 'html.parser')

# Seleciona todas as tabelas do site a partir da tag table e atribui cada uma a uma posição da lista
tabelas = soup.find_all("table")

# As três tabelas de interesse estão todas agrupadas no índice 3 da lista
indice_tabelas = 3

# Seleciona todas as linhas das três tabelas de interesse a partir da tag tr
linhas_tabelas = tabelas[indice_tabelas].find_all("tr")

# Aquisição e limpeza de todas as linhas das três tabelas de interesse
for info_tabela in info_tabelas:
    for linha in info_tabela:
        if len(linha) == 2:
            linhas_tabelas[linha[0]] = armazena_linha_tabela(linhas_tabelas[linha[0]], linha[1])
        else:
            linhas_tabelas[linha[0]] = armazena_linha_tabela2(linhas_tabelas[linha[0]], linha[1], linha[2])

for info_tabela in info_tabelas:
    for linha in info_tabela:
        print(linhas_tabelas[linha[0]])