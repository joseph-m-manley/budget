#!/usr/bin/env python3

from csv import DictReader

noise = ['DEBIT CARD PURCHASE   ', 'XXXXX3536 ', 'XXXXX1603 ']

def get_activity(path):
    with open(path, 'r') as csvfile:
        return DictReader(csvfile)
    
    
def 

if __name__ == '__main__':
    #Initialize
    transactions = list()
    categories = dict() # a dict of string -> lists: categories['food'] = [money, money, money]

    #Read the list looking for transactions for the current month
    for row in GetActivityCSV(path):
        description = row['Description']
        transactionMonth = row['Date'].split('/')[0]
        for item in home:
            if item in description and (currentMonth == transactionMonth): 
                transactions.append(row['Withdrawals'].replace('$', ''))
                print(row['Description'])

    value = 0.0
    for t in transactions:
        value += float(t)

    print(value)
