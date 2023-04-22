# Задача 1.
# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое,
# среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

import numpy as np

arr = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
arrLength = len(arr)
newArr = sorted(arr)

sum = 0
for i in range(arrLength):
    sum += arr[i]
avg = sum / arrLength

meanSquareDeviation = round(np.sqrt(np.sum((newArr - avg) ** 2) / arrLength), 2)
shiftedDispersion = round(np.sum((newArr - avg) ** 2) / arrLength, 2)
nonShiftedDispersion = round(np.sum((newArr - avg) ** 2) / (arrLength - 1), 2)

print(f'Среднее арифметическое - {avg}')
print(f'Среднее квадратичное отклонение - {meanSquareDeviation}')
print(f'Смещённая дисперсия - {shiftedDispersion}')
print(f'Несмещённая дисперсия - {nonShiftedDispersion}')