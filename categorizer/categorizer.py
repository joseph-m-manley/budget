#!/usr/bin/env python3

import constants
import json
from constants import paths
import re
from csv import DictReader


def get_config():
    with open('config.json') as file:
        return json.load(file)


def get_input(message, options=('Y', 'N', 'Q')):
    x = None
    message += ' '
    message += ', '.join(options[:-1])
    message += ' or %s: ' % options[-1]
    while x not in options:
        x = input(message).upper()
    return x


def open_set(path):
    import os.path
    if os.path.exists(path):
        with open(path, 'r') as f:
            return set(f.readlines())
    return set()


def save_set(s, path):
    with open(path, 'w+') as f:
        f.writelines("%s\n" % item for item in s)


def process_keys(keys, care, dontcare):
    for key in keys:
        x = get_input('%s\nDo you care about this?' % key)
        if x == 'Y':
            care.add(key)
        elif x == 'N':
            dontcare.add(key)
        elif x == 'Q':
            break


def categorize(keys, carePath, dontcarePath):
    care = open_set(carePath)
    dontcare = open_set(dontcarePath)

    old = care.union(dontcare)
    newKeys = frozenset(keys.difference(old))
    process_keys(newKeys, care, dontcare)

    if get_input('Do you want to save?') == 'Y':
        save_set(care, carePath)
        save_set(dontcare, dontcarePath)


def normalizing_func(noise):
    def normalize(description):
        for n in noise:
            description = re.sub(n, '', description, flags=re.IGNORECASE)
        return description.strip()
    return normalize


def normalize_keys(keys, noise):
    normalizer = normalizing_func(noise)
    return set(map(normalizer, keys))


def get_column(path, col):
    with open(path) as csv:
        table = DictReader(csv)
        return set(row[col] for row in table)


def main():
    config = get_config()
    descriptions = get_column(config['paths']['activity'], 'Description')
    keys = normalize_keys(descriptions, config['noise'])
    categorize(keys, config['paths']['care'], config['paths']['dontcare'])


if __name__ == '__main__':
    main()
