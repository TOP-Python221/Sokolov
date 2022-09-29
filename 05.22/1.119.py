s = ['0']
while n := input():
    s.append(n)
if s != ['0']:
    s.remove('0')
    a = sum(map(float, s)) / len(s)
    print(f'\nСреднее зн.{a}'
          f'\nНиже среднего{[int(i) for i in s if float(i) < a]}'
          f'\nРавный среднему{[int(i) for i in s if float(i) == a]}'
          f'\nВыше среднего{[int(i) for i in s if float(i) > a]}')
