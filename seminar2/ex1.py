# Задача 1. Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
# Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.

from math import factorial as fact

hitProbability = 0.8
shotsNum = 100
totalHits = 85


def factorialFunc(shots, hits):
    res = fact(shots) // (fact(hits) * fact(shots - hits))
    return res


probabilityBernoulli = round(factorialFunc(shotsNum, totalHits) * hitProbability ** totalHits * (1 - hitProbability) ** 15 * 100, 2)
print(f'Вероятность того, что стрелок попадет в цель ровно 85 раз равна {probabilityBernoulli}%')
