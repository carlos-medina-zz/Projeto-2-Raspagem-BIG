from raspagem import Raspagem
import numpy as np
import pandas as pd

lista_tabelas = Raspagem()


tabela1 = lista_tabelas[0]

titulo_tabela1 = tabela1.pop(0)

colunas_tabela1 = tabela1.pop(0)

df = pd.DataFrame(np.array(tabela1), columns = colunas_tabela1)
print(df)