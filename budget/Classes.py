class CategoryMap():
    def __init__(self):
        self.d = dict()

    def __init__(self, dictOfLists):
        self.d = {k: v for k, v in dictOfLists}

    def __safe_get(self, key):
        if key not in self.d:
            self.d[key] = []
        return self.d[key]

    def __getitem__(self, key):
        return self.get(key)

    def get(self, key):
        if key not in self.d:
            raise KeyError()
        return self.d[key]

    def add(self, key, value):
        self.__safe_get(key).append(value)


import re
class Description():
    def __init__(self, string, noise=[]):
        self.string = self.remove_noise(string, noise)

    def __eq__(self, thing):
        if isinstance(thing, Description): 
            return self.string == thing.string
        elif isinstance(thing, str):
            return self.string == thing
        else:
            raise TypeError("thing should be a Description or a string")

    def __str__(self):
        return self.string

    def remove_noise(self, string, noise):
        pattern = '(%s)' % '|'.join(noise)
        matcher = re.compile(pattern, re.IGNORECASE)
        return matcher.sub('', string).strip()

from budget import utilities
class Description2(str):
    def contains_any(self, possible_substrings):
        return utilities.contains_any(self, possible_substrings)

    def contains_none(self, possible_substrings):
        return not self.contains_any(possible_substrings)


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


class Data():
    def __init__(self, configPath):
        self.paths = get_json(configPath)

    def get_categories(self):
        return try_get_json(self.paths['categories'])

    def get_noise(self):
        return try_get_json(self.paths['noise'])['noise']

    def get_budget(self):
        return try_get_json(self.paths['budget'])['expenses']

    def get_descriptions(self):
        with open(self.paths['activity']) as csv:
            table = DictReader(csv)
            return set(row['Description'] for row in table)

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
    
    def determine_key_and_category(self, unknown):
        key = self.ask_for_key(unknown)
        category = self.ask_for_category(key)
        return (key, category)


class Category():
    def __init__(self, items):
        self.items = items

    def belongs(self, description):
        desc = description.upper()
        for item in self.items:
            if item.upper() in desc:
                return True
        return False

