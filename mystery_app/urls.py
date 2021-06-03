from django.urls import path
from mystery_app.views import index, show_five_words, end_game

urlpatterns = [
    path('', index, name='index'),
    path('play', show_five_words, name='play'),
    #path('play', GuessCreateView, name='play'),
    #path('end/<int:pk>', end_game, name='end'),
    path('end', end_game, name='end')
]
