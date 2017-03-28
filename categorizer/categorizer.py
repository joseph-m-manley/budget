#!/usr/bin/env python3

import helpers.iohelpers as iohelpers
import helpers.collectionUtilities as util


def add_category(category, value_to_add, categories):
    if category in categories:
        categories[category].add(value_to_add)
    else:
        categories[category] = {value_to_add}


def ask_for_key(phrase):
    print('\n%s' % phrase)
    key = phrase
    if len(key) > 15:
        x = input('Assign a key? ').upper()
        if x not in ('Y', 'Q', 'N', ''):
            key = x
        elif x == 'Y':
            key = input('Key: ').upper()
    return key


def merge_categories(phrases, categories):
    merged = util.dict_of_sets(categories)
    known_words = set(util.flatten(merged.values()))
    unknown_phrases = util.filter_duplicates(phrases, known_words)

    for phrase in unknown_phrases:
        if not util.contains_any(phrase, known_words):
            key = ask_for_key(phrase)
            known_words.add(key)

            category = input('What category does this belong in? ').upper()
            if category == 'Q':
                break  # quit
            elif category == '':
                continue  # skip this item

            add_category(category, key, merged)

    return util.dict_of_lists(merged)


def categorize(config):
    noise = iohelpers.get_noise(config['noise'])
    existing_categories = iohelpers.get_json(config['categories'])

    raw_phrases = iohelpers.get_column(config['csvfilepath'], config['column'])
    normalized_phrases = util.filter_noise_from_words(raw_phrases, noise)

    return merge_categories(normalized_phrases, existing_categories)


def main():
    config = iohelpers.get_config()
    categorized = categorize(config)

    if input('Do you want to save? Y or N: ').upper() == 'Y':
        save_jsn(categorized, config['categories'])


if __name__ == '__main__':
    main()
