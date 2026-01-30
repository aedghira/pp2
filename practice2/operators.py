#ARITHMETIC OPERATORS
#Example on w3schools
print(10 + 5)

#my own examples
#1
print(11 - 6)
#2
print(11 * 5)
#3
print(11 + 5)
#4
print(2 ** 6)
#5
print(24 // 6)
#6
print(11111 / 2)

#Example on w3schools
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

#my own examples
#1
a = 111 + 5            #116
b = 100000 + 1000 + a  #101116
c = 1 + 2 + a + b      #101239
#2
a = 4
b = 5

addition = a + b         #9
difference = a - b       #-1
multiplication = a * b   #20
division = a / b         #0.8
#3
a, b = 1, 11            
a = a + 5                #6
b = a + 2 + b            #19
#4
s = 222
s = s + 2222 - 3 
s = s + s + s
#5
a = 3
b = a - 78
c = b + 110
d = a + c

#Example on w3schools
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#My own examples
#1
a = 33
b = 2


print(a ** (b + 1))       # 35937 (a to the power of (b + 1)) 
print(b - a)              # -31   (substraction of b and a)
print(a + b + b)          # 37    (addition of a and 2b)
print((a + b) ** 2)       # 1225  ((a + b) to the power of 2)
#2
a, b = 16, 4


print(b / a)              # 0.25 (division of b and a)
print(b // a)             # 0     (floor division of b and a)
#3
a = 777
b = 12


print(a % b)              # 9     (modulus of a and b)
print(b % a)              # 12    (modulus of b and a)
print(a * b * b * b)      # 1342656  (multiplication of a and b^3)
#4
a = 7
b = 8
c = 9

print(a * c ** b)         # 301327047
print(a % c // b)         # 0         
#5
x = 12
y = 144


print(x + y * y)          # 20748
print(x // y * y)         # 0 

#Example on w3schools
x = 12
y = 5

print(x / y)

#My own examples
#1
x = 1
y = 6
   

print(x / y)             # 0.16666666666666666
#2
a = 144
b = 12

print(a / b)             # 12.0
print(b / a)             # 0.08333333333333333
#3
a = int(input())
b = int(input())

print(b / a / a)
print(a / b / b)
#4
a, b = 1, 1


print(a / b / b / b)    # 1.0
print(b / a / a / a)    # 1.0
#5
a, b, c =90, 45, 2


print(a / b / c)        # 1.0
print(b / a / c)        # 0.25
print(c / b / a)        # 0.0004938271604938272

#Example on w3schools
x = 12
y = 5

print(x // y)

#My own examples
#1
x = 10
y = 3

print(x // y)           # 3
#2
a = 10000
b = 2222

print(a // b)           # 4
print(b // a)           # 0
#3
a, b = 24, 7

print(b // a)           # 0
print(a // b)           # 3
#4
a, b, c = 81, 65, 3

print(c // a // b)      # 0
print(b // a // c)      # 0
#5
a = 0
b = 100000000000

print(a // b)           # 0


#ASSIGNMENT OPERATORS
#Example on w3schools
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#My own examples
#1
a = [1, 2, 3]   

if (c := len(a)) >= 3:
    print("We have 3 or more array's elements")
else:
    print('We have less than 3 elements in our array')
#2
a = [10, 20, 67, 78, 66]
b = ['a', 'b', 'c']

if (c := len(b)) < len(a):
    print('Length of the array of integers is greater than array of strings')
#3
a = [19, 21, 22, 47, 58, 69, 7] 

if (c := a[6]) > 50:
    print('On friday we sold more than 50 tickets to theatre')   
else:
    print('Our sales 0f tickets  were no more than 50 on Friday')
#4
cosmetics = ['brow palette', 'eyeshadow', 'lipstick', 'bronzer', 'blush']

if (run_out := cosmetics[3]) == 'bronzer':
    print('My'+cosmetics[3]+'is run out!!!!!!!!!!!!!!!!!!!!!')
else:
    print('No need to buy a new bronzer!!!!!')  
#5
fruits = ['apples', 'bananas', 'peaches', 'grapes']

if (c := len(fruits[1])) == len(fruits[2]):
    print(len(fruits[1]))
else:
    print(len(fruits[2]))


#LOGICAL OPERATORS
#Example on W3schools
x = 5

print(x > 0 and x < 10)

#My own examples
#1
x = 7

print(x > 5 and x < 6)
#2
x = int(input())

print(x >= 100 and x <= 110)
#3
x = int(input())
y = int(input())

print(x < 100 and y < 100)
#4
a = 67

print(a > 10 and a > 65 and a != 45)
#5
a = int(input())
b = int(input())

print(a > b and b > 100 and b < 8777)

#Example on W3schools
x = 5

print(x < 5 or x > 10)

#My own examples
#1
x = 7

print(x == 7 or x > 1)
#2
x = int(input())

print(x != 0 or x == 1)
#3
a = 999

print(a > 998 or a < 999)
#4
a = int(input())
b = int(input())

print(a == b or b != 100)
#5
a = 6
b = 7

print(b > a or a > 5)

#Example on W3schools
x = 5

print(not(x > 3 and x < 10))

#My own examples
#1
x = 6

print(not(x < 5 and x == 0))
#2
x = int(input())

print(not(x > 10 and x < 100000))
#3
x = int(input())
y = int(input())

print(not(x > y and y > 134))
#4
x = int(input())
y = int(input())

print(not(x < y and x > 111))
#5
a = 1

print(not(a > 2 and a != 0))

#IDENTITY OPERATORS
#Example on W3schools
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#My own examples
#1
x = [1, 2, 3]
y = [1, 2]
z = y

print(x is z)
print(x is y)
print(x == y)
print(y is z)
#2
a = [1, 11, 111]
b = [11, 111, 1111]

print(a is b)
print(b is a)
#3
a = ['a', 'b', 'c']
b = ['a', 'b', 'c']
c = a
d = b

print(d is a)
print(c is b)
print(a is b)
print(c is a)
#4
a = ['one', 'twenty three', 'twelve']
b = ['one', 'twelve', 'twenty three']

print(a is b)
#5
a = [1, 2, 3, 45, 78]
b = [1, 2, 4, 34, 555]
c = a

print(a is b)

c = b

print(c is a)
print(c is b)

#Example on W3schools
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

#My own examples
#1
x = [1, 2, 3]
y = [1, 2, 3]

print(x is not y)
#2
a = [12, 24, 36]

b = a

print(a is not b)
#3
a = [1, 11]
b = [11111, 45]
c = a
d = b

print(c is not b)
print(c is not a)
print(d is not b)
print(d is not a)
#4
a = ['a', 'b', 'c']
b = ['a', 'b', 'c']
c = b

print(c is not b)

c = a

print(c is not a)
#5
a = ['union', 'set', 'intersection']
b = ['nigation', 'predicate']

print(a is not b)

b = a

print(a is not b)

#Example on W3schools
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#My own examples
#1
a = ['a', 'b', 'c']
b = ['a', 'b', 'c']

print(a is b)
print(a == b)

b = a

print(a is b)
#2
a = [11, 111, 111]
b = [111, 11, 111]

print(a == b)
print(a is b)

b = [11, 111, 111]

print(a == b)
print(a is b)
#3
a = [1, 2]
c = a
b = c

print(a is c)
print(b is c)
print(a == b)
print(a == c)
#4
a = ['orange', 'blue', 'pink']
b = ['orange', 'blue', 'pink']

print(a is b)
print(a == b)

c = a

print(c is b)

c = b

print(c is a)
#5
a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']
c = ['1', '2', '3', '4']

print(c is a)
print(c == a)

c = a

print(c == a)
print(c is a)

#MEMBERSHIP OPERATORS
#Example on W3schools
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

#My own examples
#1
a = [1, 2, 3, 'a']

print('b' in a)
#2
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(1 in a)
print(44 in a)
#3
a = [1, 2, 3, 4]
b = [1, 3]

print(b in a)
#4
a = [9, 99, 999, 9999]

print('9999' in a)
print('999' in a)
print('99' in a)
print('9' in a)
#5
a = ['apple', 'grapefruit', 'orange', 'grapes']

print('pomelo' in a)
print('apple' in a)
print('lemon' in a)

#Example on W3schools
fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

#My own examples
#1
a = [1, 3, 5]

print(4 not in a)
print(2 not in a)
print(6 not in a)
#2
a = ['a', 'b', 'c']
b = 'a'

print(b not in a)
#3
a = [1, 111, 111, 111]

print(999 not in a)
print(111 not in a)
print(99 not in a)
#4
a = [1, 2, 33, 55]
b = [3, 4, 44, 66]

print(b not in a)

b = a

print(b not in a)
#5
a = ['friday', 'tuesday', 'thursday']
b = ['q', 'w', 'e', 'r', 't', 'y']

print(b not in a)
print(a not in b)

a = ['friday', 'w']

print(a not in b)

#Example on W3schools
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

#My own examples
#1
a = 'you are awesome'

print('awesome' in a)
print('awesome ' not in a)
print('1' in a) 
#2
a = 'Jane'
b = 'Julie'

print('J' in a and 'J' not in b)
print('J' in a and 'J' in b)
print('ulie' in a or 'ulie' in b) 
#3
a = '123'

print('1' in a)
print('2' in a)
#4
girl = 'XX'
boy = 'XY'

print('XY' in girl)
print('XX' in boy)
print('Y' in boy and 'Y' not in girl)
print('XY' not in boy and 'XX' not in girl)
#5
q = 'H'
w = 'G'
c = q

print(c in q and c in w)
print(c in q or c in w)

#BITWISE OPERATORS
#Example on W3schools

print(6 & 3)

#My own examples
#1
print(7 & 2)
#2
print(77 & 66)
#3
print(4 & 2)
#4
print(9 & 99)
#5
print(0 & 1)

#Example on W3schools

print(6 | 3)

#My own examples
#1
print(4 | 2)
#2
print(9 | 0)
#3
print(100 | 101)
#4
print(12 | 4)
#5
print(1 | 0)

#Example on W3schools

print(6 ^ 3)

#My own examples
#1
print(8 ^ 3)
#2
print(90 ^ 6)
#3
print(0 ^ 1)
#4
print(44 ^ 11)
#5
print(7 ^ 9)

#OPERATOR PRECEDENCE
#Example on W3schools
print((6 + 3) - (6 + 3))

#My own examples
#1
print((5 + 90) - (6 + 8))
#2
print((10 + 3) - (66 - 8))
#3
print((60 - 30) - (60 + 30))
#4
print((6 + 33333) - (66666 + 3))
#5
print((61 + 68) - (75 - 90))

#Example on W3schools

print(100 + 5 * 3)

#My own examples
#1
print(6 + 8 * 9)
#2
print(100 - 2 * 111)
#3
print(22222 + 0 * 3)
#4
print(105 * 6 - 3)
#5
print(70 + 33 // 3)
#6
print(3 + 98030 // 3)
#7
print(89 - 51 // 17)

#Example on W3schools

print(5 + 4 - 7 + 3)

#My own examples
#1
print(78 + 4 - 77 + 3)
#2
print(89 - 8 + 87 + 88)
#3
print(2 + 90 - 11 + 33)
#4
print(5 + 9000 - 8 + 45)
#5
print(9999 - 44 + 99 - 9)
#6
print(111 + 85 - 543 - 24)
#7
print(7 + 1234 - 22 + 36)
#8
print(22 - 4356 + 178 - 49)