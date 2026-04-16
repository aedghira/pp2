#Example on W3schools
x = lambda a : a + 10
print(x(5))

#My own examples
#1
x = lambda a : a + 99
print(x(7))

#2
x = lambda a : a + 11
print(x(56))

#3
x = lambda a : a + 9
print(x(9))

#4
x = lambda a : a + 1
print(x(18))

#5
x = lambda a : a + 88
print(x(67))

#Example on W3schools
x = lambda a, b : a * b
print(x(5, 6))

#My own examples
#1
x = lambda a, b : a * b
print(x(11, 90))

#2
x = lambda a, b : a * b
print(x(5, 0))

#3
x = lambda a, b : a * b
print(x(1, 6))

#4
x = lambda a, b : a * b
print(x(11, 2))

#5
x = lambda a, b : a * b
print(x(15, 66))


#Example on W3schools
x = lambda a, b, c : a + b + c
print(x(95, 16, 26))

#My own examples
#1
x = lambda a, b, c : a + b + c
print(x(65, 62, 28))

#2
x = lambda a, b, c : a + b + c
print(x(5, 6588, 112))

#3
x = lambda a, b, c : a + b + c
print(x(0, 1, 2))

#4
x = lambda a, b, c : a + b + c
print(x(50, 60, 8))

#5
x = lambda a, b, c : a + b + c
print(x(122, 33, 66))



#Example on W3schools
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#My own examples
#1
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(5)

print(mydoubler(10))
#2
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(21))
#3
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(98888)

print(mydoubler(1))
#4
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(4)

print(mydoubler(6))
#5
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(5)

print(mydoubler(5))
