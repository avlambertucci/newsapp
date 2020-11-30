# Newsapp

## Exercicio:

Você deverá criar uma API para um portal de notícias para cadastro de notícias,
pesquisa de notícias e visualização de notícias.
No cadastro de notícias o usuário poderá informar os seguintes dados:
 Título da notícia (obrigatório);
 Texto da notícia (ilimitado e obrigatório);
 Autor (chave estrangeira para a tabela Autor e é obrigatório).
Também devem existir a opção de editar e excluir.
Na pesquisa de notícias o usuário poderá pesquisar pelas notícias cadastradas no
banco de dados. A consulta ocorrerá somente por um parâmetro. A consulta à tabela
de notícias deve ser feita nos campos título, texto e nome do autor.
Para visualizar notícias realizar a busca no banco de dados de todos os campos da
notícia e realizar a listagem destas.
Você deverá cria um banco de dados, preferencialmente em Mongo, você pode
definir a estrutura.

## Fluxo de funcionamento

### O portal de noticias contem a lista de noticias, e dois botoes (deletar e editar) para cada notícia

![](assets\cadastrando.gif)

-----------------------------------------
### Deletando uma noticias

![](assets\deletando.gif)
-----------------------------------------
### editando uma noticia

![](assets\editando.gif)
-----------------------------------------
### Buscando por título 

![](assets\buscando.gif)
