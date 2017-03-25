#!/usr/bin/env python3

import re


def join_patterns(patterns):
    matcher = '(%s)' % ')|('.join(patterns)
    return re.compile(matcher, re.IGNORECASE)


def filter_noise(words, noise):
    rgx = join_patterns(noise)
    return set(rgx.sub('', word).strip() for word in words)


def contains_any(phrase, words_to_match):
    if not words_to_match:
        return False
    rgx = join_patterns(words_to_match)
    return bool(rgx.search(phrase))


def filter_duplicates(phrases, words_to_filter):
    if not words_to_filter:
        return set(phrases)
    return set(filter(
        lambda phrase: not contains_any(phrase, words_to_filter), phrases))
