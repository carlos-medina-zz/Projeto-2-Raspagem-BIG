import requests
from bs4 import BeautifulSoup

# Função que armazena uma linha da tabela. Ela recebe a linha a ser armazenada e a tag na qual ela se encontra
# Ela também limpa os dados que não são de interesse e retira espaços extras em branco e lineskips
def Armazena_linha_tabela (linha_tabela, tag):
    linha_tabela = linha_tabela.find_all(tag)
    linha_tabela = [item.get_text() for item in linha_tabela]
    linha_tabela = [" ".join(item.split()) for item in linha_tabela]

    return (linha_tabela)

# Função similar a armazena_linha_tabela mas que recebe duas tags. Criada para 1) ler a primeira coluna das linhas
# de dados das tabelas 2 e 3 que possui uma tag distinta dos outros dados 2) ler as outras colunas que possuem só uma tag
# 3) juntar as duas leituras em uma única variável
def Armazena_linha_tabela2 (linha_tabela, tag1, tag2):
    linha_tabela1 = Armazena_linha_tabela(linha_tabela, tag1)
    linha_tabela2 = Armazena_linha_tabela(linha_tabela, tag2)
    linha_tabela = linha_tabela2
    linha_tabela.insert(0, linha_tabela1[0])
    
    return (linha_tabela)

# Função que extrai todas as linhas relevantes das tabelas e as armazenam em uma única lista por tabela
def tabela_lista(linhas_tabelas, info_tabelas):

    # Lista (1) de listas (2). Em (1) cada elemento é uma tabela e em (2) cada elemento é uma linha da tabela
    lista_tabelas = [ [] for i in range(len(info_tabelas)) ]
    
    return (lista_tabelas)

# Função principal do código
def Raspagem():

    # Lista que contém em cada elemento informações sobre cada linha da tabela. Cada elemento é outra lista
    # que contém o índice da sua posição na tabela e a tag para cada item da linha ser encontrado, respectivamente.
    # O primeiro elemento da lista mãe refere-se ao título, o segundo ao nome das colunas e o restante as demais linhas.
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

    # Similar a info_tabela1, porém, com dois tipos de listas: uma com dois e outra com três itens.
    # Quando há três itens, o segundo refere-se a tag da primeira coluna das linhas de dados enquanto o terceiro é a tag das outras colunas
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
                linhas_tabelas[linha[0]] = Armazena_linha_tabela(linhas_tabelas[linha[0]], linha[1])
            else:
                linhas_tabelas[linha[0]] = Armazena_linha_tabela2(linhas_tabelas[linha[0]], linha[1], linha[2])

    return (info_tabelas, linhas_tabelas)