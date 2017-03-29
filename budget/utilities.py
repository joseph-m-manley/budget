#!/usr/bin/env python3

import json
import re
from csv import DictReader


def dict_of_sets(d):
    return {k: set(v) for k, v in d.items()}


def dict_of_lists(d):
    return {k: list(v) for k, v in d.items()}


def invert_dict(d):
    return {value: key for key in d for value in d[key]}


def flatten(list_of_lists):
    return [item for _list in list_of_lists for item in _list]


def join_patterns(patterns):
    matcher = '(%s)' % ')|('.join(patterns)
    return re.compile(matcher, re.IGNORECASE)


def filter_noise(words, noise):
    rgx = join_patterns(noise)
    return set(rgx.sub('', word).strip() for word in words)


def contains_any(phrase, words_in_phrase):
    if not words_in_phrase:
        return False
    rgx = join_patterns(words_in_phrase)
    return bool(rgx.search(phrase))


def filter_duplicates(phrases, words_to_filter):
    if not words_to_filter:
        return set(phrases)
    return set(filter(
        lambda phrase: not contains_any(phrase, words_to_filter), phrases))


def get_json(path):
    with open(path) as file:
        return json.load(file)


def save_json(j, path):
    with open(path, 'w+') as file:
        json.dump(j, file, indent=4)


def get_config():
    return get_json('config.json')


def get_noise(path):
    return get_json(path)['noise']


def get_column(path, col):
    with open(path) as csv:
        table = DictReader(csv)
        return set(row[col] for row in table)


def get_table(path):
    with open(path) as csv:
        table = DictReader(csv)
        return list(table)
