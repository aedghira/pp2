#Example on W3schools
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#My own examples
#1
thisdict = {'name': 'Anna', 'age': 20, 'city': 'Almaty'}
#2
thisdict = {'brand': 'BMW', 'model': 'X5', 'year': 2018}
#3
thisdict = {'country': 'Kazakhstan', 'capital': 'Astana'}
#4
thisdict = {'fruit': 'apple', 'color': 'red'}
#5
thisdict = {'language': 'Python', 'level': 'beginner'}

#Example onW3schools
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#My own examples
#1
thisdict = {'name': 'Anna',
             'age': 20}
print(thisdict['name'])
#2
thisdict = {'brand': 'BMW', 
            'year': 2018}
print(thisdict['brand'])
#3
thisdict = {'city': 'Almaty', 
            'country': 'KZ'}
print(thisdict['city'])
#4
thisdict = {'fruit': 'apple', 
            'price': 300}
print(thisdict['fruit'])
#5
thisdict = {'language': 'Python', 
            'version': 3}
print(thisdict['language'])

#Example onW3schools
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#My own examples
#1
thisdict = {'a': 1, 
            'a': 2}
print(thisdict)
#2
thisdict = {'year': 2000, 
            'year': 2024}
print(thisdict)
#3
thisdict = {'x': 10, 
            'x': 20, 
            'x': 30}
print(thisdict)
#4
thisdict = {'name': 'Ann', 
            'name': 'Ali'}
print(thisdict)
#5
thisdict = {'color': 'red', 
            'color': 'blue'}
print(thisdict)

#Example onW3schools
print(len(thisdict))

#My own examples
#1
thisdict = {'a': 1, 'b': 2}
print(len(thisdict))
#2
thisdict = {'name': 'Anna', 'age': 20, 'city': 'Almaty'}
print(len(thisdict))
#3
thisdict = {'x': 1}
print(len(thisdict))
#4
thisdict = {}
print(len(thisdict))
#5
thisdict = {'one': 1, 'two': 2, 'three': 3}
print(len(thisdict))


#Example onW3schools
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#My own examples
#1
thisdict = {'name': 'Anna', 'student': True, 'age': 20}
#2
thisdict = {'brand': 'Tesla', 'electric': True, 'year': 2022}
#3
thisdict = {'numbers': [1, 2, 3], 'active': False}
#4
thisdict = {'pi': 3.14, 'valid': True}
#5
thisdict = {'colors': ['red', 'blue'], 'count': 2}

#Example onW3schools
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#My own examples
#1
thisdict = dict(name='Anna', age=20)
print(thisdict)
#2
thisdict = dict(brand='BMW', year=2018)
print(thisdict)
#3
thisdict = dict(city='Almaty', country='KZ')
print(thisdict)
#4
thisdict = dict(language='Python', level='basic')
print(thisdict)
#5
thisdict = dict(x=1, y=2)
print(thisdict)

#Example onW3schools
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#My own examples
#1
thisdict = {'name': 'Anna', 'age': 20}
x = thisdict['age']
#2
thisdict = {'brand': 'BMW', 'year': 2018}
x = thisdict['year']
#3
thisdict = {'city': 'Almaty'}
x = thisdict['city']
#4
thisdict = {'fruit': 'apple'}
x = thisdict['fruit']
#5
thisdict = {'language': 'Python'}
x = thisdict['language']

#Example onW3schools
x = thisdict.get("model")

#My own examples
#1
thisdict = {'name': 'Anna'}
x = thisdict.get('name')
#2
thisdict = {'brand': 'BMW'}
x = thisdict.get('brand')
#3
thisdict = {'city': 'Almaty'}
x = thisdict.get('city')
#4
thisdict = {'fruit': 'apple'}
x = thisdict.get('fruit')
#5
thisdict = {'language': 'Python'}
x = thisdict.get('language')

#Example onW3schools
x = thisdict.keys()

#My own examples
#1
thisdict = {'a': 1, 
            'b': 2}
x = thisdict.keys()
#2
thisdict = {'name': 'Anna',
            'age': 20}
x = thisdict.keys()
#3
thisdict = {'city': 'Almaty'}
x = thisdict.keys()
#4
thisdict = {'fruit': 'apple'}
x = thisdict.keys()
#5
thisdict = {'x': 1, 
            'y': 2}
x = thisdict.keys()

#Example onW3schools
x = thisdict.values()

#My own examples
#1
thisdict = {'a': 1, 
            'b': 2}
x = thisdict.values()
#2
thisdict = {'name': 'Anna', 
            'age': 20}
x = thisdict.values()
#3
thisdict = {'city': 'Almaty'}
x = thisdict.values()
#4
thisdict = {'fruit': 'apple'}
x = thisdict.values()
#5
thisdict = {'x': 1, 
            'y': 2}
x = thisdict.values()

#Example onW3schools
x = thisdict.items()

#My own examples
#1
thisdict = {'a': 1, 'b': 2}
x = thisdict.items()
#2
thisdict = {'name': 'Anna', 'age': 20}
x = thisdict.items()
#3
thisdict = {'city': 'Almaty'}
x = thisdict.items()
#4
thisdict = {'fruit': 'apple'}
x = thisdict.items()
#5
thisdict = {'x': 1, 'y': 2}
x = thisdict.items()

#Example onW3schools
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#My own examples
#1
thisdict = {'name': 'Anna'}
if 'name' in thisdict:
    print('yes')
#2
thisdict = {'brand': 'BMW'}
if 'brand' in thisdict:
    print('yes')
#3
thisdict = {'city': 'Almaty'}
if 'city' in thisdict:
    print('yes')
#4
thisdict = {'fruit': 'apple'}
if 'fruit' in thisdict:
    print('yes')
#5
thisdict = {'language': 'Python'}
if 'language' in thisdict:
    print('yes')

#Example onW3schools
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#My own examples
#1
thisdict = {'year': 2000}
thisdict.update({'year': 2024})
#2
thisdict = {'age': 18}
thisdict.update({'age': 20})
#3
thisdict = {'price': 100}
thisdict.update({'price': 150})
#4
thisdict = {'count': 1}
thisdict.update({'count': 2})
#5
thisdict = {'level': 'basic'}
thisdict.update({'level': 'advanced'})

#Example onW3schools
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#My own examples
#1
thisdict = {'a': 1, 'b': 2}
thisdict.pop('a')
print(thisdict)
#2
thisdict = {'name': 'Ali', 'age': 18}
thisdict.pop('age')
print(thisdict)
#3
thisdict = {'x': 10, 'y': 20}
thisdict.pop('y')
print(thisdict)
#4
thisdict = {'color': 'red', 'size': 'M'}

#Example onW3schools
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#My own examples
#1
thisdict = {'a': 1, 'b': 2}
thisdict.popitem()
print(thisdict)
#2
thisdict = {'name': 'Sara', 'city': 'Almaty'}
thisdict.popitem()
print(thisdict)
#3
thisdict = {'x': 5, 'y': 6, 'z': 7}
thisdict.popitem()
print(thisdict)
#4
thisdict = {'one': 1}
thisdict.popitem()
print(thisdict)
#5
thisdict = {'brand': 'BMW', 'year': 2020}
thisdict.popitem()
print(thisdict)

#Example onW3schools
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]

#My own examples
#1
thisdict = {'a': 10, 'b': 20}
del thisdict['a']
print(thisdict)
#2
thisdict = {'name': 'Tom', 'age': 25}
del thisdict['age']
print(thisdict)
#3
thisdict = {'x': 1, 'y': 2}
del thisdict['y']
print(thisdict)
#4
thisdict = {'color': 'blue', 'size': 'L'}
del thisdict['color']
print(thisdict)
#5
thisdict = {'price': 500, 'discount': 50}
del thisdict['discount']
print(thisdict)

#Example onW3schools
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#My own examples
#1
thisdict = {'a': 1, 'b': 2}
thisdict.clear()
print(thisdict)
#2
thisdict = {'name': 'Anna'}
thisdict.clear()
print(thisdict)
#3
thisdict = {'x': 10, 'y': 20}
thisdict.clear()
print(thisdict)
#4
thisdict = {'brand': 'Adidas'}
thisdict.clear()
print(thisdict)
#5
thisdict = {'year': 2024}
thisdict.clear()
print(thisdict)

#Example onW3schools
for x in thisdict:
  print(x)

#My own examples
#1
thisdict = {'a': 1, 'b': 2}
for x in thisdict:
    print(x)
#2
thisdict = {'name': 'Ali', 'age': 19}
for x in thisdict:
    print(x)
#3
thisdict = {'x': 10}
for x in thisdict:
    print(x)
#4
thisdict = {'color': 'red', 'size': 'S'}
for x in thisdict:
    print(x)
#5
thisdict = {'brand': 'Puma'}
for x in thisdict:
    print(x)

#Example onW3schools
for x in thisdict.values():
  print(x)

#My own examples
#1
thisdict = {'a': 1, 'b': 2}
for x in thisdict.values():
    print(x)
#2
thisdict = {'name': 'Anna', 'age': 20}
for x in thisdict.values():
    print(x)
#3
thisdict = {'x': 100}
for x in thisdict.values():
    print(x)
#4
thisdict = {'color': 'black', 'size': 'M'}
for x in thisdict.values():
    print(x)
#5
thisdict = {'year': 2025}
for x in thisdict.values():
    print(x)

#Example onW3schools
for x in thisdict.keys():
  print(x)

#My own examples
#1
thisdict = {'a': 1, 'b': 2}
for x in thisdict.keys():
    print(x)
#2
thisdict = {'name': 'Ali', 'age': 19}
for x in thisdict.keys():
    print(x)
#3
thisdict = {'x': 10}
for x in thisdict.keys():
    print(x)
#4
thisdict = {'color': 'red', 'size': 'S'}
for x in thisdict.keys():
    print(x)
#5
thisdict = {'brand': 'Puma'}
for x in thisdict.keys():
    print(x)

#Example onW3schools
for x, y in thisdict.items():
  print(x, y)

#My own exa#1
thisdict = {'a': 1, 'b': 2}
for x, y in thisdict.items():
    print(x, y)
#2
thisdict = {'name': 'Ali', 'age': 18}
for x, y in thisdict.items():
    print(x, y)
#3
thisdict = {'x': 5}
for x, y in thisdict.items():
    print(x, y)
#4
thisdict = {'color': 'green'}
for x, y in thisdict.items():
    print(x, y)
#5
thisdict = {'year': 2023}
for x, y in thisdict.items():
    print(x, y)

#Example onW3schools
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#My own examples
#1
thisdict = {'a': 1}
mydict = thisdict.copy()
print(mydict)
#2
thisdict = {'name': 'Sara'}
mydict = thisdict.copy()
print(mydict)
#3
thisdict = {'x': 10}
mydict = thisdict.copy()
print(mydict)
#4
thisdict = {'brand': 'HP'}
mydict = thisdict.copy()
print(mydict)
#5
thisdict = {'year': 2024}
mydict = thisdict.copy()
print(mydict)

#Example onW3schools
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#My own examples
#1
thisdict = {'a': 1}
mydict = dict(thisdict)
print(mydict)
#2
thisdict = {'name': 'Omar'}
mydict = dict(thisdict)
print(mydict)
#3
thisdict = {'x': 7}
mydict = dict(thisdict)
print(mydict)
#4
thisdict = {'color': 'white'}
mydict = dict(thisdict)
print(mydict)
#5
thisdict = {'price': 300}
mydict = dict(thisdict)
print(mydict)

#Example onW3schools
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#My own examples
#1
myfamily = {
    'child1': {'name': 'Ali', 'year': 2001},
    'child2': {'name': 'Sara', 'year': 2005}
}
#2
myfamily = {
    'son': {'name': 'Adam', 'year': 2010},
    'daughter': {'name': 'Amina', 'year': 2012}
}
#3
myfamily = {
    'child1': {'name': 'Omar', 'year': 2003},
    'child2': {'name': 'Yusuf', 'year': 2006},
    'child3': {'name': 'Maryam', 'year': 2009}
}
#4
myfamily = {
    'student1': {'name': 'Anna', 'grade': 90},
    'student2': {'name': 'Elena', 'grade': 95}
}
#5
myfamily = {
    'person1': {'name': 'John', 'age': 30},
    'person2': {'name': 'Mike', 'age': 25}
}

#Example onW3schools
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#My own examples
#1
child1 = {'name': 'Ali', 'year': 2001}
child2 = {'name': 'Sara', 'year': 2005}
myfamily = {'child1': child1, 'child2': child2}
#2
child1 = {'name': 'Adam', 'year': 2010}
child2 = {'name': 'Amina', 'year': 2012}
myfamily = {'son': child1, 'daughter': child2}
#3
child1 = {'name': 'Omar', 'year': 2003}
child2 = {'name': 'Yusuf', 'year': 2006}
child3 = {'name': 'Maryam', 'year': 2009}
myfamily = {'child1': child1, 'child2': child2, 'child3': child3}
#4
child1 = {'name': 'Anna', 'grade': 90}
child2 = {'name': 'Elena', 'grade': 95}
myfamily = {'student1': child1, 'student2': child2}
#5
child1 = {'name': 'John', 'age': 30}
child2 = {'name': 'Mike', 'age': 25}
myfamily = {'person1': child1, 'person2': child2}
