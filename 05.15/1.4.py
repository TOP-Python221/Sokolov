a = [int(i) for i in input("Введите номер билета: ")]
print(["Нет","Да"][sum(a[:3]) == sum(a[3:])])