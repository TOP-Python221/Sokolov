a = input()
b = input()
c = 'abcdefgh'
#d = ['12345678']
if (((c.index(a[0]))%2==0) + (int(a[1])%2==0)) == (((c.index(b[0]))%2==0) + (int(b[1])%2==0)):
    print('YES')
else: 
    print('NO')
 