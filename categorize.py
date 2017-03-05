#!/usr/bin/env python3

from csv import DictReader

noise = ['DEBIT CARD PURCHASE   ', 'XXXXX3536 ', 'XXXXX1603 ']

def get_activity(path):
    with open(path, 'r') as csvfile:
        return DictReader(csvfile)


def contains(categories, description):
    pass


def add_to_categories(categories, description):
    pass


def categorize()
    categories = dict() # a dict of string -> lists: categories['food'] = [money, money, money]

    # Read the list looking for transactions for the current month
    for transaction in get_activity(path):
        description = transaction['Description']
        if not contains(categories, description):
            add_to_categories(categories, description)

def main():
    pass

if __name__ == '__main__':
    main()
