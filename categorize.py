#!/usr/bin/env python3

from csv import DictReader
import constants


def normalize(description):
    for n in constants.noise:
        description = description.replace(n, '')
    return description


def add_withdrawal(categories, transaction):
    if transaction['Withdrawals']:
        description = normalize(transaction['Description'])                    
        categories[description] = transaction    


def categorize_withdrawals(path):
    withdrawals = dict()
    with open(path) as activity:
        for transaction in DictReader(activity):
            add_withdrawal(withdrawals, transaction)
    return withdrawals


def main():
    categorize_withdrawals(constants.path)


if __name__ == '__main__':
    main()
