n = [n.strip('.,:;?!-()"\'') for n in input().lower().split()]
print(n)
if n[0] == n[-1]:
     print("Паллиндром")
else:
     print("Данное вырвжение паллиндроммом не является")
# Is it crazy how saying sentences backwards creates backwards
# sentences saying how crazy it is?

#['is', 'it', 'crazy', 'how', 'saying', 'sentences', 'backwards', 'creaters', 'backwards', 'sentences', 'saying', 'how', 'crazy', 'it', 'is']
#Паллиндром