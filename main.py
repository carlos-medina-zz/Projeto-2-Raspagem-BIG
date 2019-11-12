from raspagem import Raspagem

info_tabelas, linhas_tabelas = Raspagem()

for info_tabela in info_tabelas:
    for linha in info_tabela:
        print(linhas_tabelas[linha[0]])