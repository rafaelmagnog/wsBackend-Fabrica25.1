from django.apps import AppConfig

class PlaylistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playlist'

    def ready(self):
        from .models import Playlist
        if not Playlist.objects.exists():
            Playlist.objects.create(
                name="My Watchlist",
                playlist_type="watchlist"
            )
            Playlist.objects.create(
                name="Liked Movies",
                playlist_type="recommended"
            )
