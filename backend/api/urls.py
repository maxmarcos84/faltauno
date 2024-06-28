from django.urls import path
from .views import CreatePlayerView, GetPlayersByUserView

urlpatterns = [
    path('player/', CreatePlayerView.as_view(), name='create_player'),
    path('players/', GetPlayersByUserView.as_view(), name='get_players')

]