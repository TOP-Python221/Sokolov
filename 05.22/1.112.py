n = list(map(int, input().split()))
print(n)
# УДАЛИТЬ: второй список не нужен, достаточно изменить первый
s = []
if len(n) <= 4:
    print("Введите больше цифр!")
else:
    n.remove(max(n))
    n.remove(min(n))
    s.append(n)
    
print(*s)


# ДОБАВИТЬ: примеры выполнения скрипта в закомментированном виде под меткой tests
# tests:


# ИТОГ: хорошо — 3/3
