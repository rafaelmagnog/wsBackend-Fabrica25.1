from django.contrib import admin
from .models import Movie, Playlist

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'director')
    search_fields = ('title', 'director')

class PlaylistAdmin(admin.ModelAdmin):
    filter_horizontal = ('movies',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Playlist, PlaylistAdmin)
