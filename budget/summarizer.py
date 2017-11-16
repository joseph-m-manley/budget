#!/usr/bin/env python3

import datetime
import budget.utilities as util


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
    return description in t['Description']


def summarize(categories, activity):
    expenses = dict.fromkeys(categories.keys(), 0.0)
    descriptions = invert_dict(categories)
    for transaction in activity:
        # Find the category associated with this transaction
        for description in descriptions:
            if is_relevant(transaction, description):
                category = descriptions[description]
                expenses[category] += get_transaction_amount(transaction)
                break

    return {k: round(v, 2) for k, v in expenses.items()}


def subtract_expenses(budget, expenses):
    remaining = dict.fromkeys(budget.keys(), 0.0)
    for category in budget:
        difference = float(budget[category]) - float(expenses[category])
        remaining[category] = round(difference, 2)

    return remaining


def calculate_totals(budget, expenses):
    if budget != dict():
        remaining = subtract_expenses(budget, expenses)
        return {'budget': budget, 'expenses': expenses, 'remaining': remaining}
    else:
        return {'expenses': expenses}


def main():
    config = util.get_config()

    budget = util.get_budget(config['budget'])
    expenses = summarize(
        util.get_json(config['categories']),
        util.get_table(config['activity']))

    util.save_json(
        calculate_totals(budget, expenses),
        config['budget'])


if __name__ == '__main__':
    main()
