#!/usr/bin/env python3

from budget.utilities import remove_known, contains_none, filter_noise
from budget.Classes import Data, Input, CategoryMap
from collections import OrderedDict


def flatten(list_of_lists):
    return [item for _list in list_of_lists for item in _list]


def merge_with_categories(known_categories, unknown_descriptions, user=Input()):
    '''
    known_categories: dict of lists {food: [abc, xyz]} , comes from categories.json
    unknown_descriptions: a list of normalized activity descriptions that do not match any known category keys
    '''
    for unknown in unknown_descriptions:
        if not known_categories.keyword_exists(unknown):
            (key, category) = user.determine_key_and_category(unknown)

            if category == 'Q':
                break  # quit
            elif category == '':
                continue  # skip this item

            known_categories.add(category, key)

    return known_categories


def categorize(known_categories, descriptions):
    '''
    descriptions: activity descriptions (with noise removed)
    known_categories: dict of lists {food: [abc, xyz]} , comes from categories.json
    returns: dict of lists {food: [abc, xyz, tuv]} , result of adding new descriptions to existing categories
    '''
    return merge_with_categories(known_categories, descriptions)


def main():
    config = Data('config.json')
    known_categories = CategoryMap(config.get_categories())
    descriptions = config.get_normalized_descriptions()

    categorized = categorize(known_categories, descriptions)

    if input('Do you want to save? Y or N: ').upper() == 'Y':
        config.save_categories(categorized)


if __name__ == '__main__':
    main()
