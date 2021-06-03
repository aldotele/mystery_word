import os
import random
from mystery_conf.settings import BASE_DIR

INPUT_FILES_DIR = os.path.join(BASE_DIR, 'mystery_app', 'input_files')
INPUT_FILE_TEST = ''
NUMBER_OF_FILES_AVAILABLE = 6  # currently there are 6 possible input files


class Round:
    info = None  # each time a new Round instance gets created, its info attribute will change

    def __init__(self, input_file):  # an input file name is passed to the Round instance
        Round.info = Round.parse_input_file(input_file)  # will store five hints and winning words in two keys

    @staticmethod
    def parse_input_file(input_file):
        round_info = {'hints': [], 'word': ''}
        inf = open(os.path.join(INPUT_FILES_DIR, input_file), 'r')
        lines = inf.readlines()  # store each line as one element of the same list
        for i in range(5):
            round_info['hints'].append(lines[i].strip())
        round_info['word'] = lines[-1].strip()
        inf.close()

        return round_info  # dictionary with keys hints and word

    @staticmethod
    def select_random_file():
        random_number = random.randrange(1, NUMBER_OF_FILES_AVAILABLE+1)
        file_name = 'mwtest' + str(random_number) + '.txt'
        return file_name


# if __name__ == '__main__':
    # test_input_file = 'mwtest1.txt'
    # new_round = Round(test_input_file)
    # print(new_round.info)

