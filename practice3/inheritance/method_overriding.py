class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#Example on W3schools
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

#My own examples
#1
class age(Person):
  def __init__(self, fname, lname, age_):
    super().__init__(fname, lname)
    self.age_ = age_

  def ag(self):
    print("His name is", self.firstname, self.lastname, "and he is", self.age_)

#2
class nationality(Person):
  def __init__(self, fname, lname, nationality_):
    super().__init__(fname, lname)
    self.nationality_ = nationality_

  def natn(self):
    print("His name is", self.firstname, self.lastname, "and he is", self.nationality_)

#3
class citizenship(Person):
  def __init__(self, fname, lname, citizenship_):
    super().__init__(fname, lname)
    self.citizenship_ = citizenship_

  def cits(self):
    print("His name is", self.firstname, self.lastname, "and his citizenship is", self.citizenship_)

#4
class profession(Person):
  def __init__(self, fname, lname, profession_ ):
    super().__init__(fname, lname)
    self.profession_ = profession_

  def prof(self):
    print("His name is", self.firstname, self.lastname, "and he is", self.profession_)

#5
class university(Person):
  def __init__(self, fname, lname, uni):
    super().__init__(fname, lname)
    self.uni = uni

  def welcome(self):
    print("His name is", self.firstname, self.lastname, "and he studies at the", self.uni)