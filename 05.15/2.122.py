n = input().lower().split()
vowels = 'aeoiu'
d = ''
for i in n:
    if i[0] in vowels:
        i += 'way '
        d += i
    else:
         for y in i:
             if y in vowels:
                 s = i.index(y)
                 i = i[s:] + i[:s] + 'ay '
                 d += i
                 break
print(d)




