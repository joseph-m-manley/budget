#!/usr/bin/env python3


def invert_dict(d):
    return {value: key for key in d for value in d[key]}


def get_transaction_amount(t):
    if t['Withdrawals']:
        return float(t['Withdrawals'])
    elif t['Deposits']:
        return float(t['Deposits'])
    else:
        return 0.0


def summarize(categories, activity):
    expenses = dict.fromkeys(categories.keys(), 0.0)
    descriptions = invert_dict(categories)

    for transaction in activity:
        for description in descriptions:
            if description in transaction['Description']:
                category = descriptions[description]
                expenses[category] += get_transaction_amount(transaction)

    return expenses


def main():
    pass
    # config = get_config()
    # categories = get_categories(config['categories'])
    # activity = get_jsn(config['csvfilepath'])

    # summarize(categories, activity)


if __name__ == '__main__':
    main()
