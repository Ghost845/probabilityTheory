# Задача 3. Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

from math import factorial as fact

throwNum = 144
headsProb = 0.5
tailsProb = 1 - headsProb
headsObjProb = 70


def factorialFunc(shots, hits):
    res = fact(shots) // (fact(hits) * fact(shots - hits))
    return res


res = round(factorialFunc(throwNum, headsObjProb) * headsProb ** headsObjProb * tailsProb ** (throwNum - headsObjProb) * 100, 2)
print(f'Вероятность того, что орел выпадет ровно 70 раз равна {res}%')
