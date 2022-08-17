n = input("Введите адрес: ")
if n.find('@') != -1 and n.find('.') != -1:
    print('Верно')
else:
    print('Неверно')