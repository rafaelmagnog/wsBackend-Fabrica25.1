from django.shortcuts import render, redirect, get_object_or_404
import requests
from django.contrib import messages
from .models import Playlist, Movie
from django.conf import settings

def main_menu(request):
    return render(request, 'main_menu.html')

def playlist_detail(request, playlist_type):
    playlist = get_object_or_404(Playlist, playlist_type=playlist_type)
    return render(request, 'playlist_detail.html', {'playlist': playlist})

def search_movies(request):
    query = request.GET.get('query', '')
    search_results = []
    if query:
        omdb_api_key = settings.OMDB_API_KEY
        search_url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&s={query}&type=movie"
        search_response = requests.get(search_url)
        if search_response.status_code == 200:
            search_data = search_response.json()
            if search_data.get('Response') == 'True':
                # Para cada filme encontrado, buscar detalhes
                for movie in search_data['Search']:
                    detail_url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&i={movie['imdbID']}&plot=short"
                    detail_response = requests.get(detail_url)
                    if detail_response.status_code == 200:
                        detail_data = detail_response.json()
                        if detail_data.get('Response') == 'True':
                            search_results.append({
                                'title': detail_data.get('Title'),
                                'year': detail_data.get('Year'),
                                'director': detail_data.get('Director'),
                                'plot': detail_data.get('Plot'),
                                'poster': detail_data.get('Poster'),
                                'imdb_id': detail_data.get('imdbID')
                            })
                    else:
                        messages.error(request, "Erro ao buscar detalhes do filme.")
            else:
                messages.info(request, "Nenhum filme encontrado para a sua pesquisa.")
        else:
            messages.error(request, "Erro na conexão com a OMDb API.")
    return render(request, 'search.html', {'query': query, 'search_results': search_results})

def movie_detail(request, imdb_id):
    omdb_api_key = settings.OMDB_API_KEY
    detail_url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&i={imdb_id}&plot=full"
    try:
        response = requests.get(detail_url)
        response.raise_for_status()
        data = response.json()
        if data.get('Response') == 'True':
            movie = {
                'title': data.get('Title'),
                'year': data.get('Year'),
                'director': data.get('Director'),
                'plot': data.get('Plot'),
                'poster': data.get('Poster'),
                'imdb_id': data.get('imdbID')
            }
        else:
            messages.error(request, "Filme não encontrado na OMDb API.")
            return redirect('main_menu')
    except requests.exceptions.RequestException as e:
        messages.error(request, f"Erro na conexão com a OMDb API: {str(e)}")
        return redirect('main_menu')
    
    return render(request, 'movie_detail.html', {'movie': movie})

def add_movie(request, playlist_type):
    if request.method == "POST":
        imdb_id = request.POST.get('imdb_id')
        omdb_api_key = settings.OMDB_API_KEY
        url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&i={imdb_id}&plot=full"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data.get('Response') == 'True':
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
                playlist = get_object_or_404(Playlist, playlist_type=playlist_type)
                playlist.movies.add(movie)
                messages.success(request, f"{movie.title} adicionado à {playlist.name}")
            else:
                messages.error(request, "Filme não encontrado na OMDb API.")
        except requests.exceptions.RequestException as e:
            messages.error(request, f"Erro na conexão com a OMDb API: {str(e)}")
    return redirect('playlist_detail', playlist_type=playlist_type)

def remove_movie(request, playlist_id, movie_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == "POST":
        playlist.movies.remove(movie)
        messages.success(request, f"{movie.title} removido de {playlist.name}")
    return redirect('playlist_detail', playlist_type=playlist.playlist_type)
