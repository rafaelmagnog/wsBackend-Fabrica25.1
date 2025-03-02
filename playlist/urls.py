from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('watchlist/', views.playlist_detail, {'playlist_type': 'watchlist'}, name='watchlist'),
    path('liked/', views.playlist_detail, {'playlist_type': 'recommended'}, name='liked'),
    path('search/', views.search_movies, name='search'),
    path('movie/<str:imdb_id>/', views.movie_detail, name='movie_detail'),  # Rota para detalhes do filme
    path('add/<str:playlist_type>/', views.add_movie, name='add_movie'),
    path('remove/<int:playlist_id>/<int:movie_id>/', views.remove_movie, name='remove_movie'),
]
