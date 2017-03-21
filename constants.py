#!/usr/bin/env python3

noise = [
        'DEBIT',
        'CARD PURCHASE',
        'INDIANAPOLIS?',
        'IN',
        'CARMEL',
        '#',
        'X+\d{4}',
        '\d+',
        'SQ \*',
        'RECURRING',
        'ACH']


paths = {
        activity: '../depositAcctivityExport.csv',
        care: '../categories/care.txt',
        dontcare: '../categories/care.txt'}