#Write a Python program to convert degree to radian.

import math

degree = int(input())

print(math.radians(degree))

#Write a Python program to calculate the area of a trapezoid

height = int(input())
base_1 = int(input())
base_2 = int(input())

S = ((base_1 + base_2) / 2) * height
print(S)

#Write a Python program to calculate the area of regular polygon

n = int(input())
length = int(input())

print(int((0.25 * n * (length ** 2)) // (math.tan(math.pi / n))))

#Write a Python program to calculate the area of a parallelogram

h = int(input())
a = int(input())

print(float(h * a))