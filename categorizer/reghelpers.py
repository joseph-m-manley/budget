#!/usr/bin/env python3

import re


def rgx_filter(words, noise, func):
    matcher = '(%s)' % ')|('.join(noise)
    rgx = re.compile(matcher, re.IGNORECASE)
    return func(rgx, words)


def filter_noise(words, noise):
    def rm_noise(rgx, words):
        return set(re.sub(rgx, '', word).strip() for word in words)
    return rgx_filter(words, noise, func)


def filter_duplicates(words, dupes):
    def rm_dupes(rgx, words):
        return set(filter(lambda w: not rgx.search(w), words))
    return rgx_filter(words, dupes, func)
