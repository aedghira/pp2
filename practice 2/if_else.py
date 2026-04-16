#Example on W3schools
a = 33
b = 200
if b > a:
  print("b is greater than a")

#My own examples
#1
a = 33
b = 290
if b > a:
    print("b is greater than a")
#2
number = 15
if number > 0:
    print("The number is positive")
#3
age = 20
if age >= 18:
    print("You are an adult")
#4
is_logged_in = True
if is_logged_in:
    print("Welcome back!")
#5
x = 10
y = 5
if x > y:
    print("x is greater than y")


#Example on W3schools
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

#My own examples
#1
is_admin = False
if is_admin:
    print("You have admin access")
#2
has_subscription = True
if has_subscription:
    print("Welcome, subscriber!")
#3
is_logged_in = False
if is_logged_in:
    print("User is logged in")
#4
email_verified = True
if email_verified:
    print("Email verified successfully")
#5
can_edit = True
if can_edit:
    print("You can edit this document")

#Example on W3schools
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#My own examples
#1
a = 232
b = 1
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
#2
x = 10
y = 10
if y > x:
    print("y is greater")
elif x == y:
    print("x and y are equal")
else:
    print("x is greater")
#3
number = 7
if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
else:
    print("Negative")
#4
temperature = 15
if temperature > 30:
    print("Hot")
elif temperature > 20:
    print("Warm")
else:
    print("Cold")
#5
score = 45
if score >= 90:
    print("A")
elif score >= 50:
    print("B")
else:
    print("C")

#Example on W3schools
number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")
#My own examples
#1
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
#2
number = 7
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
#3
x = 15
if x > 10:
    print("x is bigger than 10")
else:
    print("x is 10 or less")
#4
logged_in = False
if logged_in:
    print("Welcome!")
else:
    print("Please log in")
#5
age = 16
if age >= 18:
    print("Adult")
else:
    print("Minor")

#Example on W3schools
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#My own examples
#1
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
#2
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
#3
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")
#4
x = 10
y = 20
z = 5
if x < y and z < x:
    print("Both conditions True")
#5
age = 17
has_permission = True
if age >= 18 or has_permission:
    print("Allowed to enter")

#Example on W3schools
username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

#My own examples
#1
username = "Emil"
if len(username) > 0:
    print(f"Welcome, {username}!")
else:
    print("Error: Username cannot be empty")
#2
name = "Sara"
if name != "":
    print(f"Hello, {name}")
else:
    print("Name is empty")
#3
user = ""
if len(user) > 0:
    print("Logged in")
else:
    print("No user")
#4
nickname = "Mike"
if nickname:
    print(f"Hi, {nickname}")
else:
    print("Nickname missing")
#5
input_name = "Ali"
if len(input_name) > 0:
    print(f"Welcome, {input_name}!")
else:
    print("Please enter a name")

#Example on W3schools
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#My own examples
#1
x = 5
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
#2
x = 15
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
#3
x = 25
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
#4
x = 10
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
#5
x = 30
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

#Example on W3schools
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")
#My own examples
#1
age = 16
has_license = False
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")
#2
age = 20
has_license = True
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")
#3
age = 25
has_license = False
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")
#4
age = 17
has_license = True
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")
#5
age = 30
has_license = True
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")

#Example on W3schools
temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")
#My own examples
#1
temperature = 15
is_sunny = True
if temperature > 20:
    if is_sunny:
        print("Perfect beach weather!")
    else:
        print("Warm, but not sunny")
#2
temperature = 25
is_sunny = True
if temperature > 20:
    if is_sunny:
        print("Perfect beach weather!")
    else:
        print("Warm, but not sunny")
#3
temperature = 22
is_sunny = False
if temperature > 20:
    if is_sunny:
        print("Perfect beach weather!")
    else:
        print("Warm, but not sunny")
#4
temperature = 18
is_sunny = True
if temperature > 20:
    if is_sunny:
        print("Perfect beach weather!")
    else:
        print("Warm, but not sunny")
#5
temperature = 30
is_sunny = False
if temperature > 20:
    if is_sunny:
        print("Perfect beach weather!")
    else:
        print("Warm, but not sunny")
