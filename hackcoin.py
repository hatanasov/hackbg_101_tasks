#!/usr/bin/env python3.6
amount = int(input())
coin_price = [int(price) for price in input().split(',')]

trade_history = []
control_flag = 'sell'


def calc_invest(price, bet):
    hackcoin = bet / price
    return hackcoin


def calc_profit(price, hackcoin):
    profit = price * hackcoin
    return profit


for index in range(0, len(coin_price) - 1):
    if coin_price[index] < coin_price[index + 1] and control_flag != 'buy':
        control_flag = 'buy'
        buy_coins = calc_invest(coin_price[index], amount)
        amount = 0
        trade_history.append(control_flag)
    elif coin_price[index] > coin_price[index + 1] and control_flag != 'sell':
        control_flag = 'sell'
        sell = calc_profit(coin_price[index], buy_coins)
        amount += sell
        trade_history.append(control_flag)
    else:
        trade_history.append('hold')

if control_flag == 'buy':
    control_flag = 'sell'
    sell = calc_profit(coin_price[-1], buy_coins)
    amount += sell
    trade_history.append(control_flag)
else:
    trade_history.append('hold')

print(f'{amount:.2f}')
print(*trade_history, sep=', ')
