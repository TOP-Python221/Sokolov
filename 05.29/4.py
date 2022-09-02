vvod = input('Введите строку: ').split()
res = {}
for i in vvod:
    if i in res:
        print(f'{i}_{res.get(i)}',end = ' ')
    else:
        print(i,end = ' ')
    res[i] = res.get(i, 1) + 1



# Введите строку:
# 1.py 1.py aux.h main.cpp functions.h main.cpp 2.py main.cpp
# Вывод:
# 1.py 1.py_2 aux.h main.cpp functions.h main.cpp_2 2.py main.cpp_3
