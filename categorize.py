#!/usr/bin/env python3

from csv import DictReader
import constants

def get_activity(path):
    with open(path, 'r') as csvfile:
        return DictReader(csvfile)


def contains(categories, description):
    pass


def add_to_categories(categories, description):
    pass


def categorize(path):
    categories = dict() # a dict of string -> lists: categories['food'] = [money, money, money]

    for transaction in get_activity(path):
        description = transaction['Description']
        print(description)
        if not contains(categories, description):
            add_to_categories(categories, description)

def main():
    categorize(constants.path)

if __name__ == '__main__':
    main()
