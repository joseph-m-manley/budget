#!/usr/bin/env python3

from iohelpers import *
from reghelpers import *


def categorize(words, categories=dict()):
    working = {k: set(v) for k, v in categories.items()}
    known_words = set(flatten(working.values()))

    unknown_words = filter_duplicates(words, known_words)

    for word in unknown_words:
        if word not in known_words:
            known_words.add(word)

            print('\n%s' % word)
            key = word
            if len(key) > 15:
                x = input('Assign a key? ').upper()
                if x not in ('Y', 'Q', 'N', ''):
                    key = x
                elif x == 'Y':
                    key = input('Key: ').upper()

            x = input('What category does this belong in? ').upper()
            if x == 'Q':
                break
            if x == '':
                continue
            elif x in working:
                working[x].add(key)
            else:
                working[x] = {key}

    return {k: list(v) for k, v in working.items()}


def flatten(list_of_lists):
    return [item for _list in list_of_lists for item in _list]


def main():
    config = get_config()
    noise = get_noise(config['noise'])
    existing_categories = get_json(config['categories'])

    raw_words = get_column(config['csvfilepath'], config['column'])
    normalized_words = filter_noise(raw_words, noise)

    categorized = categorize(normalized_words, existing_categories)

    if input('Do you want to save? Y or N: ').upper() == 'Y':
        save_jsn(categorized, config['categories'])


if __name__ == '__main__':
    main()
