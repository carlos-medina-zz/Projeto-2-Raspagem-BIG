import numpy as np
import pandas as pd
from unicodedata import normalize
from datetime import date
import os

# Função que retorna duas listas: a primeira contém as três tabelas como dataframes
# e a segunda os títulos de cada uma das tabelas
def CriaDataframe (lista_tabelas):
    
    # Cria uma lista com 3 listas para armazenar os titulos das tabelas
    titulos_tabelas = [ [] for i in range(len(lista_tabelas))]

    # Cria uma lista com 3 listas para armazenar as labels das colunas
    colunas_tabelas = [ [] for i in range(len(lista_tabelas))]

    # Cria uma lista com 3 listas para armazenar os dataframes das tabelas
    df_list = [ [] for i in range(len(lista_tabelas))]

    # Extração, conversão e substituição de dados das tabelas
    contador_tabela = 0
    for tabela in lista_tabelas:

        # Extração do título da tabela que consta na primeira posição da lista
        titulos_tabelas[contador_tabela] = lista_tabelas[contador_tabela].pop(0)
        
        # Conversão da variável list para string extraindo o único elemento
        titulos_tabelas[contador_tabela] = titulos_tabelas[contador_tabela][0]

        # Extração das labels das colunas que consta na primeira posição da lista
        colunas_tabelas[contador_tabela] = lista_tabelas[contador_tabela].pop(0)

        # Remove todos os pontos e substitui todas as vírgulas por pontos 
        for linha in range(len(tabela)):
            for item in range(len(tabela[linha])):
                if "," in tabela[linha][item]:
                    tabela[linha][item] = tabela[linha][item].replace(",", ".")
                else:
                    tabela[linha][item] = tabela[linha][item].replace(".", "")

        # Cria os dataframes
        df_list[contador_tabela] = pd.DataFrame(np.array(tabela), columns = colunas_tabelas[contador_tabela])
        
        # Converte todos os dados numéricos que antes eram do tipo str para o tipo float
        for coluna in colunas_tabelas[contador_tabela]:
            if coluna == "Tipo":
                pass
            else:
                df_list[contador_tabela][coluna] = df_list[contador_tabela][coluna].astype(float)
        
        contador_tabela += 1

    return (df_list, titulos_tabelas)

# Cria o nome de cada uma das tabelas para ser salvo no disco
def CriaNomeArquivos(titulos_tabelas):
    
    nome_arquivos = [ [] for i in range(len(titulos_tabelas)) ]
    
    contador_nome = 0
    for titulo in titulos_tabelas:

        # Troca os espaços dos nomes por _
        nome_arquivos[contador_nome] = titulo.replace(" ", "_")

        # Substitui caracteres acentuados pelos seus equivalentes não acentudos
        nome_arquivos[contador_nome] = normalize('NFKD', nome_arquivos[contador_nome]).encode('ASCII', 'ignore').decode('ASCII')

        # Adiciona a data atual no nome do arquivo
        today = date.today()
        today = str(today)
        nome_arquivos[contador_nome] = nome_arquivos[contador_nome] + "_" + today + ".csv"

        contador_nome += 1

    return (nome_arquivos)

# Salva o dataframe em .csv somente se não existir outro com o mesmo nome, ou seja, somente caso a ação não tenha sido
# realizada no mesmo dia
def SalvaTabela (df_list, nome_arquivos, local):
    # Salva em uma lista os nomes de todos os dataframes salvos previamente em disco
    dfs_antigos = os.listdir(local)

    for indice in range(len(df_list)):
        if nome_arquivos[indice] in dfs_antigos:
            print("O dataframe {} já foi criado hoje" .format(nome_arquivos[indice]))
        else:
            nome = local + "\\" + nome_arquivos[indice]
            df_list[indice].to_csv (nome, index = None, header=True)
    
    return ()

def SalvaDados(lista_tabelas, local):
    df_list, titulos_tabelas = CriaDataframe(lista_tabelas)

    nome_arquivos = CriaNomeArquivos(titulos_tabelas)

    SalvaTabela(df_list, nome_arquivos, local)

    return()