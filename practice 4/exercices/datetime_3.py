#Write a Python program to drop microseconds from datetime.

import datetime

s = datetime.datetime.now()
print(s.strftime("%Y-%m-%d %H:%M"))