import json
from csv import DictReader

def get_json(path):
    with open(path) as file:
        return json.load(file)

def save_json(j, path):
    with open(path, 'w+') as file:
        json.dump(j, file, indent=4)

def try_get_json(path):
    try:
        return get_json(path)
    except FileNotFoundError as e:
        print(e)
        return dict()

from budget.utilities import filter_noise
class Data():
    def __init__(self, configPath):
        self.paths = get_json(configPath)

    def get_categories(self):
        return CategoryMap(try_get_json(self.paths['categories']))

    def get_noise(self):
        return try_get_json(self.paths['noise'])['noise']

    def get_budget(self):
        return try_get_json(self.paths['budget'])['expenses']

    def get_descriptions(self):
        with open(self.paths['activity']) as csv:
            table = DictReader(csv)
            return set(row['Description'] for row in table)

    def get_normalized_descriptions(self):
        noise = self.get_noise()
        raw_descriptions = self.get_descriptions()
        return filter_noise(raw_descriptions, noise)

    def save_categories(self, categories):
        save_json(categories, self.paths['categories'])


class Input():
    def ask_for_category(self, key):
        return input('What category does %s belong in? ' % key).lower()

    def ask_for_key(self, description):
        print('\n%s' % description)
        key = description
        if len(key) > 15:
            x = input('Assign a key? ').lower()
            if x not in ('Y', 'Q', 'N', ''):
                key = x
            elif x == 'Y':
                key = input('Key: ').lower()
        return key
    
    def determine_key_and_category(self, description):
        key = self.ask_for_key(description)
        category = self.ask_for_category(key)
        return (key, category)
