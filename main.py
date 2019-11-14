from raspagem import Raspagem
import numpy as np
import pandas as pd

info_tabelas, linhas_tabelas = Raspagem()

tabela1 = []
tabela2 = []
tabela3 = []
lista_tabelas = [tabela1, tabela2, tabela3]


lista_tabelas[0][0].append("casa")

'''
for info_tabela in info_tabelas:
    contador_tabela = 0

    for linha in info_tabela:
        contador_linha = 0
        
        for item in linhas_tabelas[linha[0]]:
            lista_tabelas[contador_tabela][contador_linha].append(item)

        contador_linha += 1
    

    contador_tabela += 1
'''