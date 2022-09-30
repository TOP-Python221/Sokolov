n = [int(n) for n in input().split()]
# count = 0
# for i in range(1, len(n)):
#     if n[i] > n[i-1]:
#         count += 1
# ИСПОЛЬЗОВАТЬ: этот цикл также можно было заменить представлением списка и встроенной функцией:
count = sum([1 for i in range(1, len(n)) if n[i-1] < n[i]])
print(count)


# tests:
# Ввод 1 2 3 4 5
# Вывод 4

# Ввод 10 5 20 30 7
# Вывод 2


# ИТОГ: хорошо — 3/3
