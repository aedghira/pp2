#Write a Python program to print yesterday, today, tomorrow.

from datetime import date, timedelta

x = date.today()

print(x - timedelta(days=1))
print(x)
print(x + timedelta(days=1))
