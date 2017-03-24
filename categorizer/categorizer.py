#!/usr/bin/env python3

from iohelpers import *
from reghelpers import *


def get_input(message, options=('Y', 'N', 'Q')):
    x = None
    message += ' '
    message += ', '.join(options[:-1])
    message += ' or %s: ' % options[-1]
    while x not in options:
        x = input(message).upper()
    return x


def categorize(words, categories=dict()):
    working = {k: set(v) for k, v in categories.items()}

    for word in words:
        print(word)
        x = input('What category does this belong in? ').upper()
        if x == 'Q':
            break
        elif x in working:
            working[x].add(word)
        else:
            working[x] = {word}

    return {k: list(v) for k, v in working.items()}


def flatten(list_of_lists):
    return [item for _list in list_of_lists for item in _list]


def preprocess(words, noise, duplicates):
    normalized_words = filter_noise(words, set(noise))
    return filter_duplicates(normalized_words, set(duplicates))


def main():
    config = get_config()
    categories = get_categories(config['categories'])
    new_words = get_column(config['csvfilepath'], config['column'])

    known_words = flatten(categories.values())
    unknown_words = preprocess(new_words, config['noise'], known_words)
    categorized = categorize(unknown_words, categories)

    if get_input('Do you want to save?') == 'Y':
        save_jsn(categorized, categorized)


if __name__ == '__main__':
    main()
