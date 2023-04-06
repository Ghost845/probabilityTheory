# Задача 3.В ящике имеется 15 деталей, из которых 9 окрашены.
# Рабочий случайным образом извлекает 3 детали. Какова вероятность того, что все 3 извлеченные детали окрашены?

from math import factorial as fact

detailsNum = 15
coloredDetails = 9
draw = 3


def factorialFunc(num, draw):
    res = fact(num) / (fact(draw) * fact(num - draw))
    return res


coloredDetailsDrawNum = factorialFunc(coloredDetails, draw)
generalDrawNum = factorialFunc(detailsNum, draw)
resultingProbability = round(coloredDetailsDrawNum / generalDrawNum * 100, 1)
print(f'Вероятность того, что все 3 извлеченные детали окрашены равна {resultingProbability}%')
