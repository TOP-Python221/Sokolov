def f(i):
    t = i.split()
    r = ''

    for j in range(len(t)):
        if j < len(t) - 2:
            t[j] = t[j] + ','
            r += t[j]
        elif j == len(t) - 2:
            t[j] = t[j] + ' и '
            r += t[j]
        else:
            r += t[j]
    return r 
i = input()
print(f(i))