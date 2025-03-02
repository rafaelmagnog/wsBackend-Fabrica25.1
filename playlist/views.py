from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from .models import Playlist, Movie

# Create your views here.

def playlist_view(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlist.html', {'playlists': playlists})

def add_movie(request, playlist_id):
    if request.method == "POST":
        imdb_id = request.POST.get('imdb_id')
        # Chave da OMDb API – configurar a propria key da OMDb
        omdb_api_key = "a07e6021"
        url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&i={imdb_id}&plot=full"
        response = requests.get(url)
        data = response.json()
        if data.get('Response') == 'True':
            # Cria ou atualiza o filme no banco de dados
            movie, created = Movie.objects.get_or_create(
                imdb_id=imdb_id,
                defaults={
                    'title': data.get('Title'),
                    'year': data.get('Year'),
                    'director': data.get('Director'),
                    'plot': data.get('Plot'),
                    'poster': data.get('Poster'),
                }
            )
            try:
                playlist = Playlist.objects.get(id=playlist_id)
                playlist.movies.add(movie)
                messages.success(request, f"{movie.title} adicionado à playlist.")
            except Playlist.DoesNotExist:
                messages.error(request, "Playlist não encontrada.")
        else:
            messages.error(request, "Filme não encontrado na OMDb API.")
    return redirect('playlist_view')
