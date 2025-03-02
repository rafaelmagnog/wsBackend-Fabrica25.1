# Movie Playlists

Este é um projeto Django que permite aos usuários criar playlists de filmes que desejam assistir (Watchlist) e filmes que recomendam (Liked Movies). A aplicação integra a API OMDb para buscar informações detalhadas dos filmes.

## Funcionalidades

- Busca de filmes via OMDb API.
- Criação e gerenciamento de duas playlists: Watchlist e Liked Movies.
- Exibição de detalhes completos dos filmes em um layout tipo "card".
- Adição e remoção de filmes das playlists.
- CRUD completo para as entidades relacionadas (Movie e Playlist) via Django Admin e API.
- Autenticação por token para endpoints da API com Django REST Framework.

## Pré-requisitos

- Docker e Docker Compose instalados na máquina.

## Instruções para Execução

1. Clone o repositório.
2. Configure as variáveis de ambiente criando um arquivo `.env` (veja o exemplo fornecido).
3. Construa e inicie os containers Docker:
   ```bash
   docker-compose up --build
