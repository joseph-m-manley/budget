#!/usr/bin/env python3

from iohelpers import *
import re


def filter_noise(words, noise):
    matcher = '(%s)' % ')|('.join(noise)
    rgx = re.compile(matcher, re.IGNORECASE)
    return set(re.sub(rgx, '', word).strip() for word in words)


def flatten(list_of_lists):
    return [item for _list in list_of_lists for item in _list]


def categorize(words, categories):
    working = {k: set(v) for k, v in categories.items()}
    shown = set(flatten(working.values()))

    for word in words:
        if word not in shown:
            shown.add(word)

            print('\n%s' % word)
            x = input('What category does this belong in? ').upper()
            if x == 'Q':
                break
            elif x == '':
                continue
            elif x in working:
                working[x].add(word)
            else:
                working[x] = {word}

    return {k: list(v) for k, v in working.items()}


def main():
    config = get_config()
    noise = get_noise(config['noise'])
    existing_categories = get_json(config['categories'])

    raw_words = get_column(config['csvfilepath'], config['column'])
    normalized_words = filter_noise(raw_words, noise)

    categorized = categorize(normalized_words, existing_categories)
    print(categorized)

    if input('Do you want to save? Y or N: ').upper() == 'Y':
        save_jsn(categorized, config['categories'])


if __name__ == '__main__':
    main()
