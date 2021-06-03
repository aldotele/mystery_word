from django.urls import path
from mystery_app.views import index, play_round, end_game, index_instructions

urlpatterns = [
    path('', index, name='index'),
    path('instructions', index_instructions, name='index_instructions'),
    path('play', play_round, name='play'),
    #path('play', GuessCreateView, name='play'),
    #path('end/<int:pk>', end_game, name='end'),
    path('end', end_game, name='end')
]
