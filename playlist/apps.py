"""
Configuração do aplicativo 'playlist'.
Este módulo utiliza o sinal post_migrate para garantir que playlists padrão
sejam criadas após as migrações, evitando que o sistema fique sem listas iniciais.
"""

from django.apps import AppConfig
from django.db.models.signals import post_migrate

class PlaylistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playlist'

    def ready(self):
        # Importa o modelo Playlist somente quando o aplicativo estiver pronto
        from .models import Playlist

        def create_default_playlists(sender, **kwargs):
            """
            Função que cria playlists padrão se nenhuma playlist existir.
            Garante que o usuário tenha uma 'watchlist' e uma lista de filmes 'liked' logo após as migrações.
            """
            if not Playlist.objects.exists():
                Playlist.objects.create(
                    name="My Watchlist",
                    playlist_type="watchlist"
                )
                Playlist.objects.create(
                    name="Liked Movies",
                    playlist_type="recommended"
                )

        # Conecta a função create_default_playlists ao sinal post_migrate para ser executada após cada migração
        post_migrate.connect(create_default_playlists, sender=self)
