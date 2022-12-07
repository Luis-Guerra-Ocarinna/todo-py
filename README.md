# todo-py
Realizado por: Luis Rosa
Objetivo: Lista de afazres com autenticação de usuário

Reference Architecture: [Bruno Rocha - CodeShow: Arquitetura Definitiva para o Projeto Web Com Python e Flask](https://www.youtube.com/watch?v=-qWySnuoaTM)

## Run:
```shell
$ pip install -r requirements.txt
$ npm i
$ npx tailwindcss \
    -i ./todo_py/blueprints/web/static/css/src/tailwind.css \
    -o ./todo_py/blueprints/web/static/css/dist/tailwind.css
$ cp .env{.example,}
$ flask run