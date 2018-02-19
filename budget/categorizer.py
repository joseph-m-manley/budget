from budget.CategoryMap import CategoryMap
from budget.Data import Data
from budget.Input import Input


def categorize(known_categories, unknown_descriptions, user=Input()):
    for unknown in unknown_descriptions:
        if not known_categories.keyword_exists(unknown):
            key, category = user.determine_key_and_category(unknown)

            if category == 'q':
                break  # quit
            elif category != '':
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
