# Documentação

## Comentários

- Ver o código fonte da página (CTRL + U no Google Chrome) é bastante importante para facilitar o encontro das informações que se busca em um site. Porém, aparentemente, ela não mostra o texto de forma correta e não contém todas as classes utilizadas pelo CSS. Para isso, recomenda-se utilizar a aba Elements presente no Chrome DevTools (CTRL + SHIFT + I);
- Depois de usar o método .select() num objeto da classe bs4.BeautifulSoup, ela o transforma numa lista. Isso impede que sejam usados outros métodos interessates das classes do Beaufiul Soup. Portanto, recomenda-se usar o método .find_all() que tem o mesmo resultado, porém, mantém o objeto como uma classe do Beautiful Soup;

## Links utilizados

- [Artigo - aprendendo sobre web scraping](https://imasters.com.br/back-end/aprendendo-sobre-web-scraping-em-python-utilizando-beautifulsoup)