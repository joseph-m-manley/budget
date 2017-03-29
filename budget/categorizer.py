#!/usr/bin/env python3

import budget.utilities as util


def add_category(category, value_to_add, categories):
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


def merge_categories(descriptions, categories):
    known_descriptions = set(util.flatten(categories.values()))
    merged = util.dict_of_sets(categories)
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

            add_category(category, key, merged)

    return util.dict_of_lists(merged)


def categorize(config):
    noise = util.get_noise(config['noise'])
    existing_categories = util.get_json(config['categories'])

    raw_descriptions = util.get_column(config['csvfilepath'], config['column'])
    normalized_descriptions = util.filter_noise(raw_descriptions, noise)

    return merge_categories(normalized_descriptions, existing_categories)


def main():
    config = util.get_config()
    categorized = categorize(config)

    if input('Do you want to save? Y or N: ').upper() == 'Y':
        save_jsn(categorized, config['categories'])


if __name__ == '__main__':
    main()
