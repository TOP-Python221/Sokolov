TEXT = """Однажды, в студёную зимнюю пору
Я из лесу вышел; был сильный мороз.
Гляжу, поднимается медленно в гору
Лошадка, везущая хворосту воз.
И, шествуя важно, в спокойствии чинном,
Лошадку ведёт под уздцы мужичок
В больших сапогах, в полушубке овчинном,
В больших рукавицах... а сам с ноготок!
«Здорово, парнище!» — «Ступай себе мимо!» —
«Уж больно ты грозен, как я погляжу!
Откуда дровишки?» — «Из лесу, вестимо,
Отец, слышишь, рубит, а я отвожу».
(В лесу раздавался топор дровосека.) —
«А что, у отца-то большая семья?» —
«Семья-то большая, да два человека
Всего мужиков-то: отец мой да я...» —
«Так вон оно что! А как звать тебя?» — «Власом». —
«А кой тебе годик?» — «Шестой миновал...
Ну, мёртвая!» — крикнул малюточка басом,
Рванул под уздцы и быстрей зашагал...
На эту картину так солнце светило,
Ребёнок был так уморительно мал,
Как будто всё это картонное было,
Как будто бы в детский театр я попал.
Но мальчик был мальчик живой, настоящий,
И дровни, и хворост, и пегонький конь,
И снег до окошек деревни лежащий,
И зимнего солнца холодный огонь —
Всё, всё настоящее русское было,
С клеймом нелюдимой, мертвящей зимы,
Что русской душе так мучительно мило,
Что русские мысли вселяет в умы, —
Те честные мысли, которым нет доли,
Которым нет смерти —
В которых так много и злобы и боли,
В которых так много любви!"""

words = TEXT.split()
print(len(words)) # Вывести на экран количество слов
print(len("".join(words))) # Вывести на экран количество символов
wordsdict = {}
for word in words:
    word = word.lower().strip('"').strip("(").strip("!").strip("«").rstrip("...»").strip(",")
    if word not in wordsdict:
        wordsdict[word] = 1
    else:
        wordsdict[word] = wordsdict[word] + 1

wordslist = sorted(wordsdict.items(), key=lambda x: x[1], reverse=True)
print(wordslist)

longest = ""
wordsfreq = []
for word in wordsdict:
    wordsfreq.append((word, wordsdict[word]))
    if len(word) > len(longest):
        longest = word

wordsfreq.sort(key=lambda row: row[1], reverse=True)
print(wordsfreq == wordslist)

dct = {}
for word in wordsfreq:
    dct.update({word[0]: word[1]})
print(dct)