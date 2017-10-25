import json
from difflib import get_close_matches


def display(definitions):
    """
    Display the definitions
    :param definitions:
    :return:
    """
    for definition, index in zip(definitions, range(1, len(definitions) + 1)):
        print(str(index) + ': ' + definition)


def lookup(word):
    """
    Look up a word in the dictionary
    :param word:
    :return:
    """
    # Load data
    data = json.load(open('data.json'))

    if word in data:
        display(data[word])
    elif word.lower() in data:
        display(data[word])
    elif len(get_close_matches(word, data.keys())) > 0:
        closest_word = get_close_matches(word, data.keys())[0]
        answer = input("Did you mean '%s' instead? [y/n]" % closest_word)

        if answer == 'y':
            display(data[closest_word])
            return
    else:
        print("No definition available.")