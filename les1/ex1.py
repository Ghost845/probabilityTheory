import numpy as np
# np.random.seed(1)
# n = 60
# b = np.random.randint(1, 7, n)
# print(b)
# a = b[b == 3]
# print(a)
# m = len(a)
# print(m)
# w = m/n
# print(w)

from math import factorial


def combinations(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n-k))


print(combinations(36, 4))