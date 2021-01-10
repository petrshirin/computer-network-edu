import os
import sys
from azure_translate import Translator


def read_file(file_name: str) -> str:
    with open(file_name, 'r') as f:
        return f.read()


if __name__ == '__main__':
    key = os.environ['SECRET_KEY']
    text = read_file('text_to_translate.txt')
    try:
        target = sys.argv[1]
        source = sys.argv[2]
        translator = Translator(key)
        print(translator.translate(text.split('\n'), target=target, source=source))

    except IndexError:
        print('Invalid params')
