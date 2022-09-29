otr = []
pol = []
nol = []

n = list(map(int,input().split()))
for i in n:
    if i < 0:
        otr.append(i)
    elif i > 0:
        pol.append(i)
    elif i == 0:
        nol.append(i)

print(*otr,*nol,*pol,sep='\n')
