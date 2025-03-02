
# MovieList

[![Status](https://img.shields.io/badge/status-In%20Progess-orange)](README.md)
[![Language: PT-BR](https://img.shields.io/badge/Linguagem-Português-green)](README.md)
[![Language: EN](https://img.shields.io/badge/Language-English-red)](README.en.md)

**MovieList** is a web application developed in Django for managing movie lists. With it, you can add movies to your watchlist, mark movies as favorites and consult detailed information via the **API OMDb**. The application is containerized with **Docker** and uses **PostgreSQL** as its database.

This project was developed as part of a challenge from the **Software Factory Backend Workshop at UNIPÊ** (University Center of João Pessoa), an innovation center that has been proposing solutions to real problems since 2009.

---

## Index

- [Resources](#resources)
- [Technologies Used](#technologies-used)
- [Important Files](#important-files)
- [Prerequisites](#prerequisites)
- [Installation](#instalation)
  - [Running with Docker](#running-with-docker)
  - [Running without Docker (Manual)](#running-without-docker-manual)
- [Database Configuration](#database-configuration)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Project Structure](#project-structure)

---

## Resources

- **Watchlist management**: Add and remove movies from your list of movies to watch.
- **Favorites**: Mark movies as favorites for quick access.
- **Movie Search**: Search for movies via the OMDb API and get detailed information.
- **Movie Details**: View the title, year, director, plot and poster for each movie.
- **Containerization with Docker**: Facilitates deployment and development in different environments.
- **PostgreSQL database**: Efficiently stores movie and playlist information.

---

## Technologies Used

- **Language**: [Python 3.10](https://www.python.org/)
- **Framework**: [Django 5.1.6](https://docs.djangoproject.com/en/5.1/)
- **Database**: [PostgreSQL](https://www.postgresql.org/)
- **Containerization**: [Docker](https://docs.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- **Libraries**:
  - [Django REST Framework](https://www.django-rest-framework.org/)
  - [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
  - [requests](https://docs.python-requests.org/en/master/)
  - [python-dotenv](https://pypi.org/project/python-dotenv/)
  - And others listed in [requirements.txt](#important-files)

---

## Important Files

- **`.gitignore`**  
  Contains rules to ignore files that should not be versioned, such as:
  - Virtual environment folders (`venv/`, `.venv/`, etc.)
  - Python cache files (`__pycache__`, `*.pyc`, `*.pyo`)
  - Local database (`db.sqlite3`)
  - Sensitive configuration files (`.env`)
  - IDE or operating system temporary files

- **`.dockerignore`**  
  Contains rules for ignoring files when sending the context to Docker. This prevents large or sensitive files from being included in the image, such as:
  - `.git`, `venv`, `__pycache__`
  - `.env`
  - `db.sqlite3`

- **`.env`**  
  File that is **not** versioned and contains environment variables, including:
  - PostgreSQL database credentials
  - Django's `SECRET_KEY`
  - Debug settings and allowed hosts
  - OMDb API key

- **`Dockerfile`**  
  Defines how the Docker image of the Django application is built:
  - Uses the base image `python:3.10-slim`
  - Installs system dependencies and Python
  - Exposes port 8000 and runs the Django development server

- **`docker-compose.yml`**  
  Orchestrates the Docker services:
  - **web** (Django application)
  - **db** (PostgreSQL)
  - Defines volumes, ports and environment variables

- **`requirements.txt`**  
  Lists the Python dependencies required for the project:
  - `Django`, `djangorestframework`, `psycopg2-binary`, `requests`, etc.

---

## Prerequisites

To run the project, you need to have installed on your machine:

1. [Python 3.10 or higher](https://www.python.org/)
2. [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) (if you choose to run via containers)
3. [PostgreSQL](https://www.postgresql.org/) (if you choose to run manually without Docker)

---

## Installation

The application can be run in two ways:

1. **Running with Docker**  
2. **Running without Docker (Manual)**

### Running with Docker

1. **Clone the repository**:

   ```bash
   git clone https://github.com/rafaelmagnog/wsBackend-Fabrica25.1.git
   cd wsBackend-Fabrica25.1
   ```


2. **Create the `.env` file** (if it doesn't already exist) in the root of the project with the necessary settings:
   ```bash
   PG_HOST=db
   PG_PORT=5432
   PG_USER=postgres
   PG_PASSWORD=postgres
   PG_DB=movie_db

   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1,[::1]

   OMDB_API_KEY=your_omdb_api_key
   ```

3. **Start the application**:

   ```bash
   docker-compose up --build
   ```
   This command will:
   - Build the Docker image of the application.
   - Upload the database services (PostgreSQL) and the Django application.

4. **Save the migrations**  
   The `docker-compose.yml` file already includes the command to apply the migrations automatically before starting the server. If you want to run it manually:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Access the application**  
   Open your browser at [http://localhost:8000](http://localhost:8000).

#### Useful Tips with Docker

- To run the project in the background:
  ```bash
  docker-compose up -d --build
  ```
- To stop the containers:
  ```bash
  docker-compose down
  ```
- To view the logs:
  ```bash
  docker-compose logs -f
  ```
- To create a Django superuser:
  ```bash
  docker-compose exec web python manage.py createsuperuser
  ```

### Running without Docker (Manual)

If you prefer to run the application manually (for example, in a local environment with PostgreSQL already installed):

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rafaelmagnog/wsBackend-Fabrica25.1.git
   cd wsBackend-Fabrica25.1
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate # (Linux/Mac)
   # On Windows:
   # venv\Scripts\activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configure the database**:  
   Make sure you have PostgreSQL installed and running. Create a database and a user with the credentials defined in `.env`.

5. **Create the `.env` file** (if it doesn't already exist) and set the environment variables, for example:
   ```bash
   PG_HOST=localhost
   PG_PORT=5432
   PG_USER=postgres
   PG_PASSWORD=postgres
   PG_DB=movie_db

   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1,[::1]

   OMDB_API_KEY=your_omdb_api_key
   ```

6. **Apply the migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Run the application**:
   ```bash
   python manage.py runserver
   ```
   Log in at [http://127.0.0.1:8000](http://127.0.0.1:8000).

8. **(Optional) Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

---

## Database configuration

By default, the project is configured to use **PostgreSQL**. If you are using Docker, you don't need to configure it manually, as the database service is created automatically by `docker-compose.yml`. If you are running without Docker:

1. install PostgreSQL on your operating system.
2. Create a database (`movie_db`, for example).
3. Create a user and password (`postgres/postgres` or whatever you prefer).
4. Update the `.env` file with the correct credentials.

---

## Environment Variables

The `.env` file must contain essential variables for the application to work, including:

- **PostgreSQL settings**:
  ```bash
  PG_HOST=db
  PG_PORT=5432
  PG_USER=postgres
  PG_PASSWORD=postgres
  PG_DB=movie_db
  ```
- **Django settings**:
  ```bash
  SECRET_KEY=your_secret_key
  DEBUG=True
  ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
  ```
- **OMDb API key**:
  ```bash
  OMDB_API_KEY=your_omdb_api_key
  ```
**Important**: Replace `your_secret_key` and `your_omdb_api_key` with the appropriate values. Django's secret key (`SECRET_KEY`) is fundamental to the security of the application and must be unique and kept secret. The OMDb API key (`OMDB_API_KEY`) is required to perform movie searches and can be obtained by registering at [OMDb API](http://www.omdbapi.com/).

In addition to the `.env` file, check that the settings related to the API keys are loaded correctly in the code, especially when initializing the OMDb API. Use libraries such as `python-dotenv` to load environment variables from the `.env` file.


**Important**: The `.env` is listed in `.gitignore` to ensure that sensitive information is not versioned.

---

## Use

After starting the application (either via Docker or manually), you can access it:

- **Home page**: [http://localhost:8000](http://localhost:8000) (or [http://127.0.0.1:8000](http://127.0.0.1:8000) if running without Docker)
- **Admin Django**: [http://localhost:8000/admin](http://localhost:8000/admin) (if you have created a superuser)

Within the system, you can:

- **Add movies** to your list of movies to watch (Watchlist).
- **Mark movies as favorites**.
- **Search for movie information** using integration with the OMDb API.
- **View details of each movie**, including poster, plot and director.

---

## Project Structure

Below is a summary of the structure of the most important directories and files:

```bash
WSBACKEND-FABRICA25.1
├── movie_playlist
│ ├── __pycache__
│ ├── __init__.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── playlist
│ ├── __pycache__
│ ├── migrations
│ │ └── __pycache__
│ ├── static
│ │ └── playlist.css
│ ├── templates
│ │ ├── base.html
│ │ ├── main_menu.html
│ │ ├── movie_detail.html
│ │ └── playlist_detail.html
│ │ └── search.html
│ ├── __init__.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
│ └── viewsets.py
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
