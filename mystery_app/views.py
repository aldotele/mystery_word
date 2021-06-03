from django.shortcuts import render
from django.http import HttpResponse
from mystery_conf.settings import BASE_DIR
import os
from .models import Guess
from django.views.generic import CreateView
from django.urls import reverse
from mystery_app.round_package.round import INPUT_FILE_TEST, Round


def index(request):
    return render(request, 'index.html')


def index_instructions(request):
    return render(request, 'index_instructions.html')


def play_round(request):
    # create round with test input file
    new_round = Round(INPUT_FILE_TEST)
    context = {}
    i = 0
    for hint in new_round.info['hints']:
        key = "option" + str(i)
        context[key] = hint
        i += 1
    #print(context)

    return render(request, 'round.html', context)


def end_game(request):
    guess = request.POST.get('guess', '')
    context = Round.info
    context['guess'] = guess.upper()
    if guess.upper().strip() == context['word'].upper():
        context['result'] = 'YOU WON !'
    else:
        context['result'] = 'YOU LOST :('
    print(context)
    # if request.POST.get('guess', ''):
    #     g = request.POST.get('guess')
    #     print(g)
    #     context['guess'] = g

    return render(request, 'end.html', context)


"""
class GuessCreateView(CreateView):
    #print('here')
    model = Guess
    fields = ['word']
    template_name = 'show_words.html'

    def get_success_url(self):
        return reverse('end', args=[self.object.pk])
"""