# Globartigos

## Descrição

Este é um projeto que utiliza Django Templates. O objetivo é criar um site para publicação e gerenciamento de artigos.

## Instalação

Para instalar o projeto, siga os seguintes passos:

1. Clone o repositório
2. Crie um ambiente virtual `python -m venv venv`
3. Ative o ambiente virtual `venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (Linux)
4. Instale as dependências `make install`
5. Execute as migrações `make migrate`
6. Execute os testes `make test`
7. Crie um super usuário `make superuser`
8. Execute o servidor `make run`
9. Acesse o site em `http://localhost:8000/admin/` para fazer login com o super usuário criado
10. Acesse o site em `http://localhost:8000/` para ver o site

## Comportamentos

```feature
Eu como um usuário não autenticado
Vejo apenas artigos publicados sem controle de acesso.

Eu como um usuário autenticado
Posso pertencer a um grupo ou não
Vejo artigos de acordo com o grupo que pertenço.

Eu como um artigo
Posso estar ativo ou não
Posso pertencer a um grupo ou não
Posso estar em destaque ou não
Possuo uma contagem de acessos
Estou atrelado a uma categoria
```

## Requisitos

- [x] Menu lateral, contendo a lista de todas as categorias cadastradas na aplicação, com abertura através de botão;
- [x] Busca, com lista de categorias, permitindo a consulta em todos os artigos ou apenas na categoria selecionada;
- [x] Banner com os artigos em destaque, sendo apresentados em um slider;
- [x] Lista com os 3 artigos mais acessados;
- [x] Lista de artigos, ordenada por data de publicação;
- [x] Lista de artigos da editoria selecionada, ordenada por data de publicação;
- [x] Lista de artigos encontrados, com paginação;
- [x] Página contendo as informações do artigo selecionado;
- [x] Caso o usuário não tenha acesso ao conteúdo, deve mostrar uma mensagem de acesso negado.
- [x] Deve exibir apenas artigos que o usuário tenha permissão para acessar.

## Considerações

1. Apenas artigos com o `is_active=True` serão mostrados no site, então se o artigo não estiver ativo, ele não será mostrado.
2. Apenas artigos com o `is_highlighted=True` serão mostrados no slider, então se o artigo não estiver em destaque, ele não será mostrado.
3. Apenas categorias com o `is_active=True` serão mostradas no site, então se a categoria não estiver ativa, ela não será mostrada.
4. Em todos esses casos, no admin temos uma action para ativar/desativar os objetos.
