#!/usr/bin/env python3

import constants
import withdrawals


def get_choice(message, choices):
    message += ': '
    message += ', '.join(choices[:-1])
    message += ' or ' + choices[-1]
    x = None
    while x not in choices:
        x = input(message).upper()
    return x


def open_set(path):
    with open(path, 'r') as f:
        return set(f.readlines())


def save_set(s, path):
    with open(path, 'w+') as f:
        f.writelines("%s\n" % item for item in s)


def process_keys(keys, care, dontcare):
    for key in keys:
        print(key)
        x = get_choice('%s: Do you care about this?' % key, ('Y', 'N', 'Q'))
        if x == 'Y':
            care.add(key)
        elif x == 'N':
            dontcare.add(key)
        elif x == 'Q':
            break


def categorize(keys):
    care = open_set(constants.paths['care'])
    dontcare = open_set(constants.paths['dontcare'])

    newKeys = frozenset(keys.difference(care.union(dontcare)))
    process_keys(newKeys, care, dontcare)

    x = get_choice
    save_set(care, constants.paths['care'])
    save_set(dontcare, constants.paths['dontcare'])


def main():
    keys = withdrawals.get_keys(constants.paths['activity'], constants.noise)
    categorize(keys)


if __name__ == '__main__':
    main()
