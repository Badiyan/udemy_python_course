import json
from difflib import get_close_matches

FILE_NAME = 'data.json'
data = json.load(open(FILE_NAME))

def get_meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        suggestion = get_close_matches(word,data.keys())[0]
        dialog = input(f'Did u mean {suggestion} instead?  y/n : ')
        if dialog == 'y':
            return data[suggestion]
        elif dialog == 'n':
            return f'The word {word} doesn\'t exist - recheck it'
        else:
            return f'{dialog} is not understandable answer '
    else:
        return f'THe word {word} doesn\'t exist. Recheck the inputed value or try another word'

def print_output():
    output = get_meaning(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

def print_with_borders(text:str):
    text_len = len(text) + 4
    print('*' * text_len)
    print('* ' + text + ' *')
    print('*' * text_len)


if __name__ == '__main__':
    print_with_borders('The simple tesaurus programm')
    run = 1
    while run != 0:
        word = input('Enter word: ')
        print_output()
        exit_ask = input('Exit? y/n: ')
        if exit_ask == 'y':
            run = 0
        elif exit_ask == 'n':
            run = 1
        else:
            print('Not understand answer - write y or n only')
            run = 1