# Задача 4. В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

from math import factorial as fact

ticketsNum = 100
winningTicketsNum = 2
draw = 2


def factorialFunc(num, draw):
    res = fact(num) / (fact(draw) * fact(num - draw))
    return res


winTickDrawNum = factorialFunc(winningTicketsNum, draw)
generalTickDrawNum = factorialFunc(ticketsNum, draw)
resultingProbability = round(winTickDrawNum / generalTickDrawNum * 100, 3)
print(f'Вероятность того, что все 3 извлеченные детали окрашены равна {resultingProbability}%')