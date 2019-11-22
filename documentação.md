# Documentação

## Comentários

### raspagem.py

- Ver o código fonte da página (CTRL + U no Google Chrome) é bastante importante para facilitar o encontro das informações que se busca em um site. Porém, aparentemente, ela não mostra o texto de forma correta e não contém todas as classes utilizadas pelo CSS. Para isso, recomenda-se utilizar a aba Elements presente no Chrome DevTools (CTRL + SHIFT + I);
- Depois de usar o método .select() num objeto da classe bs4.BeautifulSoup, ela o transforma numa lista. Isso impede que sejam usados outros métodos interessates das classes do Beaufiul Soup. Portanto, recomenda-se usar o método .find_all() que tem o mesmo resultado, porém, mantém o objeto como uma classe do Beautiful Soup;
- Uma grande dificuldade encontrada foi a falta de padronização do formato das tabelas. A primeira tabela tem somente duas tags distintas: a primeira é 'b' para o título e a segundo é 'font'. Porém, quando tentou-se usar a mesma função para as tabelas 2 e 3, descobriu-se que as tabelas estavam em formatos diferentes. Para solucionar o problema, foi feita outra função que aceita duas tags e mescla o resultado final;

### xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

- Inicialmente, para trocar as vírgulas por pontos, foi utilizado o código abaixo:
```python
for linha in tabela1:
    for item in tabela1:
        item = item.replace(",", ".")
```
Porém, percebeu-se que somente a variável item era alterada; a variável a qual ela se referia continuava intacta. A solução encontrada foi usar loops com range do tamanho das listas e usar os índices para acessar as listas diretamente.

## Links utilizados

- [Artigo - aprendendo sobre web scraping](https://imasters.com.br/back-end/aprendendo-sobre-web-scraping-em-python-utilizando-beautifulsoup)