#!/usr/bin/env python3

from csv import DictReader
import re


def normalize(description, noise):
    for n in noise:
        description = re.sub(n, '', description)
    return description.strip()


def is_withdrawal(transaction):
    return (transaction['Withdrawals'] and
            'TRANSFER' not in transaction['Description'])


def get_withdrawals(file, noise):
    keys = set()
    for transaction in DictReader(file):
        if is_withdrawal(transaction):
            keys.add(normalize(transaction['Description'], noise))
    return keys


def get_keys(path, noise):
    with open(path, 'r') as activity:
        return frozenset(get_withdrawals(activity, noise))

