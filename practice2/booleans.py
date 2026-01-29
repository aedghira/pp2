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
