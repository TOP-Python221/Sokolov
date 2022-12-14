# ИСПРАВИТЬ: метод split() и так возвращает объект list, нет нужды его преобразовывать
larger = list(input().split())
smaller = list(input().split())

# ИСПРАВИТЬ: с учётом того, что объекты входных списков вы далее не используете — то целесообразно не создавать новые переменные, а перезаписывать уже имеющиеся
larger_1 = ' '.join(map(str, larger))
smaller_1 = ' '.join(map(str, smaller))

# КОММЕНТАРИЙ: а вот это хороший вариант использования строкового метода
print(f'\n{bool(larger_1.find(smaller_1) + 1)}')


# tests:
# 56 99 78 33 4896 238 74
# здесь пустой список
# True

# 22 56 17 69 31
# 69 31
# True

# 12 23 45 56
# 12 45
# False


# КОММЕНТАРИЙ: внимательнее к типам используемых объектов: то, что у нас в Python динамическая типизация, даёт нам много возможностей писать очень неоптимальный код — не пользуйтесь ими


# ИТОГ: хорошо — 4/5
