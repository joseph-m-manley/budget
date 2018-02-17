#!/usr/bin/env python3

from budget.utilities import remove_known, contains_none, filter_noise
from budget.Classes import Data, Input
from collections import OrderedDict


def add_category(categories, category, value_to_add):
    value = value_to_add.lower()
    if category in categories:
        categories[category].append(value)
    else:
        categories[category] = [value]


def flatten(list_of_lists):
    return [item for _list in list_of_lists for item in _list]


def merge_with_categories(known_categories, known_descriptions, unknown_descriptions, user=Input()):
    '''
    known_categories: dict of lists {food: [abc, xyz]} , comes from categories.json
    unknown_descriptions: a list of normalized activity descriptions that do not match any known category keys
    '''
    for unknown in unknown_descriptions:
        if contains_none(unknown, known_descriptions):
            key = user.ask_for_key(unknown)
            category = user.ask_for_category(key)
            # (key, category) = user.determine_key_and_category(unknown)

            known_descriptions.append(key)

            if category == 'Q':
                break  # quit
            elif category == '':
                continue  # skip this item

            add_category(known_categories, category, key)

    return known_categories


def categorize(descriptions, known_categories):
    '''
    descriptions: activity descriptions (with noise removed)
    known_categories: dict of lists {food: [abc, xyz]} , comes from categories.json
    returns: dict of lists {food: [abc, xyz, tuv]} , result of adding new descriptions to existing categories
    '''
    known_descriptions = flatten(known_categories.values())
    unknown_descriptions = remove_known(descriptions, known_descriptions)

    return merge_with_categories(known_categories, known_descriptions, unknown_descriptions)


def get_normalized_descriptions(config):
    noise = config.get_noise()
    raw_descriptions = config.get_descriptions()
    return filter_noise(raw_descriptions, noise)


def main():
    config = Data('config.json')
    known_categories = config.get_categories()
    descriptions = get_normalized_descriptions(config)

    categorized = categorize(descriptions, known_categories)

    if input('Do you want to save? Y or N: ').upper() == 'Y':
        config.save_categories(categorized)


if __name__ == '__main__':
    main()
