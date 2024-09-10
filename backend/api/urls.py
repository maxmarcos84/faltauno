from django.urls import path
from .views import (
    CreatePlayerView, 
    UpdatePlayerView, 
    GetPlayersByUserView, 
    getSportsView, 
    GetSkillsBySport,
    SkillsRatingCreateView,
    SkillRatingUpdateView,
    GetSkillsByUser)

urlpatterns = [
    path('player/', CreatePlayerView.as_view(), name='create_player'),
    path('player/update/<pk>/', UpdatePlayerView.as_view(), name='update_player'),
    path('players/<int:user_id>', GetPlayersByUserView.as_view(), name='get_players'),
    path('sports/', getSportsView.as_view(), name='get_sports'),
    path('skills/<int:sport_id>', GetSkillsBySport.as_view(), name='get_skills'),
    path('skill_rating_create/', SkillsRatingCreateView.as_view(), name='rating_skill_create'),
    path('skill_rating_update/<pk>/', SkillRatingUpdateView.as_view(), name='rating_skill_update'),
    path('player_skills/<int:player_id>/', GetSkillsByUser.as_view(), name='get_player_skills')
]