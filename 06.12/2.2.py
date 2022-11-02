def sound(file_path: str, audioformat: (int, str), channel: (int, str), sample_rates: (int, str), bit_depth: (int, str),) -> object:
    """Обработка звукового файла"""

        # ОТВЕТИТЬ: что объединяет эти четыре параметра и чем они отличаются от параметра, ожидающего путь к файлу?
        # ОТВЕТИТЬ: что такое путь и чем он отличается от той строки, которую передали вы?
        #

    # ИСПОЛЬЗОВАТЬ: вам необходимо проверить корректность всех и каждого переданных аргументов — почему бы по такому случаю не завести словарик?
    checks = {
        'file_path': False,
        'audioformat': False,
        'channel': False,
        'sample_rate': False,
        'bit_depth': False,
    }

    for key in checks.keys():
        checks[key] = True


    audioformats = 0 < audioformat < 10000
    if type(audioformats) is str:
        return int(audioformats)

    channels = 1 < channel < 11
    if type(channels) is str:
        return int(channels)

    sample_rates = [8000, 11025, 16000, 22050, 32000, 44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000]
    for i in sample_rates:
        if sample_rates == [i]:
            return sample_rates

    bit_depths = [8, 16, 24, 32]
    for i in bit_depths:
        if bit_depths == [i]:
            return i

    # ДОБАВИТЬ: а вот здесь уже можно сформировать строку с результатами проверки и наконец-то эту строку вернуть



# тесты
print(sound(15, 8, 11025, 32, '.wav'))

# ДОБАВИТЬ: тесты с некорректными данными
