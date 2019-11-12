# Documentação

## Comentários

- Ver o código fonte da página (CTRL + U no Google Chrome) é bastante importante para facilitar o encontro das informações que se busca em um site. Porém, aparentemente, ela não mostra o texto de forma correta e não contém todas as classes utilizadas pelo CSS. Para isso, recomenda-se utilizar a aba Elements presente no Chrome DevTools (CTRL + SHIFT + I);
- Depois de usar o método .select() num objeto da classe bs4.BeautifulSoup, ela o transforma numa lista. Isso impede que sejam usados outros métodos interessates das classes do Beaufiul Soup. Portanto, recomenda-se usar o método .find_all() que tem o mesmo resultado, porém, mantém o objeto como uma classe do Beautiful Soup;
- Uma grande dificuldade encontrada foi a falta de padronização do formato das tabelas. A primeira tabela tem somente duas tags distintas: a primeira é 'b' para o título e a segundo é 'font'. Porém, quando tentou-se usar a mesma função para as tabelas 2 e 3, descobriu-se que as tabelas estavam em formatos diferentes. Para solucionar o problema, foi feita outra função que aceita duas tags e mescla o resultado final;

## Links utilizados

- [Artigo - aprendendo sobre web scraping](https://imasters.com.br/back-end/aprendendo-sobre-web-scraping-em-python-utilizando-beautifulsoup)