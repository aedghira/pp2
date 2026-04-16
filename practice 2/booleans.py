#Example on w3schools
print(10 > 9)
print(10 == 9)
print(10 < 9)
#my own examples
#1
print(8 <= 10)
#2
print(7 < 6)
#3
print(8 == 8)
#4
print(9 > 6)
#5
print(11 < 12)

#Example on w3schools
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#my own examples
#1
a = 3
b = 4
if a < b:
  print('a is less than b')
elif a == b:
  print('a is equal to b')  
else:
  print('a is greater than b')  
#2
a = 3
if a >= 3:
  print('Known that a is greater or equal to 3')       
else:
  print('Known that a is not greater than 3')   
#3
age = int(input()) 
if age >= 18:
  print('We can sell you this product because you are an adult')
else:
  print('We can not sell you this product because you are not an adult') 
#4
number = int(input())   
if number == 999:
  print('You are so lucky!You win the lottery')
else:
  print('Sorry,you did not win the lottery(((((') 
 #5
apples = int(input())
bananas = int(input())
counter = apples + bananas
if counter > 10:
  print('We have more than 10 fruits!')
else:
  print('We do not have more than 10 fruits(((')  

#example on w3schools
print(bool("Hello"))
print(bool(15))
#my own examples
#1
print(bool(''))
#2
print(bool(22222))
#3
print(bool(0))
#4
print(bool('wow'))
#5
print(bool('aaaaaa'))

#example on w3schools
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#my own examples
#1
a, b = 2, 5
print(bool(a), bool(b))
#2
a = 44
b = 'python'
print(bool(a))
print(bool(b))
#3
a = int(input())
if a:
  print(bool(1))
else:
  print(bool(0))  
#4
a = 1111
if a:
  print(bool(0))  
else:
  print(bool(1))
#5
a = int(input())
b = int(input())
if a and b:
  print(bool(1))  
else:
  print(bool(0))

#Example on w3schools
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#my own examples
#1
bool('1111111') 
#2
bool('')
#3
bool(22222222)
#4
bool(0)
#5
bool("apple3")

#Example on w3schools
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
#my own examples
#1
class a():
  def __len__(b):
    return 1
w = a()
print(bool(w))
#2
class a():
  def __len__(thing):
    return 4444
w = a()
print(bool(w))
#3
class a():
  def __len__(t):
    return 12
c = a()
print(bool(c))  
#4
class b():
  def __len__(see):
    return 0;
q = b()
print(bool(b))
#5
class b():
  def __len__(f):
    return 0
class a():
  def __len__(r):
    return 1
q = a()  
s = b()
print(bool(q), bool(s))

#Example on w3schools
def myFunction() :
  return True

print(myFunction())
#my own examples
#1
def f():
  return False
print(f())
#2
def a():
  return 1
print(bool(a()))
#3
def a():
  return True
print(a())
#4
def f():
  return 1111
print(bool(f()))
#5
def a():
  return 0
print(bool(a()))

#Example on w3schools
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
#my own examples
#1
def a() :
  return 1

if bool(a()):
  print("YES!")
else:
  print("NO!")
#2
def a():
  return False

if a():
  print('Oh,nooo!')
else:
  print('Yeeees!')
#3
def a():
  b = int(input())
  return b

if a() >= 1111:
  print('WOW')
else:
  print('It is so sad((((')
#4
def a():
  b = 0
  return b

print(bool(a()))
#5
def b():
  return False

if b():
  print('THANK YOUUUU')
else:
  print('No needs to apologize') 

#Example on w3schools
x = 200
print(isinstance(x, int))
#my own examples
#1
x = 'hello' 
b = 'hola'
c = 'привет'
d = 'сәлем'
print(isinstance(x, str))
print(isinstance(b, str))
print(isinstance(c, str))
print(isinstance(d, str))
#2
a = 12
print(isinstance(a, str))
#3
a = '13'
print(isinstance(a, int))
#4
a = 11
print(isinstance(a, int))
#5
a = 33
if isinstance(a, int):
  print('WELL')
else:
  print('Ohh(((')  