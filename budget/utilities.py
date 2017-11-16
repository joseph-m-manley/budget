#!/usr/bin/env python3

import json
import re
from csv import DictReader


def join_patterns(patterns):
    matcher = '(%s)' % '|'.join(patterns)
    return re.compile(matcher, re.IGNORECASE)


def filter_noise(words, noise):
    rgx = join_patterns(noise)
    return set(rgx.sub('', word).strip() for word in words)


def contains_any(phrase, subst_to_find):
    if not subst_to_find:
        return False
    rgx = join_patterns(subst_to_find)
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


def try_get_json(path, key):
    try:
        return get_json(path)[key]
    except:
        return dict()


def get_noise(path):
    return try_get_json(path, 'noise')


def get_budget(path):
    return try_get_json(path, 'budget')


def get_descriptions(path):
    with open(path) as csv:
        table = DictReader(csv)
        return set(row['Description'] for row in table)


def get_table(path):
    with open(path) as csv:
        table = DictReader(csv)
        return list(table)
