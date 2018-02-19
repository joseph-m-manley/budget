import json

from budget.utilities import filter_noise
from budget.CategoryMap import CategoryMap
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
