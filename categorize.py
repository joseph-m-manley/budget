#!/usr/bin/env python3

import constants
import withdrawals

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
    keys = get_withdrawal_keys(constants.path, constants.noise)

if __name__ == '__main__':
    main()
