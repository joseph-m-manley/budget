#!/usr/bin/env python3

from csv import DictReader
import constants
from datetime import datetime
import re


def relevant_activity(t):
    return t['Withdrawals'] and datetime.now().month - 1 == int(t['Date'][0:2])


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


def categorize(withdrawals):
    total = 0.0
    for v in withdrawals.values():
        total += float(v['Withdrawals'].replace('$', '').replace(',', ''))
    print(total)
        


def main():
    activity = get_withdrawals(constants.path)
    categorize(activity)

if __name__ == '__main__':
    main()
