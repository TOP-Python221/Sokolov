# a = [int(i) for i in input("Введите номер билета: ")]
# print(["Нет","Да"][sum(a[:3]) == sum(a[3:])])

b = 1
c = 999999
count = 0
for a in range(b, c + 1):
    a = str(a)
    if sum(map(int, a[-3:])) == sum(map(int, a[:-3])):
        count += 1
print(count)