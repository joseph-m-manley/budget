#!/usr/bin/env python3

noise = [
        'DEBIT CARD',
        'RECURRING',
        'PURCHASE',
        'INDIANAPOLIS?',
        '\bIN\b',
        'CARMEL',
        '#?\b\d+',
        'X+\d{4}',
        '\b\w+ \*',
        '\bACH\b']

paths = {
        'activity': 'depositAcctivityExport.csv',
        'care': '../categories/care.txt',
        'dontcare': '../categories/dontcare.txt'}
