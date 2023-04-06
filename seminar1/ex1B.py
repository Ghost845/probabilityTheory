# Задача 1. Из колоды в 52 карты извлекаются случайным образом 4 карты.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

# ♣️ Трефы — clubs.
# ♦️ Бубны — diamonds.
# ♥️ Червы — hearts.
# ♠️ Пики — spades

from math import factorial as fact

cardsNum = 52


def factorialFunc(num, draw):
    res = fact(num) / (fact(draw) * fact(num - draw))
    return res


oneAceProbability = (factorialFunc(
    4, 1) * factorialFunc(48, 3) / factorialFunc(cardsNum, 4))
twoAceProbability = (factorialFunc(
    4, 2) * factorialFunc(48, 2) / factorialFunc(cardsNum, 4))
threeAceProbability = (factorialFunc(
    4, 3) * factorialFunc(48, 1) / factorialFunc(cardsNum, 4))
fourAceProbability = (factorialFunc(
    4, 4) * factorialFunc(48, 0) / factorialFunc(cardsNum, 4))
resultingProbability = round((
    oneAceProbability + twoAceProbability + threeAceProbability + fourAceProbability) * 100, 2)

print(
    f'Вероятность того, что среди 4-х карт окажется хотя бы один туз равна {resultingProbability}%')
