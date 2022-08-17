a = []
while True:
    b = int(input())
    a.append(b)
    if b % 7 != 0:
        break
for i in a:
    print(i,end=' ')