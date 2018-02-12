#!/usr/bin/env python3

import budget.utilities as util
from collections import OrderedDict


def add_category(categories, category, value_to_add):
    if category in categories:
        categories[category].add(value_to_add)
    else:
        categories[category] = {value_to_add}


def ask_for_key(words):
    print('\n%s' % words)
    key = words
    if len(key) > 15:
        x = input('Assign a key? ').upper()
        if x not in ('Y', 'Q', 'N', ''):
            key = x
        elif x == 'Y':
            key = input('Key: ').upper()
    return key


def to_dict_of_sets(d):
    return {k: set(v) for k, v in d.items()}


def to_dict_of_lists(d):
    return {k: list(v) for k, v in d.items()}


def flatten(list_of_lists):
    return [item for _list in list_of_lists for item in _list]


def flatten_to_set(list_of_lists):
    return set(flatten(list_of_lists))


def merge_categories(descriptions_to_categorize, categories_with_descriptions):
    '''
    descriptions_to_categorize: set
    categories_with_descriptions: dict of lists {food: [abc, xyz]} , comes from categories.json
    returns: dict of lists {food: [abc, xyz, tuv]} , result of adding new descriptions to existing categories
    '''
    known_descriptions = flatten_to_set(categories_with_descriptions.values())
    unknown_descriptions = util.remove_matches(descriptions_to_categorize, known_descriptions)
    merged = to_dict_of_sets(categories_with_descriptions)

    for unknown_description in unknown_descriptions:
        if util.contains_none(unknown_description, known_descriptions):
            key = ask_for_key(unknown_description)
            known_descriptions.add(key)

            category = input('What category does this belong in? ').upper()

            if category == 'Q':
                break  # quit
            elif category == '':
                continue  # skip this item

            add_category(merged, category, key)

    return to_dict_of_lists(merged)


def categorize(config):
    noise = util.get_noise(config['noise'])
    raw_descriptions = util.get_descriptions(config['activity'])
    normalized_descriptions = util.filter_noise(raw_descriptions, noise)

    existing_categories = util.get_json(config['categories'])
    return merge_categories(normalized_descriptions, existing_categories)


def main():
    config = util.get_config()
    categorized = categorize(config)

    if input('Do you want to save? Y or N: ').upper() == 'Y':
        util.save_json(categorized, config['categories'])


if __name__ == '__main__':
    main()
