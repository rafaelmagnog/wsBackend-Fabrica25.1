"""
Módulo de serializers para a API.
Responsável por converter os modelos Movie e Playlist para formatos JSON e vice-versa,
facilitando a comunicação entre o backend e o frontend.
"""

from rest_framework import serializers
from .models import Movie, Playlist

class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Movie.
    Serializa todos os campos do filme.
    """
    class Meta:
        model = Movie
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Playlist.
    Inclui os filmes associados à playlist utilizando o MovieSerializer.
    """
    movies = MovieSerializer(many=True, read_only=True)
    
    class Meta:
        model = Playlist
        fields = '__all__'
