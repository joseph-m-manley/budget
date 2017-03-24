#!/usr/bin/env python3

import json
from csv import DictReader


def get_json(path):
    with open(path) as file:
        return json.load(file)


def save_jsn(j, path):
    with open(path, 'w+') as file:
        json.dump(j, file, indent=4)


def get_config():
    return get_json('config.json')


def get_noise(path):
    return get_json(path)['noise']


def get_categories(path):
    return get_json(path)['categories']


def get_column(path, col):
    with open(path) as csv:
        table = DictReader(csv)
        return set(row[col] for row in table)

