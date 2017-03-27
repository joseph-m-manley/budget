#!/usr/bin/env python3
import json
from csv import DictReader
from datetime import datetime


def get_json(path):
    with open(path) as file:
        return json.load(file)


def save_json(j, path):
    with open(path, 'w+') as file:
        json.dump(j, file, indent=4)


def get_table(path):
    with open(path) as csv:
        table = DictReader(csv)
        return list(table)


def invert_dict(d):
    return {value: key for key in d for value in d[key]}


def get_transaction_amount(t):
    if t['Withdrawals']:
        return float(t['Withdrawals'].replace('$', '').replace(',', ''))
    elif t['Deposits']:
        return float(t['Deposits'].replace('$', '').replace(',', ''))
    else:
        return 0.0


def is_relevant(t, description):
    return description in t['Description'] and datetime.now().month == int(t['Date'][0:2])


def summarize(categories, activity):
    expenses = dict.fromkeys(categories.keys(), 0.0)
    descriptions = invert_dict(categories)

    for transaction in activity:
        for description in descriptions:
            if is_relevant(transaction, description):
                category = descriptions[description]
                expenses[category] += get_transaction_amount(transaction)

    return expenses


def main():
    config = get_json('../categorizer/config.json')

    categories = get_json(config['categories'])
    activity = get_table(config['csvfilepath'])

    expenses = summarize(categories, activity)
    save_json(expenses, '../user/expenses.json')


if __name__ == '__main__':
    main()
