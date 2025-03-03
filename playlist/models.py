"""
Define os modelos principais da aplicação Movielist.
Esses modelos representam os filmes e as listas de reprodução (playlists)
que serão utilizados na aplicação.
"""

from django.db import models

class Movie(models.Model):
    """
    Modelo que representa um filme.
    Contém informações básicas como título, ano, diretor, sinopse e URL do poster.
    """
    imdb_id = models.CharField(max_length=20, unique=True)  # Identificador único do IMDb
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=10)
    director = models.CharField(max_length=255, blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    poster = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title  # Retorna o título do filme 

class Playlist(models.Model):
    """
    Modelo que representa uma playlist de filmes.
    Pode ser do tipo 'watchlist' (para assistir) ou 'recommended' (filmes curtidos/recomendados).
    """
    PLAYLIST_TYPES = (
        ('watchlist', 'Watchlist'),
        ('recommended', 'Recommended'),
    )
    name = models.CharField(max_length=100)
    playlist_type = models.CharField(max_length=20, choices=PLAYLIST_TYPES)
    movies = models.ManyToManyField(Movie, blank=True)

    def __str__(self):
        return f"{self.name} ({self.playlist_type})"  # Representação que inclui o nome e o tipo da playlist
