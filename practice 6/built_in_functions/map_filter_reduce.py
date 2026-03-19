#Examples for function 'map()'

list_1 = list(map(int, input().split()))

squares = list(map(lambda x: x ** 2, list_1 ))
print(squares)

summ = list(map(lambda y: y + 100, list_1))
print(summ)

#Examples for function 'filter()'

odd = list(filter(lambda z: z % 2 != 0, list_1))

a = list(filter(lambda k: k > 7, list_1))

print(odd)
print(a)
#Examples for function 'reduce()'
from functools import reduce 

b = reduce(lambda i, j: i + j, list_1)

c = reduce(lambda p, t: p * t, list_1 )

print(b)
print(c)
