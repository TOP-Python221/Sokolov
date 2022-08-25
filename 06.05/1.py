from random import randrange

list_1 = []
for i in range(10):
    list_1.append(randrange(0, 10))
list_2 = []
for i in range(10):
    list_2.append(randrange(0, 10))

for i in range(list_1):
    for j in range(list_2):
        if i == j:
            list_1.pop(i) and list_2.pop(j)

print(list_1)
print(list_2)