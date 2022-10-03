def isIteger(s):
    if s.isdigit():
        return "Строка является числом"
    else:
        try:
            float(s)
            return "Строка явялется числом"
        except ValueError:
            return "Строка не является числом"

print(isIteger(input()))



