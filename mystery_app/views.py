from django.shortcuts import render
from mystery_app.round_package.round import Round, current_round


def index(request):
    return render(request, 'index.html')


def index_instructions(request):
    return render(request, 'index_instructions.html')


def play_round(request):
    #new_round = Round()
    random_input_file = Round.select_random_file()[0]
    current_round.info = Round.parse_input_file(random_input_file)
    print(current_round.info)
    context = {}  # building context variable
    i = 0
    for hint in current_round.info['hints']:
        key = "option" + str(i)  # option0, option1, option2, etc. will be the keys
        context[key] = hint  # the hints will be values
        i += 1
    #print(context)

    return render(request, 'round.html', context)


def end_game(request):
    print(current_round.info)
    guess = request.POST.get('guess', '').upper().strip()
    winning_word = current_round.info['word'].upper().strip()
    context = dict()
    context['hints'] = current_round.info['hints']
    context['guess'] = guess
    context['word'] = winning_word
    if guess == winning_word:
        context['result'] = 'YOU WON !'
    else:
        context['result'] = 'YOU LOST :('

    return render(request, 'end.html', context)

    # context['guess'] = guess.upper()  # adding the guess to the current round information
    # if guess.upper().strip() == context['word'].upper():
    #     context['result'] = 'YOU WON !'
    # else:
    #     context['result'] = 'YOU LOST :('
    # print(context)
    # current_round.info = {}


"""
class GuessCreateView(CreateView):
    #print('here')
    model = Guess
    fields = ['word']
    template_name = 'show_words.html'

    def get_success_url(self):
        return reverse('end', args=[self.object.pk])
"""