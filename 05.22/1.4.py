n = [int(n) for n in input().split()]
count = 0
for i in range(1, len(n)):
    if n[i] > n[i-1]:
        count += 1
print(count)


# Ввод 1 2 3 4 5
# Вывод 4

# Ввод 10 5 20 30 7
# Вывод 2
