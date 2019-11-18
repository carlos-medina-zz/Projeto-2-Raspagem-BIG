from raspagem import Raspagem
import numpy as np
import pandas as pd

info_tabelas, linhas_tabelas = Raspagem()

a = [1, 2, 3]
b = [4, 5, 6]

lista = [a, b]

print(lista)


'''
lista_tabelas = [ [] for i in range(3) ]

lista_tabelas[0].append("casa")
lista_tabelas[0].append("nossa")
print(lista_tabelas[0])



for info_tabela in info_tabelas:
    contador_tabela = 0

    for linha in info_tabela:
        contador_linha = 0
        
        for item in linhas_tabelas[linha[0]]:
            lista_tabelas[contador_tabela][contador_linha].append(item)

        contador_linha += 1

    contador_tabela += 1
'''