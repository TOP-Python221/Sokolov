dannie = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, \
          "G": 2, "H": 4, "I": 1, "J": 2, "K": 5, "L": 1, \
          "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, \
          "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}
vvod = input('Введите слово: ')
vvod2 = vvod.upper()
count = 0
for i in vvod2:
    count = count + dannie[i]
print(vvod, 'будет', count, 'очков')

# Введите слово: privet
# privet будет 11 очков

# Введите слово: hello
# hello будет 8 очков

# Введите слово: bonjour
# bonjour будет 10 очков
()