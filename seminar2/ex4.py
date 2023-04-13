# Задача 4. В первом ящике находится 10 мячей, из которых 7 - белые.
# Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча.
# Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые?
# Какова вероятность того, что хотя бы один мяч белый?

from math import factorial as fact

firstBox = 10
firstWhiteBalls = 7
secondBox = 11
secondWhiteBalls = 9
drawNum = 2
oneBlackBall = 1
twoBlackBall = 2


def factorialFunc(shots, hits):
    res = fact(shots) // (fact(hits) * fact(shots - hits))
    return res


def probabilities(a, b, c, d):
    res = factorialFunc(a, b) / factorialFunc(c, d)
    return res


allWhite = round((factorialFunc(firstWhiteBalls, drawNum) / factorialFunc(firstBox, drawNum))
                 * (factorialFunc(secondWhiteBalls, drawNum) / factorialFunc(secondBox, drawNum)) * 100, 1)
twoWhite = round((((7 / 10) * (6 / 9) * (2 / 11) * (1 / 10)) + ((7 / 10) * (3 / 9) * (9 / 11) * (2 / 10)) + ((7 / 10) * (3 / 9) * (2 / 11) * (9 / 10)) +
                  ((3 / 10) * (7 / 9) * (9 / 11) * (2 / 10)) + ((3 / 10) * (7 / 9) *
                                                                (2 / 11) * (9 / 10)) + ((3 / 10) * (2 / 9) * (9 / 11) * (8 / 10))) * 100, 3)
ifOnlyOneWhite = round((1 - ((3 / 10) * (2 / 9) * (2 / 11) * (1 / 10))) * 100, 2)
print(
    f'Вероятность того, что все мячи белые равна {allWhite}%\nВероятность того, что ровно два мяча белые равна {twoWhite}%\nВероятность того, что хотя бы один мяч белый равна {ifOnlyOneWhite}%')
