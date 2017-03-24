#!/usr/bin/env python3

from iohelpers import *
from reghelpers import *


def get_input(msg, opt=['Y', 'N', 'Q']):
    x = None
    message = '{} {} or {}: '.format(msg, ', '.join(opt[:-1]), opt[-1])
    choices = opt + ['']
    while x not in choices:
        x = input(message).upper()
    return x


def ask_for_key(word):
    if len(word) < 20:
        return word
    x = get_input('Would you like to assign a key? ')
    if x != 'Y':
        return word
    else:
        return input('Key: ').upper()


def categorize(words, categories=dict()):
    working = {k: set(v) for k, v in categories.items()}
    shown = []

    for word in words:
        if word not in shown:
            shown.append(word)

            print('\n%s' % word)

            key = ask_for_key(word)

            x = input('What category does this belong in? ').upper()
            if x == 'Q':
                break
            elif x in working:
                working[x].add(key)
            else:
                working[x] = {key}

    return {k: list(v) for k, v in working.items()}


def flatten(list_of_lists):
    return [item for _list in list_of_lists for item in _list]


def preprocess(words, noise, duplicates):
    normalized_words = filter_noise(words, set(noise))
    return filter_duplicates(normalized_words, set(duplicates))


def main():
    config = get_config()
    noise = get_noise(config['noise'])
    categories = get_json(config['categories'])
    raw_words = get_column(config['csvfilepath'], config['column'])

    known_words = flatten(categories.values())
    new_words = preprocess(raw_words, noise, known_words)
    categorized = categorize(new_words, categories)

    if get_input('Do you want to save?') == 'Y':
        save_jsn(categorized, config['categories'])


if __name__ == '__main__':
    main()
