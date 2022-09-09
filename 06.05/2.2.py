from random import choice, sample

list1 = ['evil', 'dobro', 'telephone', 'oracle']

lis = choice(list1)
lisMix = sample(lis, k=len(lis))

print('Загаданное слово: ' + ''.join(lisMix))

while True:
    guess = input('Введите своё слово: ')
    if guess == lis:
        print('Вы угадали! \nХотите ещё раз?')
        what = input("Ваш ответ: ")
        if what == "да":
            lis = choice(list1)
            lisMix = sample(lis, k=len(lis))
            print('Загаданное слово: ' + ''.join(lisMix))
            continue
        else:
            break
    else:
        print('Вы не угадали поробуте еще раз')

