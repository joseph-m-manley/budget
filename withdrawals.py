#!/usr/bin/env python3

from csv import DictReader
from re import sub

def normalize(description, noise):
    for n in noise:
        description = re.sub(n, '', description)
    return description.strip()

def is_withdrawal(transaction):
    return transaction['Withdrawals'] and 'TRANSFER' not in transaction['Description']

def get_withdrawals(self, file, noise):
    keys = set()
    for transaction in DictReader(file):
        if is_withdrawal(transaction):
            keys.add(normalize(transaction['Description'], noise))                    
    return frozenset(keys)

class KeyFinder():
    def __init__(self, path, noise):
        self.path = path
        self.noise = noise

    def get_withdrawal_keys(self):
        with open(self.path, 'r') as activity:
            return get_withdrawals(activity, self.noise)