from random import randrange

s_1 = []
for i in range(10):
    s_1.append(randrange(0, 10))
s_2 = []
for i in range(10):
    s_2.append(randrange(0, 10))

print(list(set(s_1)-set(s_2)))
