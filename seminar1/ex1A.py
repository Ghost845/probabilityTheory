# Задача 1. Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все 4 карты – крести.

# ♣️ Трефы — clubs.
# ♦️ Бубны — diamonds.
# ♥️ Червы — hearts.
# ♠️ Пики — spades

from math import factorial as fact

cardsNum = 52
draw = 4
cardSuit = 4
clubsNum = cardsNum // cardSuit


def factorialFunc(num, draw):
    res = fact(num) // (fact(draw) * fact(num - draw))
    return res


fourClubsProbability = factorialFunc(clubsNum, draw)
generalProbability = factorialFunc(cardsNum, draw)
resultingProbability = round(fourClubsProbability / generalProbability * 100, 3)
print(f'Вероятность того, что все 4 карты – крести равна {resultingProbability}%')
