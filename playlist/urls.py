from django.urls import path, include
from rest_framework import routers
from . import views, viewsets

router = routers.DefaultRouter()
router.register(r'movies', viewsets.MovieViewSet)
router.register(r'playlists', viewsets.PlaylistViewSet)

urlpatterns = [
    # Endpoints da API
    path('api/', include(router.urls)),
    # View da interface web
    path('', views.playlist_view, name='playlist_view'),
    # Rota para adicionar filme à playlist (recebe o id da playlist)
    path('add_movie/<int:playlist_id>/', views.add_movie, name='add_movie'),
]
