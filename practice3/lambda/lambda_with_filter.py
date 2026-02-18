#Example on W3schools
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#My own examples
#1
numbers = [2, 4, 6, 8, 7, 9, 0]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#2
numbers =[0, 1, 0, 1, 0, 0, 0, 6, 1, 1]
a = list(filter(lambda x: x != 0 and x != 6, numbers))
print(a)

#3
numbers = list(map(int, input().split()))
a = list(filter(lambda x: x % 8 != 5, numbers))
print(a)

#4
numbers = [8, 8, 8, 16, 8, 8, 8]
a = list(filter(lambda x: x // 2 != 4, numbers))
print(a)

#5
numbers = [121, 8, 77, 33, 32]
a = list(filter(lambda x: x % 11 == 0, numbers))
print(a)

#5
numbers = [9, 9, 9, 9, 9, 9, 9, 10]
a = list(filter(lambda x: x ** 2 != 81, numbers))
print(a)

#6
numbers = [92, 90, 88, 86, 84, 82, 80]
a = list(filter(lambda x: x - 2 != 90, numbers))
print(a)

#7
numbers = [-9, -8, -7, -6, -5, -4, -3, -2, -1]
a = list(filter(lambda x: x + 2 != 0, numbers))
print(a)