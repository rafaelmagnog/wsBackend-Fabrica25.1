"""
Módulo de viewsets para a API.
Aqui definimos as classes que permitem a criação, leitura, atualização e exclusão (CRUD)
de filmes e playlists utilizando o Django REST Framework.
"""

from rest_framework import viewsets
from .models import Movie, Playlist
from .serializers import MovieSerializer, PlaylistSerializer

class MovieViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Movie.
    Permite operações CRUD completas em filmes.
    """
    queryset = Movie.objects.all()  # Consulta todos os filmes do banco de dados
    serializer_class = MovieSerializer # Utiliza o serializer específico para filmes.


class PlaylistViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Playlist.
    Gerencia as playlists disponíveis na aplicação.
    """
    queryset = Playlist.objects.all() # Consulta todas as playlists cadastradas
    serializer_class = PlaylistSerializer # Serializa os dados de acordo com o serializer definido
