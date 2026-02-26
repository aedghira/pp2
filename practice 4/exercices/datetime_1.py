#Write a Python program to subtract five days from current date
from datetime import date, timedelta

x = date.today()
y = x - timedelta(days=5)

print(y)

