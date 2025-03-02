from django.db import models

class Movie(models.Model):
    imdb_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=10)
    director = models.CharField(max_length=255, blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    poster = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Playlist(models.Model):
    PLAYLIST_TYPES = (
        ('watchlist', 'Watchlist'),
        ('recommended', 'Recommended'),
    )
    name = models.CharField(max_length=100)
    playlist_type = models.CharField(max_length=20, choices=PLAYLIST_TYPES)
    movies = models.ManyToManyField(Movie, blank=True)

    def __str__(self):
        return f"{self.name} ({self.playlist_type})"
