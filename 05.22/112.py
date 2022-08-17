n = list(map(int,input().split()))
print(n)
s = []
if len(n) <= 4:
    print("Введите больше цифр!")
else:
    n.remove(max(n))
    n.remove(min(n))
    s.append(n)
    
print(*s)