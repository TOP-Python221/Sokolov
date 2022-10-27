


def sound(a, d, d1, r, w='.wav') ->  str:
    """Обработка звукового файла"""
    audio_form = list(range(0, 10000))
    a = input()

    if a in audio_form:
        return a

    diap = list(range(1, 11))
    d = int(input())
    if d in diap:
        return d

    discret = [8000, 11025, 16000, 22050, 32000, 44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000]
    d1 = int(input())
    if d1 in discret:
        return d1

    razr = [8, 16, 24, 32]
    r = int(input())
    if r in razr:
        return r


sound(15, 8, 11025, 32, '.wav')
print(str(sound()))

# считаю что последний переданный аргумент должен быть строго определен, потому как это условие
