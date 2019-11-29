from raspagem import Raspagem
from salvadados import SalvaDados

# Definição do local onde são armazenados os arquivos .csv
local = r"C:\Dados_BIG"

lista_tabelas = Raspagem()

SalvaDados(lista_tabelas, local)