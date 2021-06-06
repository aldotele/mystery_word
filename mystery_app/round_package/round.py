import os
import random
from mystery_conf.settings import BASE_DIR
from mystery_app.round_package.helper import decode_word

INPUT_FILES_DIR = os.path.join(BASE_DIR, 'mystery_app', 'input_files')
INPUT_FILE_TEST = ''
NUMBER_OF_FILES_AVAILABLE = 9  # currently there are 9 possible input files


class Round:
    # the following attributes will change each time a new Round instance gets created
    hints = []
    word = ''

    def __init__(self, input_file):
        current_round_data = Round.parse_input_file(input_file)
        Round.hints = current_round_data['hints']
        Round.word = current_round_data['word']

    @staticmethod
    def parse_input_file(input_file):  # builds a dictionary of information for current round
        round_info = {'hints': [], 'word': ''}
        inf = open(os.path.join(INPUT_FILES_DIR, input_file), 'r')
        lines = inf.readlines()  # store each line as one element of the same list
        for i in range(5):
            round_info['hints'].append(lines[i].strip())  # storing hints
        encoded_winning_word = lines[-1].strip()  # in base 64
        round_info['word'] = decode_word(encoded_winning_word)  # decoding and storing the winning word
        inf.close()

        return round_info  # dictionary with keys hints and word

    @staticmethod
    def select_random_file():
        random_number = random.randrange(1, NUMBER_OF_FILES_AVAILABLE+1)
        file_name = 'mw' + str(random_number) + '.txt'  # composing the name of the file
        return file_name, random_number

