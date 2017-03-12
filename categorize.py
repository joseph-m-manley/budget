#!/usr/bin/env python3

from csv import DictReader
import constants
from datetime import datetime
import re


def relevant_activity(t):
    return (t['Withdrawals']
    and datetime.now().month - 1 == int(t['Date'][0:2])
    and 'TRANSFER' not in t['Description'])


def normalize(description):
    for n in constants.noise:
        description = re.sub(n, '', description)
    return description.strip()


def add_withdrawal(categories, transaction):
    if relevant_activity(transaction):
        description = normalize(transaction['Description'])                    
        categories[description] = transaction    


def get_withdrawals(path):
    withdrawals = dict()
    with open(path) as activity:
        for transaction in DictReader(activity):
            add_withdrawal(withdrawals, transaction)
    return withdrawals


def save_set(s, path):
    with open(path, 'w+') as f:
        f.writelines("%s\n" % item for item in set)


def categorize(withdrawals):
    care = set()
    dontcare = set()
    for key in withdrawals.keys():
        print(key)
        print(withdrawals[key]['Withdrawals'])
        x = input('Do you care about this? Y or N: ')
        if x.upper() == 'Y':
            care.add(key)
        elif x.upper() == 'N':
            dontcare.add(key)
        elif x.upper() == 'Q':
            break
    save_set(care, "care.txt")
    save_set(dontcare, "dontcare.txt")


def main():
    activity = get_withdrawals(constants.path)
    categorize(activity)

if __name__ == '__main__':
    main()
