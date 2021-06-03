import os
from mystery_conf.settings import BASE_DIR

INPUT_FILES_DIR = os.path.join(BASE_DIR, 'mystery_app', 'input_files')
INPUT_FILE_TEST = 'mwtest.txt'


class Round:
    info = ''

    def __init__(self, input_file):
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

        return round_info


if __name__ == '__main__':
    test_input_file = 'mwtest.txt'
    new_round = Round(test_input_file)
    print(new_round.info)

