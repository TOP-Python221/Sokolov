from datetime import datetime

class Data():
    def __init__(self,
                 data: int,
                 time_zone: int):
        self.data = data
        self.time_zone = time_zone

    def time_zone(self):
        return datetime.datetime.today()

    def future_time(self):
        return datetime.timedelta(days=1)


d1 = Data.time_zone()
print(d1.strftime("%A %d %B %Y"))

d2 = Data.future_time()
print(d2)