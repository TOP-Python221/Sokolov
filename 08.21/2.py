from datetime import datetime


class Date:
    def __init__(self,
                 date: int,
                 time_zone: int):
        self.date = date
        self.time_zone = time_zone

    def time_zone(self):
        return datetime.datetime.today()

    def future_time(self):
        return datetime.timedelta(days=1)


d1 = Date.time_zone()
print(d1.strftime("%A %d %B %Y"))

d2 = Date.future_time()
print(d2)


# ДОБАВИТЬ: примеры выполнения скрипта в закомментированном виде под меткой tests
# tests:
