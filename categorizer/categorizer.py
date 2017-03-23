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


def categorize(newKeys, categories):
    for key in newKeys:
        x = input('%s\nWhat category does this belong in? ' % key).upper()
        if x == 'Q':
            break
        elif x in categories:
            categories[x].add(key)
        else:
            categories[x] = {key}

    return categories


def flatten(list_of_lists):
    return [x for sublist in list_of_lists for x in sublist]


def filter_noise(words, noise):
    match = '(%s)' % ')|('.join(noise)
    rgx = re.compile(match, re.IGNORECASE)
    return set(re.sub(rgx, '', word).strip() for word in words)


def main():
    config = get_config()

    words = get_column(config['csvfile'], config['column'])
    categories = get_categories(config['categories'])

    newKeys = filter_noise(words, config['noise'])
    updated = categorize(newKeys, categories)

    if get_input('Do you want to save?') == 'Y':
        save_jsn(updated, config['categories'])


if __name__ == '__main__':
    main()
