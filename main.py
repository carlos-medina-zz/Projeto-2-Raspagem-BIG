from raspagem import Raspagem
import numpy as np
import pandas as pd

# Função que retorna duas listas: a primeira contém as três tabelas como dataframes
# e a segunda os títulos de cada uma das tabelas
def Cria_dataframe (lista_tabelas):
    
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


lista_tabelas = Raspagem()

df_list, titulos_tabelas = Cria_dataframe(lista_tabelas)
print(df_list[0])
print(df_list[1])
print(df_list[2])