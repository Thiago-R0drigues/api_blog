# API Blog

API REST desenvolvida com **FastAPI** para estudo e prática de desenvolvimento backend em Python.

O projeto tem como objetivo aplicar conceitos de criação de APIs, persistência de dados e integração com banco de dados utilizando **SQLAlchemy**.

## Tecnologias

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic

## Funcionalidades

* Criação de posts
* Listagem de posts
* Consulta de posts
* Atualização de posts
* Exclusão de posts
* Persistência dos dados em banco de dados

## Estrutura

```text
api_blog/
├── app/
│   ├── ...
├── requirements.txt
├── database.db
└── ...
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/Thiago-R0drigues/api_blog.git
```

Entre no diretório:

```bash
cd api_blog
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executando a API

Inicie o servidor com:

```bash
uvicorn app.main:app --reload
```

A API estará disponível localmente em:

```text
http://127.0.0.1:8000
```

## Documentação

O FastAPI disponibiliza automaticamente a documentação interativa da API.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

## Objetivo

Este projeto faz parte do meu processo de aprendizado em **desenvolvimento backend com Python**, com foco em construção de APIs REST, integração com bancos de dados e utilização do SQLAlchemy como ORM.

## Próximos passos

****

## Autor

**Thiago Rodrigues**

GitHub: [Thiago-R0drigues](https://github.com/Thiago-R0drigues)
