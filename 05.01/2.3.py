n = int(input("Введите целое число: "))
s = 0
for i in range(1,n + 1):
    if n % i == 0:
        s += i
        
print(s,end=' ')
    
