#!/usr/bin/env python3

import datetime
import budget.utilities as util


def get_budget(path):
    return util.get_json(path)['budget']


def invert_dict(d):
    return {value: key for key in d for value in d[key]}


def get_transaction_amount(t):
    if t['Withdrawals']:
        return float(t['Withdrawals'].replace('$', '').replace(',', ''))
    elif t['Deposits']:
        return float(t['Deposits'].replace('$', '').replace(',', ''))
    else:
        return 0.0


def is_relevant(t, description, currentMonth):
    return description in t['Description'] and currentMonth == int(t['Date'][0:2])


def summarize(categories, activity):
    expenses = dict.fromkeys(categories.keys(), 0.0)
    descriptions = invert_dict(categories)
    currentMonth = datetime.datetime.now().month

    for transaction in activity:
        for description in descriptions:
            if is_relevant(transaction, description, currentMonth):
                category = descriptions[description]
                expenses[category] += get_transaction_amount(transaction)
                break

    return expenses


def subtract_expenses(budget, expenses):
    remaining = dict.fromkeys(budget.keys())
    for category in budget:
        remaining[category] = float(budget[category]) - float(expenses[category])

    return remaining


def main():
    config = util.get_config()

    expenses = summarize(
        util.get_json(config['categories']),
        util.get_table(config['activity']))

    budget = get_budget(config['budget'])
    
    remaining = subtract_expenses(budget, expenses)

    util.save_json(
        {'budget': budget, 'expenses': expenses, 'remaining': remaining},
        config['budget'])


if __name__ == '__main__':
    main()
