#!/usr/bin/env python3

# import constants
import withdrawals


def get_input(message, options):
    x = None
    while x not in options:
        x = input(message + ' ' + ''.join(options)).upper()
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
        x = get_input('%s: Do you care about this?' % key, ('Y', 'N', 'Q'))
        if x == 'Y':
            care.add(key)
        elif x == 'N':
            dontcare.add(key)
        elif x == 'Q':
            break


def categorize(keys):
    care = open_set("care.txt")
    dontcare = open_set("dontcare.txt")

    newKeys = keys.difference(care.union(dontcare))
    process_keys(newKeys, care, dontcare)

    x = get_input
    save_set(care, "care.txt")
    save_set(dontcare, "dontcare.txt")


# def main():
    # keys = withdrawals.get_keys(constants.path, constants.noise)
    # categorize(keys)


# if __name__ == '__main__':
#     main()
