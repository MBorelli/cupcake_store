# Loja de Cupcakes Gourmet

## Sobre o Projeto

Este projeto é uma aplicação web simples para uma loja de cupcakes gourmet, desenvolvida em Python utilizando o framework Flask. O objetivo é permitir que usuários visualizem cupcakes, adicionem ao carrinho, finalizem pedidos e que um administrador possa gerenciar os pedidos.

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

Processo de Desenvolvimento
Planejamento
Definição das funcionalidades principais: vitrine, carrinho, pedidos, login/admin.
Escolha do framework Flask pela simplicidade e rapidez no desenvolvimento.
Configuração Inicial
Criação da estrutura de pastas e arquivos.
Configuração do ambiente virtual Python.
Modelagem
Definição dos modelos de dados (cupcakes, pedidos, usuários).
Implementação do banco de dados SQLite para persistência simples.
Desenvolvimento Backend
Criação das rotas principais no Flask (vitrine, carrinho, finalizar pedido, admin).
Implementação da lógica de negócio em views.py e models.py.
Desenvolvimento Frontend
Criação dos templates HTML com Jinja2.
Adição de CSS para estilização básica.
Inclusão de imagens ilustrativas dos cupcakes.
Testes Locais
Testes manuais das funcionalidades.
Ajustes de layout e correção de bugs.
Documentação
Criação deste arquivo README com instruções detalhadas.
Como Rodar o Projeto
1. Pré-requisitos
Python 3.x instalado (Download Python)
pip instalado (geralmente já vem com o Python)
(Opcional) Ambiente virtual Python
2. Instale as Dependências
No terminal, navegue até a pasta do projeto e execute: