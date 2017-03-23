#!/usr/bin/env python3

import json
import re
from csv import DictReader


def get_json(path):
    with open(path) as file:
        return json.load(file)


def save_jsn(j, path):
    with open(path, 'w+') as file:
        json.dump(j, file, indent=4)


def get_config():
    return get_json('config.jsn')


def get_categories(path):
    return get_json(path)['categories']


def get_input(message, options=('Y', 'N', 'Q')):
    x = None
    message += ' '
    message += ', '.join(options[:-1])
    message += ' or %s: ' % options[-1]
    while x not in options:
        x = input(message).upper()
    return x


def categorize(newKeys, categories=None):
    if categories is None:
        categories = dict()

    for key in newKeys:
        x = input('%s\nWhat category does this belong in? ' % key)
        if x == 'Q':
            break
        elif x in categories:
            categories[x].add(key)
        else:
            categories[x] = {key}

    return categories


def flatten(list_of_lists):
    return [x for sublist in list_of_lists for x in sublist]


def normalize(words, noise):
    result = set()
    for word in words:
        for n in noise:
            word = re.sub(n, '', word, flags=re.IGNORECASE)
        result.add(word.strip())
    return result


def get_column(path, col):
    with open(path) as csv:
        table = DictReader(csv)
        return set(row[col] for row in table)


def main():
    config = get_config()

    descriptions = get_column(config['csvfile'], config['column'])
    newKeys = normalize(descriptions, config['noise'])
    categories = get_categories(config['categories'])

    updated = categorize(newKeys, categories)

    if get_input('Do you want to save?') == 'Y':
        save_jsn(updated, config['categories'])


if __name__ == '__main__':
    main()
