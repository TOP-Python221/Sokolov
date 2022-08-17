a = ord(input()) - 96
b = int(input())
c = ord(input()) - 96
d = int(input())
if abs(a - c) > 1 or abs(b - d) > 1:
    print("Нет")
else:
    print("ДА") 


