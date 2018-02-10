#!/usr/bin/env python3

import json
import re
from csv import DictReader


def join_patterns(patterns):
    '''
    takes a list of regex patterns and makes:
        '(one|two|three|four)'
    returns a regex matcher for that pattern
    '''
    matcher = '(%s)' % '|'.join(patterns)
    return re.compile(matcher, re.IGNORECASE)


def filter_noise(strings, noise):
    '''
    takes a list of raw strings:
        ['xxxhelloxxx', ...]
    and regex patterns:
        ['x{3}', ...]
    creates a list of activities with the noise removed:
        ['hello', ...]
    returns it as a set
    '''
    rgx = join_patterns(noise)
    filtered = [rgx.sub('', _str).strip() for _str in strings]
    return set(filtered)


def contains_any(string, possible_substrings):
    '''
    takes a string and a list of possible substrings
    returns whether any of the substrings exist in the string
    '''
    if not possible_substrings:
        return False
    rgx = join_patterns(possible_substrings)
    return bool(rgx.search(string))


def contains_none(string, possible_substrings):
    '''
    takes a string and a list of possible substrings
    returns whether none of the substrings exist in the string
    '''
    return not contains_any(string, possible_substrings)


def remove_matches(strings, substrings):
    '''
    takes a list of strings and a list of substrings
    removes any element in strings in which any of the substrings is found
    returns the filtered strings as a set
    '''
    if not substrings:
        return set(strings)
    filtered = filter(lambda desc: contains_none(desc, substrings), strings)
    return set(filtered)


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
