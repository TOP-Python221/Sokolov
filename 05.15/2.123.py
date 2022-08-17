s = input()

words = s.split()
words_new = []
for w in words:
    w_new = []
    for a in w:
        if a in ',.?!':
            w_new.append(a)
    words_new.append(w_new)
# print(words_new)

str_out = ''

for i in range(len(words)):
    words[i] = words[i].strip(',.?!')
    if words[i][0].lower() in 'aeiou':
        words[i] += 'way' + ''.join(words_new[i]) + ' '
        str_out += words[i]
    else:
        for j in words[i]:
            if j.lower() in 'aeiou':
                n = words[i].index(j)
                if words[i][0].isupper():
                    words[i] = words[i][n:n+1].upper() + words[i][n+1:] + words[i][0].lower() + words[i][1:n] + 'ay' + ''.join(words_new[i]) + ' '
                else:
                    words[i] = words[i][n:] + words[i][:n] + 'ay' + ''.join(words_new[i]) + ' '
                str_out += words[i]
                break

print(str_out)
