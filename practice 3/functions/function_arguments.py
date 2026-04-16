#Example on W3schools
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#My own examples
#1
def my(name):
  print(name + 'Asylkhan')

my('Algida')
my('Aida')
my('Qaraqat')
my('Ulzhalgas')
my('Khanshayim')

#2
def day(time):
  print(time + '16.02.2026')

day('12 pm')
day('5 am')
day('8 pm')

#3
def book(b):
  print(b + 'by Anna Jane')

book('Восхитительная ведьма')
book('Влюбленная ведьма')
book('По осколкам твоего сердца')

#4
def function(s):
  print(s , 'is a number')

function(12)
function(33333)
function(1)
  
#5
def dance(style):
  print(style + 'is amazing!!!!!!!!!!')

dance('Tango')
dance('hip - hop')
dance('street style')


#Example on W3schools
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#My own example
#1
def lottery(name, num):
  print(name, num)

lottery('Anna', 23)

#2
def practice(work, defence):
  print(defence, work)

practice('Engineer', 'nuclear energy')

#3
def music(fave, singer):
  print(singer, fave)

music('Yeah!', 'Usher, Lil Jon, Ludacris')

#4
def root(num):
  print(num, 'is square root of', num ** 2)

root(8)

#5
def architecture(style):
  print(style, 'looks great')

architecture('Minimalism')


#Example on W3schools
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

#My own examples
#1
def technologies(brand, type):
  print('I have amazing', type)
  print('My', type, 'was made by', brand)

technologies(brand = 'Samsung', type = 'microwave')

#2
def bags(brand_1, brand_2):
  print('I have bags from', brand_1, brand_2)

bags(brand_1 = 'Chanel', brand_2 = 'Dior')

#3
def classes(first, second):
  print('My eldest son studies at', first)
  print('My yuongest studies at', second)

classes(first = '11th grade', second = '6th grade')

#4
def workers(num1, num2):
  print(num1, 'works in BI group company as a programmist')
  print(num2, 'works as a developer')

workers(num1 = 'Mary', num2 = 'Jane')

#5
def floors(n, a):
  print('Jhonatan lives in a', n, 'floor')
  print('Sierra lives in a', a, 'floor')

floors(11, 28)

#Example on W3schools
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")

#My own examples
#1
def my_function(animal, age):
  print("I have a", animal)
  print("My", animal + "'s name is", age, 'years old')

my_function('cat', '2')

#2
def my_function(book, author):
  print("I have a book", book)
  print('Author of this book is', author)

my_function('Ten negritos', 'Agatha Christie')

#3
def my_function(hobby, n):
  print('My hobby is', hobby)
  print('I do', hobby, 'for about', n, 'years')

my_function("art", "10")

#4
def my_function(name, birthday):
  print('My name is', name)
  print('My birthday is', birthday)

my_function("Algida", "23 january")

#5
def my_function(car, brand):
  print('I want to buy a new', car)
  print('My dream car is', brand)

my_function("sportcar", "Koenigsegg")

#Example on W3schools
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

#My own examples
#1
def my_function(art, author, age):
  print(author, 'draw', art, 'at', age, 'years old')

my_function("Leonardo da Vinci", author = "Mona Lisa", age = 51)

#2
def my_function(luck, amount, num):
  print('Oh, you have', amount, 'lotteries.I hope you can win with the', num, 'You', luck)

my_function('won!!!!', amount = 4, num = 666)

#3
def my_function(snack, soda, chocolate):
  print('I have', snack, soda, 'and', chocolate)

my_function('chips', chocolate = 'Hersheys', soda = 'Cola')

#4
def my_function(worker, company,  experience):
  print('I have worked as a', worker, 'in a', company, 'for about', experience, 'years')

my_function('builder', company = 'BI group', experience = '11')

#5
def my_function(consumer, product, cost):
  print('Our consumer named', consumer, 'bought a', product, 'which costs', cost, 'dollars')

my_function("Alaina", product = "TV", cost = '2500 dollars') #yeah, she is rich-rich)))))))

#Example on W3schools
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#My own examples
#1
def my_function(subjects):
  for subject in subjects:
    print(subject)

a = list(map(str, input().split()))
my_function(a)

#2
def my_function(flowers):
  for flower in flowers:
    print(flower)

f = ["roses", "peonies", "orchids"]
my_function(f)

#3
def my_function(colors):
  for color in colors:
    print(color)

c = ["blue", "ivory", "pink", 'cherry red', 'orange']
my_function(c)

#4
def my_function(cities):
  for city in cities:
    print(city)

c = list(map(str, input().split()))
my_function(c)

#5
def my_function(students):
  for student in students:
    print(student)

s = ["Anne", "Belle", "Elisa"]
my_function(s)