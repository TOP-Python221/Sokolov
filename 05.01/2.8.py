a = 1
b = 1
n = int(input())
print(a,b,end=' ')
for i in range(2,n):
    a,b = b,a + b
    print(b, end=' ')
    n -= 1
