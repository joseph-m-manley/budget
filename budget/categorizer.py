from budget.CategoryMap import CategoryMap
from budget.Data import Data
from budget.Input import Input

class Categorizer():
    def __init__(self, known_categories, finder=Input()):
        self.known_categories = known_categories
        self.finder = finder

    def categorize(self, unknown_descriptions):
        for unknown in unknown_descriptions:
            if not self.known_categories.keyword_exists(unknown):
                key, category = self.finder.determine_key_and_category(unknown)

                if category.upper() == 'Q':
                    break  # quit
                elif category != '':
                    self.known_categories.add(category, key)

        return self.known_categories


def main():
    data = Data('data.json')
    known_categories = data.get_categories()
    categorizer = Categorizer(known_categories)

    descriptions = data.get_conditioned_descriptions()
    categorized = categorizer.categorize(descriptions)

    if input('Do you want to save? Y or N: ').upper() == 'Y':
        data.save_categories(categorized)


if __name__ == '__main__':
    main()
