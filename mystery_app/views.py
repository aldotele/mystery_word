from django.shortcuts import render
from mystery_app.round_package.round import Round


def index(request):
    return render(request, 'index.html')


def play_round(request):
    random_input_file = Round.select_random_file()[0]  # random input file extracted
    new_round = Round(random_input_file)
    context = {}  # building context variable
    i = 0
    for hint in Round.hints:
        key = "option" + str(i)  # option0, option1, option2, etc. will be the keys
        context[key] = hint  # the hints will be values
        i += 1
    context['word'] = Round.word
    #print(context)

    return render(request, 'new_round.html', context)


def end_game(request):  # currently NOT used
    guess = request.POST.get('guess', '').upper().strip()
    winning_word = Round.word.upper().strip()
    context = dict()
    context['hints'] = Round.hints
    context['guess'] = guess
    context['word'] = winning_word
    if guess == winning_word:
        context['result'] = 'YOU WON !'
    else:
        context['result'] = 'YOU LOST :('

    return render(request, 'end.html', context)


def index_instructions(request):  # currently NOT used
    return render(request, 'index_instructions.html')


"""
class GuessCreateView(CreateView):
    #print('here')
    model = Guess
    fields = ['word']
    template_name = 'show_words.html'

    def get_success_url(self):
        return reverse('end', args=[self.object.pk])
"""