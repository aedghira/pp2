#ITERATORS AND EXAMPLES TO THEM
#Example on W3schools

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#My own examples
#1
flowers = ['peony', 'rose', 'orchid', 'chamomile']
my_iter = iter(flowers)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#2
colour = ('black', 'yellow', 'blue', 'ivory', 'pink', 'purple')
my_iter = iter(colour)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#3
cities = ['Almaty', 'Peru', 'Bangladesh', 'Bali', 'Toronto']
my_iter = iter(cities)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#4
snacks = ['chips', 'soda', 'chocolate', 'fruits', 'grains', 'smoothies']
my_iter = iter(snacks)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#5
names = ('Algida', 'Emir', 'David', 'Zeyne')
my_iter = iter(names)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


#Example on W3schools
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
   print(x)

#My own examples
#1
a = (1, 2, 3, 4, 5, 6)

for x in a:
   print(x)

#2
a = ['a', 'ai', 'aid', 'aida']

for x in a:
   print(x)

#3
a = ('error', 'misclick', 'misunderstanding')

for x in a:
   print(x)

#4
a = ['sun', 'wind', 'water', 'air']

for x in a:
   print(x)
   
#5


#Example on W3schools
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#My own examples
#1
class square:
   def __iter__(self):
      self.a = 1
      return self

   def __next__(self):
      x = self.a
      self.a **= 2
      return x

a = square()
b = iter(a)

print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

#2
class sum_of_squares:
   def __iter__(self):
      self.a = 1
      self.b = int(input())
      return self

   def __next__(self):
      x = self.a
      self.b += 1
      self.a = (self.a + self.b) ** 2
      return x

a = sum_of_squares()
b = iter(a)

print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

#3
class root:
   def __iter__(self):
      self.a = 1
      return self

   def __next__(self):
      x = self.a
      self.a += 1
      self.a = self.a ** (1 / self.a)
      return x

a = root()
b = iter(a)

print(next(b))
print(next(b))

#4
class average_value:
   def __iter__(self):
      self.a = 1
      return self

   def __next__(self):
      x = self.a
      self.a += 1
      return x // 2
      

a = average_value()
b = iter(a)

print(next(b))
print(next(b))

#5
class divisor:
   def __iter__(self):
      self.a = 1
      return self

   def __next__(self):
      x = self.a
      self.a += 8
      self.a //= 4
      return x

a = divisor()
b = iter(a)

print(next(b))
print(next(b))
print(next(b))


#GENERATORS AND EXAMPLES TO THEM

#Example on geeksforgeeeks
def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)
for n in ctr:
    print(n)

#My own examples
#1
def function(max):
    cnt = 0
    while cnt < max:
        yield cnt
        cnt += 3

x = int(input())
ctr = function(x)
for n in ctr:
    print(n)

#2
def func(max):
    cnt = 2
    while cnt <= max:
        yield cnt
        cnt **= cnt

ctr = func(8)
for n in ctr:
    print(n)

#3
def my_fun(min):
    cnt = int(input())
    while cnt >= min:
        yield cnt
        cnt -= 1

a = int(input())
ctr = my_fun(a)
for n in ctr:
    print(n)

#4
def funct(m):
    cnt = 96
    while cnt % m == 0:
        yield cnt
        cnt //= m

ctr = funct(4)
for n in ctr:
    print(n)

#5
def functi(m):
    cnt = 1
    while cnt % 2 == m:
        yield cnt
        cnt += 1

ctr = functi(1)
for n in ctr:
    print(n)

#Example on geeksforgeeks
def fun():
    yield 1            
    yield 2            
    yield 3            
 
# Driver code to check above generator function
for val in fun(): 
    print(val)

#My own examples
#1
def fun():
    yield 10           
    yield 20           
    yield 30            
 
for val in fun(): 
    print(val)

#2
def fun():
    yield 10           
    yield 20           
    yield 30            
 
for val in fun(): 
    print(val)

#3
def fun():
    yield 1           
    yield 210           
    yield 39            
 
for val in fun(): 
    print(val)

#4
def fun():
    yield 1         
    yield 0        
    yield 1            
 
for val in fun(): 
    print(val)

#5
def fun():
    yield 45           
    yield 90           
    yield 135            
 
for val in fun(): 
    print(val)


#Example on W3schools
sq = (x*x for x in range(1, 6))
for i in sq:
    print(i)

#My own examples
#1
roo = (x**3 for x in range(1, 5))
for i in roo:
    print(i)

#2
c = (x**(0.25) for x in range(1, 4))
for i in c:
    print(i)

#3
d = (x**(0.5) for x in range(1, 3))
for i in d:
    print(i)

#4
e = (x*5 for x in range(1, 8))
for i in e:
    print(i)

#5
f = (x//5 for x in range(1, 7))
for i in f:
    print(i)