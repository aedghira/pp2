#Example on W3schools
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#My own examples
#1
def myf(*a):
  print('Our neighbor is ' + a[1])

myf('Emily', 'Raya', 'Edward')

#2
def a(*num):
  print('The winning lottery is in the number', num[3])

a(654, 211, 145, 999, 876)

#3
def b(*s):
  print('We bought a new', s[0])

b('Porsche', 'Koenigsegg', 'Lamborghini', 'Ferrari', 'Maserati', 'Mclaren')

#4
def uf(*d):
  print('You were amazing at the', d[2])

uf('theatre', 'concert', 'Gala-dinner', 'show')

#5
def my(*error):
  print('We have an error:', error[1])

my('car is broken', 'mom wants to beat us', 'our otchid is died')


#Example on W3schools
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

#My own examples
#1
def my_func(meeting, *guests):
  for guest in guests:
    print(meeting, guest)

my_func('Wedding guests:', 'Holand and Mary', 'Kevin and Jannet', 'Ian and Samanta', 'John and Teymi')

#2
def my_func(h, *names):
  for name in names:
    print(h, name)

my_func('How are you,', 'Toby', 'Bill', 'Mina', 'Ernes')

#3
def my_func(subject, *grades):
  for grade in grades:
    print(subject, grade)

my_func('Math:', 5, 8, 9, 10, 6, 10, 8, 3)

#4
def my_func(part, *flowers):
  for flower in flowers:
    print(part, flower)

my_func('Garden:', 'rose', 'peony', 'orchid','chamomile')

#5
def my_func(science, *topics):
  for topic in topics:
    print(science, topic)

my_func('Physics:', 'mechanics', 'quantum section', 'termodynamics', 'magnetism', 'electricity')


#Example on W3schools
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#My own examples
#1
def my_function(*numbers):
  total = 1000
  for num in numbers:
    total -= num
  return total

print(my_function(11, 25, 6))
print(my_function(10, 2, 30, 4))
print(my_function(59))

#2
def my_function(*numbers):
  total = 10000000
  for num in numbers:
    total //= num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#3
def my_function(*numbers):
  total = 1034567
  for num in numbers:
    total %= num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#4
def my_function(*numbers):
  total = 9
  for num in numbers:
    total *= num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#5
def my_function(*numbers):
  total = 1
  for num in numbers:
    total **= num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


#Example on W3schools
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#My own examples
#1
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#2
def my_function(**me):
  print("Her last name is " + me["lname"])

my_function(fname = "Algida", lname = "Asylkhan")

#3
def my_function(**hobby):
  print("Her favorite hobby is " + hobby["art"])

my_function(coding = "python", art = "painting")

#4
def my_function(**me):
  print("She is  " + me["age"])

my_function(specialty = "engineer", age = "18")

#5
def my_function(**me):
  print("Her favourite subject is " + me["subject"])

my_function(movie = "Waves of life", subject = "physics")


#Example on W3schools
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

#My own examples
#1
def my_function(a, b, c):
  return a * b * c

numbers = [1, 35, 4]
result = my_function(*numbers)
print(result)

#2
def my_function(a, b, c):
  return a + b - c

numbers = [100, 17, 31]
result = my_function(*numbers)
print(result)

#3
def my_function(a, b, c):
  return a // b // c

numbers = [111, 21, 3]
result = my_function(*numbers)
print(result)

#4
def my_function(a, b, c):
  return a % b % c

numbers = [893, 24, 7]
result = my_function(*numbers)
print(result)

#5
def my_function(a, b, c):
  return a + b + c

numbers = [100, 200, 300]
result = my_function(*numbers)
print(result)