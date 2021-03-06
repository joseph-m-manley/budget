import json
import re

from budget.CategoryMap import CategoryMap
from csv import DictReader

def filter_noise(strings, noise):
    '''
    takes a list of raw strings:
        ['xxxhelloxxx', ...]
    and regex patterns:
        ['x{3}', ...]
    returns a list of activities with the noise removed:
        ['hello', ...]
    '''
    pattern = '(%s)' % '|'.join(noise)
    matcher = re.compile(pattern, re.IGNORECASE)
    filtered = [matcher.sub('', _str).strip() for _str in strings]
    return filtered

def get_json(path):
    with open(path) as file:
        return json.load(file)

def save_json(j, path):
    with open(path, 'w+') as file:
        json.dump(j, file, indent=4)

def try_get_json(path):
    try:
        return get_json(path)
    except Exception as e:
        print(e)
        return dict()

def get_table(path):
    with open(path) as csv:
        table = DictReader(csv)
        return list(table)


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
        activity = self.get_activity()
        return [transaction['Description'] for transaction in activity]

    def get_conditioned_descriptions(self):
        noise = self.get_noise()
        raw_descriptions = self.get_descriptions()
        return filter_noise(raw_descriptions, noise)

    def get_activity(self):
        return get_table(self.paths['activity'])        

    def save_categories(self, categoryMap):
        save_json(categoryMap.to_json(), self.paths['categories'])
