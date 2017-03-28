#!/usr/bin/env python3

import re


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


def filter_noise_from_words(words, noise):
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
