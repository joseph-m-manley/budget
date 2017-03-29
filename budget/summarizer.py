#!/usr/bin/env python3

from datetime import datetime
import budget.utilities as util


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
    descriptions = util.invert_dict(categories)

    for transaction in activity:
        for description in descriptions:
            if is_relevant(transaction, description):
                category = descriptions[description]
                expenses[category] += get_transaction_amount(transaction)
                break

    return expenses


def main():
    config = util.get_config()

    categories = util.get_json(config['categories'])
    activity = util.get_table(config['csvfilepath'])

    expenses = summarize(categories, activity)

    util.save_json(expenses, config['expenses'])


if __name__ == '__main__':
    main()
