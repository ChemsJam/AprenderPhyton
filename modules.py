#datetime
from datetime import timedelta, date

print(date.today())

print(timedelta(minutes=70))

from fmath import add, substract

add(1,2)
substract(3,5)

from colorama import Fore, Style, init
init(convert=True)
print(Fore.Red + "Hello world")