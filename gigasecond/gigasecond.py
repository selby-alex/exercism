from datetime import datetime
from datetime import timedelta


def add_gigasecond(date):
    age = date + timedelta(seconds=10**9)
    print(age)
    return(age)

    