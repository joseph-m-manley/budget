#!/usr/bin/env python3

from budget.Classes import Data, Input, CategoryMap

def categorize(known_categories, unknown_descriptions, user=Input()):
    '''
    known_categories: CategoryMap intialized from categories.json
    unknown_descriptions: a list of normalized activity descriptions from activity file
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


def main():
    config = Data('config.json')
    known_categories = config.get_categories()
    descriptions = config.get_normalized_descriptions()

    categorized = categorize(known_categories, descriptions)

    if input('Do you want to save? Y or N: ').upper() == 'Y':
        config.save_categories(categorized)


if __name__ == '__main__':
    main()
