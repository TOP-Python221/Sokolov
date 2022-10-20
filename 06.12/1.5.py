def Iter(a):
    """Вычисляем набор средних значений итерируемого объекта"""


    if a == type(str):
        a.isdigit()
        return a.split(' ')
    sr_arif = 0

    for a in range(a):
        sr_arif = (a[0] + a[1]) / 2
    print(sr_arif)

    sr_geom = 0
    for a in range(a):
        sr_geom = (a[0] * a[1]) ** 0.5
    print(sr_geom)

    sr_harm = 0
    for a in range(a):
        sr_harm = (1/a[0] + 1/a[1]) /2
    print(sr_harm)

    sr_quadr = 0
    for a in range(a):
        sr_quadr = ((a[0]**2 + a[1]**2)**0.5) / 2
    print(sr_quadr)

    if a == type(list) or type(tuple):
            return None
print(Iter('52423'))
#

#застзастрял на решении, почему-то выводит только None