from django.shortcuts import render
from mystery_app.round_package import helper
from .models import Round


def index(request):
    return render(request, 'index.html')


def play_round(request):
    r = Round.objects.order_by('?').first()  # getting a random round
    context = {"hint1": r.hint_1.upper(),
               "hint2": r.hint_2.upper(),
               "hint3": r.hint_3.upper(),
               "hint4": r.hint_4.upper(),
               "hint5": r.hint_5.upper(),
               "solution": helper.decode_word(r.solution)}
    return render(request, 'new_round.html', context)


def index_instructions(request):  # currently NOT used
    return render(request, 'index_instructions.html')
