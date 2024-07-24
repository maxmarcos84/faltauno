from django.urls import path
from .views import CreatePlayerView, GetPlayersByUserView, getSportsView, GetSkillsBySport

urlpatterns = [
    path('player/', CreatePlayerView.as_view(), name='create_player'),
    path('players/<int:user_id>', GetPlayersByUserView.as_view(), name='get_players'),
    path('sports/', getSportsView.as_view(), name='get_sports'),
    path('skills/', GetSkillsBySport.as_view(), name='get_skills')
]