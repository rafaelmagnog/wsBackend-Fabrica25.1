
# MoviePlay

**MoviePlay** é uma aplicação web desenvolvida em **Django** para gerenciar listas de filmes. Com ela, você pode adicionar filmes à sua watchlist, marcar filmes como favoritos e consultar informações detalhadas através da **API OMDb**. A aplicação está containerizada com **Docker** e utiliza **PostgreSQL** como banco de dados.

Este projeto foi desenvolvido como parte de um desafio do **Workshop de Backend da Fábrica de Software do UNIPÊ** (Centro Universitário de João Pessoa), um núcleo de inovação que propõe soluções para problemas reais desde 2009.

---

## Índice

- [Recursos](#recursos)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Arquivos Importantes](#arquivos-importantes)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
  - [Executando com Docker](#executando-com-docker)
  - [Executando sem Docker (Manual)](#executando-sem-docker-manual)
- [Configuração do Banco de Dados](#configuração-do-banco-de-dados)
- [Variáveis de Ambiente](#variáveis-de-ambiente)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)

---

## Recursos

- **Gerenciamento de Watchlist**: Adicione e remova filmes da sua lista de filmes para assistir.
- **Favoritos**: Marque filmes como favoritos para acesso rápido.
- **Busca de Filmes**: Pesquise filmes pela API OMDb e obtenha informações detalhadas.
- **Detalhes dos Filmes**: Visualize título, ano, diretor, enredo e pôster de cada filme.
- **Containerização com Docker**: Facilita a implantação e o desenvolvimento em diferentes ambientes.
- **Banco de Dados PostgreSQL**: Armazena de forma eficiente informações de filmes e playlists.

---

## Tecnologias Utilizadas

- **Linguagem**: [Python 3.10](https://www.python.org/)
- **Framework**: [Django 5.1.6](https://docs.djangoproject.com/en/5.1/)
- **Banco de Dados**: [PostgreSQL](https://www.postgresql.org/)
- **Containerização**: [Docker](https://docs.docker.com/) e [Docker Compose](https://docs.docker.com/compose/)
- **Bibliotecas**:
  - [Django REST Framework](https://www.django-rest-framework.org/)
  - [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
  - [requests](https://docs.python-requests.org/en/master/)
  - [python-dotenv](https://pypi.org/project/python-dotenv/)
  - E outras listadas em [requirements.txt](#arquivos-importantes)

---

## Arquivos Importantes

- **`.gitignore`**  
  Contém regras para ignorar arquivos que não devem ser versionados, como:
  - Pastas de ambiente virtual (`venv/`, `.venv/`, etc.)
  - Arquivos de cache do Python (`__pycache__`, `*.pyc`, `*.pyo`)
  - Banco de dados local (`db.sqlite3`)
  - Arquivos de configuração sensíveis (`.env`)
  - Arquivos temporários de IDE ou do sistema operacional

- **`.dockerignore`**  
  Contém regras para ignorar arquivos ao enviar o contexto para o Docker. Isso evita que arquivos grandes ou sensíveis sejam incluídos na imagem, como:
  - `.git`, `venv`, `__pycache__`
  - `.env`
  - `db.sqlite3`

- **`.env`**  
  Arquivo que **não** é versionado e contém variáveis de ambiente, incluindo:
  - Credenciais do banco de dados PostgreSQL
  - `SECRET_KEY` do Django
  - Configurações de debug e hosts permitidos
  - Chave da API OMDb

- **`Dockerfile`**  
  Define como a imagem Docker da aplicação Django é construída:
  - Utiliza a imagem base `python:3.10-slim`
  - Instala dependências do sistema e Python
  - Expõe a porta 8000 e executa o servidor de desenvolvimento Django

- **`docker-compose.yml`**  
  Orquestra os serviços Docker:
  - **web** (aplicação Django)
  - **db** (PostgreSQL)
  - Define volumes, portas e variáveis de ambiente

- **`requirements.txt`**  
  Lista as dependências Python necessárias para o projeto:
  - `Django`, `djangorestframework`, `psycopg2-binary`, `requests`, etc.

---

## Pré-requisitos

Para rodar o projeto, você precisará ter instalado em sua máquina:

1. [Python 3.10 ou superior](https://www.python.org/)
2. [Docker](https://docs.docker.com/get-docker/) e [Docker Compose](https://docs.docker.com/compose/install/) (caso opte por rodar via containers)
3. [PostgreSQL](https://www.postgresql.org/) (caso opte por rodar manualmente sem Docker)

---

## Instalação

A aplicação pode ser executada de duas maneiras:

1. **Executando com Docker**  
2. **Executando sem Docker (Manual)**

### Executando com Docker

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/rafaelmagnog/movieplay.git
   cd movieplay
   ```

2. **Crie o arquivo `.env`** (caso ainda não exista) na raiz do projeto com as configurações necessárias:
   ```bash
   PG_HOST=db
   PG_PORT=5432
   PG_USER=postgres
   PG_PASSWORD=postgres
   PG_DB=movie_db

   SECRET_KEY=sua_chave_secreta
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1,[::1]

   OMDB_API_KEY=sua_chave_da_api_omdb
   ```

3. **Inicie a aplicação**:

   ```bash
   docker-compose up --build
   ```
   Esse comando irá:
   - Construir a imagem Docker da aplicação.
   - Subir os serviços de banco de dados (PostgreSQL) e da aplicação Django.

4. **Aguarde as migrações**  
   O arquivo `docker-compose.yml` já inclui o comando para aplicar as migrações automaticamente antes de iniciar o servidor. Caso queira rodar manualmente:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Acesse a aplicação**  
   Abra seu navegador em [http://localhost:8000](http://localhost:8000).

#### Dicas Úteis com Docker

- Para rodar o projeto em segundo plano:
  ```bash
  docker-compose up -d --build
  ```
- Para parar os contêineres:
  ```bash
  docker-compose down
  ```
- Para ver os logs:
  ```bash
  docker-compose logs -f
  ```
- Para criar um superusuário Django:
  ```bash
  docker-compose exec web python manage.py createsuperuser
  ```

### Executando sem Docker (Manual)

Caso prefira executar a aplicação manualmente (por exemplo, em um ambiente local com PostgreSQL já instalado):

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/rafaelmagnog/movieplay.git
   cd movieplay
   ```

2. **Crie e ative um ambiente virtual**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # (Linux/Mac)
   # No Windows:
   # venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados**:  
   Certifique-se de ter o PostgreSQL instalado e em execução. Crie um banco de dados e um usuário com as credenciais definidas no `.env`.

5. **Crie o arquivo `.env`** (se ainda não existir) e defina as variáveis de ambiente, como exemplo:
   ```bash
   PG_HOST=localhost
   PG_PORT=5432
   PG_USER=postgres
   PG_PASSWORD=postgres
   PG_DB=movie_db

   SECRET_KEY=sua_chave_secreta
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1,[::1]

   OMDB_API_KEY=sua_chave_da_api_omdb
   ```

6. **Aplique as migrações**:
   ```bash
   python manage.py migrate
   ```

7. **Execute a aplicação**:
   ```bash
   python manage.py runserver
   ```
   Acesse em [http://127.0.0.1:8000](http://127.0.0.1:8000).

8. **(Opcional) Crie um superusuário**:
   ```bash
   python manage.py createsuperuser
   ```

---

## Configuração do Banco de Dados

Por padrão, o projeto está configurado para usar **PostgreSQL**. Se estiver utilizando Docker, não é necessário configurar manualmente, pois o serviço de banco de dados é criado automaticamente pelo `docker-compose.yml`. Caso esteja executando sem Docker:

1. Instale o PostgreSQL no seu sistema operacional.
2. Crie um banco de dados (`movie_db`, por exemplo).
3. Crie um usuário e senha (`postgres/postgres` ou conforme preferir).
4. Atualize o arquivo `.env` com as credenciais corretas.

---

## Variáveis de Ambiente

O arquivo `.env` deve conter variáveis essenciais para o funcionamento da aplicação, incluindo:

- **Configurações do PostgreSQL**:
  ```bash
  PG_HOST=db
  PG_PORT=5432
  PG_USER=postgres
  PG_PASSWORD=postgres
  PG_DB=movie_db
  ```
- **Configurações do Django**:
  ```bash
  SECRET_KEY=sua_chave_secreta
  DEBUG=True
  ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
  ```
- **Chave da API OMDb**:
  ```bash
  OMDB_API_KEY=sua_chave_da_api_omdb
  ```
**Importante**: Substitua `sua_chave_secreta` e `sua_chave_da_api_omdb` pelos valores apropriados. A chave secreta do Django (`SECRET_KEY`) é fundamental para a segurança da aplicação e deve ser única e mantida em segredo. A chave da API OMDb (`OMDB_API_KEY`) é necessária para realizar buscas de filmes e pode ser obtida ao se cadastrar no [OMDb API](http://www.omdbapi.com/).

Além do arquivo `.env`, verifique se as configurações relacionadas às chaves de API estão sendo carregadas corretamente no código, especialmente ao inicializar a API OMDb. Utilize bibliotecas como `python-dotenv` para carregar variáveis de ambiente a partir do arquivo `.env`.


**Importante**: O `.env` está listado no `.gitignore` para garantir que informações sensíveis não sejam versionadas.

---

## Uso

Após iniciar a aplicação (seja via Docker ou manualmente), você pode acessar:

- **Página inicial**: [http://localhost:8000](http://localhost:8000) (ou [http://127.0.0.1:8000](http://127.0.0.1:8000) caso execute sem Docker)
- **Admin Django**: [http://localhost:8000/admin](http://localhost:8000/admin) (se tiver criado um superusuário)

Dentro do sistema, você pode:

- **Adicionar filmes** à sua lista de filmes para assistir (Watchlist).
- **Marcar filmes como favoritos**.
- **Buscar informações de filmes** usando a integração com a API OMDb.
- **Visualizar detalhes de cada filme**, incluindo pôster, enredo e diretor.

---

## Estrutura do Projeto

Abaixo está um resumo da estrutura de diretórios e arquivos mais importantes:

```bash
WSBACKEND-FABRICA25.1
├── movie_playlist
│   ├── __pycache__
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── playlist
│   ├── __pycache__
│   ├── migrations
│   │   └── __pycache__
│   ├── static
│   │   └── playlist.css
│   ├── templates
│   │   ├── base.html
│   │   ├── main_menu.html
│   │   ├── movie_detail.html
│   │   └── playlist_detail.html
│   │   └── search.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── viewsets.py
├── venv
├── .dockerignore
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── README.md
└── requirements.txt
```

---


