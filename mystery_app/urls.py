from django.urls import path
from mystery_app.views import index, play_round, index_instructions

urlpatterns = [
    path('', index, name='index'),
    path('instructions/', index_instructions, name='index_instructions'),
    path('play/', play_round, name='play'),
]
