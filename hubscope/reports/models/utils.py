from datetime import  datetime, timedelta, date
from django.utils.timezone import localdate


class DayRange:
  
    def __init__(self, b, e=None):
        if b.__class__ == datetime:
            self.begin = b.date()
        else:
            self.begin = b

        if e is None:
            self.end = localdate()
        elif e.__class__ == datetime:
            self.end = e.date()
        else:
            self.end = e
    @property
    def size(self):
        return  (self.end - self.begin).days + 1

    @property
    def days(self):
        return [ self.begin + timedelta(days=i) for i in range(self.size) ]

    def includes(self, date):
        return self.begin <= date <= self.end
