#Example on W3schools
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#My own examples
#1
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("Asylkhan", "Algida")
x.printname()

#2
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("Emily", "Henderson")
x.printname()

#3
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("Kevin", "Mao")
x.printname()

#4
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("Jack", "Mikleson")
x.printname()

#5
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("Pit", "Piter")
x.printname()


#Example on W3schools
class Student(Person):
  pass

#My own examples
#1
class hair_color(Person):
  pass

#2
class age(Person):
  pass

#3
class profession(Person):
  pass

#4
class nationality(Person):
  pass

#5
class citizenship(Person):
  pass


#Example on W3schools
x = Student("Mike", "Olsen")
x.printname()

#My own examples
#1
x = hair_color("black", "hair")
x.printname()

#2
x = nationality("nationality:", "american")
x.printname()

#3
x = age("age:", "25")
x.printname()

#4
x = profession("profession:", "developer")
x.printname()

#5
x = citizenship("citizenship:", "USA")
x.printname()