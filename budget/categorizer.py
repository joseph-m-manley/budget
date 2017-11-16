#!/usr/bin/env python3

import budget.utilities as util


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


def merge_categories(descriptions, categories):
    known_descriptions = set(flatten(categories.values()))
    merged = to_dict_of_sets(categories)
    unknown_descriptions = util.filter_duplicates(descriptions, known_descriptions)

    for unknown_descr in unknown_descriptions:
        if not util.contains_any(unknown_descr, known_descriptions):
            key = ask_for_key(unknown_descr)
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
