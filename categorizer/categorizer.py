#!/usr/bin/env python3

from iohelpers import *
import re


def get_input(message, options=('Y', 'N', 'Q')):
    x = None
    message += ' '
    message += ', '.join(options[:-1])
    message += ' or %s: ' % options[-1]
    while x not in options:
        x = input(message).upper()
    return x


def categorize(keys, categories=dict()):
    working = {k: set(v) for k, v in categories.items()}
    for key in keys:
        print(key)
        x = input('What category does this belong in? ').upper()
        if x == 'Q':
            break
        elif x in working:
            working[x].add(key)
        else:
            working[x] = {key}

    return {k: list(v) for k, v in working.items()}


def filter_noise(words, noise):
    match = '(%s)' % ')|('.join(noise)
    rgx = re.compile(match, re.IGNORECASE)
    return set(re.sub(rgx, '', word).strip() for word in words)


def main():
    config = get_config()
    categories = get_categories(config['categories'])
    words = get_column(config['csvfilepath'], config['column'])

    clean_words = filter_noise(words, config['noise'])
    updated = categorize(clean_words, categories)

    if get_input('Do you want to save?') == 'Y':
        save_jsn(updated, config['categories'])


if __name__ == '__main__':
    main()
