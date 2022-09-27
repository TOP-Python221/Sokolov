def capitalize(s):
    result = s
    pos = 0
    while pos < len(s) and result[pos] == ' ':
        pos = pos + 1
    if pos < len(s):
        result = result[0:pos] + result[pos].upper() + result[pos + 1 : len(result)]
    pos = 0
    while pos < len(s):
        if result[pos] == "." or result[pos] == "!" or result[pos] == "?":
            pos = pos + 1
            while pos < len(s) and result[pos] == " ":
                pos = pos + 1

        if pos < len(s):
            result = result[0:pos] + result[pos].upper() + result[pos + 1 : len(result)]
            pos = pos + 1

    pos = 1
    while pos < len(s) - 1:
        if result[pos - 1] == " " and result[pos] == "i" and (result[pos + 1] == " " or result[pos + 1] == "." or
                 result[pos + 1] == "!" or result[pos + 1] == "?" or
                 result[pos + 1] == "'"):
            pos = pos + 1
    return result

def main():
    s = input("Введите текст: ")
    capitalized = capitalize(s)
    print(capitalized)

main()

