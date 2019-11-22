from raspagem import Raspagem
import numpy as np
import pandas as pd

lista_tabelas = Raspagem()


tabela1 = lista_tabelas[0]

titulo_tabela1 = tabela1.pop(0)

colunas_tabela1 = tabela1.pop(0)

# Substitui todas as vírgulas por pontos e os pontos por vírgulas
for linha in range(len(tabela1)):
    for item in range(len(tabela1[linha])):
        if "," in tabela1[linha][item]:
            tabela1[linha][item] = tabela1[linha][item].replace(",", ".")
        else:
            tabela1[linha][item] = tabela1[linha][item].replace(".", ",")

df = pd.DataFrame(np.array(tabela1), columns = colunas_tabela1)
print(df)