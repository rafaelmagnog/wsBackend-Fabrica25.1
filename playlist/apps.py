from django.apps import AppConfig
from django.db.models.signals import post_migrate

class PlaylistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playlist'

    def ready(self):
        from .models import Playlist

        def create_default_playlists(sender, **kwargs):
            if not Playlist.objects.exists():
                Playlist.objects.create(
                    name="My Watchlist",
                    playlist_type="watchlist"
                )
                Playlist.objects.create(
                    name="Liked Movies",
                    playlist_type="recommended"
                )

        post_migrate.connect(create_default_playlists, sender=self)
