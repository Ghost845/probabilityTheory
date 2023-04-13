# Задача 2. Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
# Какова вероятность, что ни одна из этих 5000 лампочек не перегорит в первый день?
# Какова вероятность, что перегорят ровно две?

from math import factorial as fact

blowProbability = 0.0004
lampNum = 5000
firstGoal = 0
secondGoal = 2
eConst = 2.71828
poissonsLambda = blowProbability * lampNum

firstGoalProb = round(poissonsLambda ** firstGoal / fact(firstGoal) * (1 / eConst ** poissonsLambda) * 100, 1)
secondGoalProb = round(poissonsLambda ** secondGoal / fact(secondGoal) * (1 / eConst ** poissonsLambda) * 100, 1)
print(
    f'Вероятность того, что ни одна из этих 5000 лампочек не перегорит в первый день равна {firstGoalProb}%\nВероятность того, что перегорят ровно две равна {secondGoalProb}%')
