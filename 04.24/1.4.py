a=int(input())
b=0
c=1
while a > 0:
    d=a%10
    b+=d
    c*=d
    a//=10
print("Сумма цифр =",b)
print("произведение цифр =",c)