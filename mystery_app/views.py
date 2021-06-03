from django.shortcuts import render
from mystery_app.round_package.round import Round, current_round


def index(request):
    return render(request, 'index.html')


def index_instructions(request):
    return render(request, 'index_instructions.html')


def play_round(request):
    # a random input file is extracted
    filename = Round.select_random_file()
    # create round with extracted input file
    current_round.info = Round.parse_input_file(filename)
    context = {}  # building context variable
    i = 0
    for hint in current_round.info['hints']:
        key = "option" + str(i)  # option0, option1, option2, etc. will be the keys
        context[key] = hint  # the hints will be values
        i += 1
    #print(context)

    return render(request, 'round.html', context)


def end_game(request):
    guess = request.POST.get('guess', '')
    context = current_round.info  # rebuilding context from this round information
    context['guess'] = guess.upper()  # adding the guess to the current round information
    if guess.upper().strip() == context['word'].upper():
        context['result'] = 'YOU WON !'
    else:
        context['result'] = 'YOU LOST :('
    #print(context)

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