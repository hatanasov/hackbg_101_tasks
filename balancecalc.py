#!/usr/bin/env python3.6

import datetime

balance_dict = {}
final_amount = 0


def convert_date(date_string):
    day, month, year = date_string.split('/')
    formatted_date = datetime.date(int(year), int(month), int(day))
    return formatted_date


while True:
    transaction = input().split(',')
    if transaction == ['----']:
        break
    transaction_date = transaction[1]
    amount = transaction[0]
    if transaction_date not in balance_dict:
        balance_dict.update({transaction_date: int(amount)})
    else:
        balance_dict[transaction_date] += int(amount)

balance_to_date = input()
balance_date = convert_date(balance_to_date)

for key, value in balance_dict.items():
    if convert_date(key) <= balance_date:
        final_amount += value

print(final_amount)
