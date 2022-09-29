from random import choice


count_1 = 0
for i in range(11):
    res = ''
    count = 0
    while True:
        res += choice(('О', 'Р')) + ''
        count_1 += 1
        count += 1
        if 'Р Р Р' in res or 'О О О' in res:
            break
    print(f'{res}(попыток: {count})')
print(f'Среднее количество попыток: {count_1/10})')


# O O O (попыток: 3)
# P P P (попыток: 3)
# O P P O P O O O (попыток: 8)
# P P P (попыток: 3)
# O O P O O P O O O (попыток: 9)
# O P O P P P (попыток: 6)
# O O P O O O (попыток: 6)
# P P P (попыток: 3)
# P P P (попыток: 3)
# P P O P P O O O (попыток: 8)
# Среднее количество попыток: 5.2)
