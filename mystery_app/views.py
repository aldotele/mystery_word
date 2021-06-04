from django.shortcuts import render
from mystery_app.round_package.round import Round


def index(request):
    return render(request, 'index.html')


def index_instructions(request):
    return render(request, 'index_instructions.html')


def play_round(request):
    # a random input file is extracted
    #filename = Round.select_random_file()[0]
    # create round with extracted input file
    #current_round_data = Round.parse_input_file(filename)
    #Round.info = current_round_data
    #print(Round.info)
    new_round = Round()
    context = {}  # building context variable
    i = 0
    for hint in Round.hints:
        key = "option" + str(i)  # option0, option1, option2, etc. will be the keys
        context[key] = hint  # the hints will be values
        i += 1
    #print(context)

    return render(request, 'round.html', context)


def end_game(request):
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