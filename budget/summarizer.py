#!/usr/bin/env python3

from budget.Data import Data, save_json


def subtract_expenses(budget, expenses):
    remaining = dict.fromkeys(budget.keys(), 0.0)
    for category in budget:
        difference = float(budget.get(category)) - float(expenses.get(category, 0.0))
        remaining[category] = round(difference, 2)

    return remaining


def calculate_totals(budget, expenses):
    if budget != dict():
        remaining = subtract_expenses(budget, expenses)
        return {'budget': budget, 'expenses': expenses, 'remaining': remaining}
    else:
        return {'expenses': expenses}


def invert_dict(d):
    return {value: key for key in d for value in d[key]}


def get_transaction_amount(t):
    if 'Withdrawals' in t and t['Withdrawals']:
        value = t['Withdrawals']
    elif 'Deposits' in t and t['Deposits']:
        value = t['Deposits']
    elif 'Debit' in t and t['Debit']:
        value = t['Debit']
    elif 'Credit' in t and t['Credit']:
        value = t['Credit']
    else:
        value = '$0.00'
    return float(value.replace('$', '').replace(',', ''))


def is_relevant(t, description):
    return description in t['Description']


def summarize(categories, activity):
    expenses = {category: 0.0 for category in categories}
    descriptions = invert_dict(categories)
    for transaction in activity:
        for description in descriptions:
            if is_relevant(transaction, description):
                category = descriptions[description]
                expenses[category] += get_transaction_amount(transaction)
                break

    return {k: round(v, 2) for k, v in expenses.items()}


def main():
    config = Data('config.json')

    categories = config.get_categories()
    activity = config.get_activity()
    expenses = summarize(categories, activity)

    budget = config.get_budget()
    totals = calculate_totals(budget, expenses)
    save_json(totals, config.paths['budget'])


if __name__ == '__main__':
    main()
