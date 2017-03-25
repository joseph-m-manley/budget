#!/usr/bin/env python3

from iohelpers import *
from listhelpers import *


def dict_of_sets(d):
    return {k: set(v) for k, v in d.items()}


def dict_of_lists(d):
    return {k: list(v) for k, v in d.items()}


def assign_keys(phrase, category_dict):
    print('\n%s' % phrase)
    key = phrase
    if len(key) > 15:
        x = input('Assign a key? ').upper()
        if x not in ('Y', 'Q', 'N', ''):
            key = x
        elif x == 'Y':
            key = input('Key: ').upper()

    x = input('What category does this belong in? ').upper()
    if x == 'Q':
        raise Exception()
    if x == '':
        return
    elif x in category_dict:
        category_dict[x].add(key)
    else:
        category_dict[x] = {key}


def categorize(phrases, categories):
    result = dict_of_sets(categories)
    known_words = set(flatten(result.values()))
    unknown_phrases = filter_duplicates(phrases, known_words)

    try:
        for phrase in unknown_phrases:
            if not contains_any(phrase, known_words):
                known_words.add(phrase)
                assign_keys(phrase, result)

    finally:
        return dict_of_lists(result)


def main():
    config = get_config()
    noise = get_noise(config['noise'])
    existing_categories = get_json(config['categories'])

    raw_phrases = get_column(config['csvfilepath'], config['column'])
    normalized_phrases = filter_noise(raw_phrases, noise)

    categorized = categorize(normalized_phrases, existing_categories)

    if input('Do you want to save? Y or N: ').upper() == 'Y':
        save_jsn(categorized, config['categories'])


if __name__ == '__main__':
    main()
