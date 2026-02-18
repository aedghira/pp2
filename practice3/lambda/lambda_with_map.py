#Example on W3schools
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#My own examples
#1
numbers = list(map(int, input().split()))
square_of_numbers = list(map(lambda x: x ** 2, numbers))
print(square_of_numbers)

#2
a = [2, 4, 8, 16, 32, 64, 128]
b = list(map(lambda y: y // 2, a))
print(b)

#3
a = [1, 55, 93, 26, 83, 29, 38]
b = list(map(lambda z: z % 7, a))
print(b)

#4
a = list(map(int, input().split()))
b = list(map(lambda w: (w + 45) / len(a), a))
print(b)

#5
a = list(map(int, input().split()))
b = list(map(lambda v: v ** 0.5, a))
print(b)

#6
a = ['tree', 'plant', 'flower', 'seaweed', 'wood']
b = list(map(lambda c: c ** 3, a))
print(b)

#7
a = [1, 2, 3, 4, 5, 6, 7]
b = list(map(lambda x: x + 1, a))
print(b)

#8
a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = list(map(lambda s: s ** 2, a))
print(b)