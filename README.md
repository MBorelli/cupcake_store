# Loja de Cupcakes Gourmet

## Sobre o Projeto

Este projeto é uma aplicação web simples para uma loja de cupcakes gourmet, desenvolvida em Python utilizando o framework Flask. O objetivo é permitir que usuários visualizem cupcakes, adicionem ao carrinho, finalizem pedidos e que um administrador possa gerenciar os pedidos conforme Situação-problema 1 de Projeto Integrador Transdisciplinar.

---

## Estrutura do Projeto

```plaintext
cupcake_store/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── img/
│   │       ├── redvelvet.jpg
│   │       └── chocolate.jpg
│   └── templates/
│       ├── base.html
│       ├── vitrine.html
│       ├── carrinho.html
│       ├── finalizar_pedido.html
│       ├── pedido.html
│       ├── login.html
│       └── admin.html
├── run.py
└── requirements.txt
```

---

## Processo de Desenvolvimento

1. __Planejamento__\
Definição das funcionalidades principais: vitrine, carrinho, pedidos, login/admin.\
Escolha do framework Flask pela simplicidade e rapidez no desenvolvimento.
2. __Configuração Inicial__\
Criação da estrutura de pastas e arquivos.\
Configuração do ambiente virtual Python.
3. __Modelagem__\
Definição dos modelos de dados (cupcakes, pedidos, usuários).\
Implementação do banco de dados SQLite para persistência simples.
4. __Desenvolvimento Backend__\
Criação das rotas principais no Flask (vitrine, carrinho, finalizar pedido, admin).\
Implementação da lógica de negócio em views.py e models.py.
5. __Desenvolvimento Frontend__\
Criação dos templates HTML com Jinja2.\
Adição de CSS para estilização básica.\
Inclusão de imagens ilustrativas dos cupcakes.
6. __Testes Locais__\
Testes manuais das funcionalidades.\
Ajustes de layout e correção de bugs.
7. __Documentação__\
Criação deste arquivo README com instruções detalhadas.

## Como Rodar o Projeto
### 1. __Pré-requisitos__
Python 3.x instalado (Download Python)\
pip instalado (geralmente já vem com o Python)\
(Opcional) Ambiente virtual Python
### 2. __Instale as Dependências__
No terminal, navegue até a pasta do projeto e execute:

~~~ bash
pip install -r requirements.txt
~~~

### 3. __Configure o Banco de Dados__
O projeto já está configurado para criar o banco SQLite automaticamente na primeira execução.

### 4. __Execute a Aplicação__
No terminal, ainda na pasta do projeto, rode:
~~~
python run.py
~~~
A aplicação estará disponível em:<http://localhost:5000>

### 5. __Acesse como Usuário ou Admin__
Usuário: pode navegar pela vitrine, adicionar cupcakes ao carrinho e finalizar pedidos.\
Admin: acesse /login para entrar como administrador (usuário e senha padrão definidos no código).

## __Observações Finais__
As imagens dos cupcakes estão em app/static/img/. Você pode substituir por outras imagens se desejar.\
O CSS pode ser customizado em app/static/css/style.css.\
Para adicionar mais cupcakes ou alterar preços, edite o arquivo models.py ou adicione via interface admin (se implementado).
