#Example on W3schools
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#My own examples
#1
fruits = [('apple', 5), ('banana', 8), ('grapes', 1000)]
sorted_fruits = sorted(fruits, key=lambda x: x[1])
print(sorted_fruits)

#2
a = [('Math', 99), ('Physics', 98), ('PP2', 100), ('Discrete structures', 97)] #yep, this is a manefistation
b = sorted(a, key=lambda y: y[1])
print(b)

#3
a = [('Tree', 4), ('Burj Khalifa', 830), ('Baiterek', 97)]
b = sorted(a, key=lambda z: z[1])

#4
a = [(3, 66), (4, 88), (9, 44), (8, 11)]
b = sorted(a, key=lambda w: w[0])
print(b)

#5
a = [(3, 66), (4, 88), (9, 44), (8, 11)]
b = sorted(a, key=lambda w: w[1])
print(b)

#Example on W3schools
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#My own examples
#1
words = ['heels', 'bag', 't-shirt', 'skirt', 'dress', 'jeans', 'pajama']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#2
words = ['column', 'arch', 'steel', 'glass', 'brick']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#3
words = list(map(str, input().split()))
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#4
words = ['Europe', 'Asia', 'USA', 'Africa', 'Australia']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#5
words = ['Astana', 'Almaty', 'Paris', 'Washington', 'Los-Angeles', 'Monaco']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
