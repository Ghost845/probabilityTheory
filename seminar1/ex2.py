# Задача 2. На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
# Код содержит три цифры, которые нужно нажать одновременно .
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?
# Размещение

from math import factorial as fact

numbersCount = 10
codeChars = 3
triesNumber = 1


def factorialFunc(num, chars):
    res = fact(num) / fact(num - chars)
    return res


placementNum = round(triesNumber / factorialFunc(numbersCount, codeChars) * 100, 2)
print(
    f'Вероятность того, что человек, не знающий код, откроет дверь с первой попытки равна {placementNum}%')
