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
    self.graduationyear = 2019

x = Student("Mike", "Olsen", 2019)


#My own examples
#1
x = Person("Asylkhan", "Algida")
x.printname()


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = 2029

x = Student("Asylkhan", "Algida", 2029)

#2
x = Person("Yeat", "Salivan")
x.printname()


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = 2027

x = Student("Yeat", "Salivan", 2027)

#3
x = Person("Terry", "Ernest")
x.printname()


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = 2028

x = Student("Terry", "Ernest", 2028)

#4
x = Person("Katerine", "James")
x.printname()

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = 2017

x = Student("Katerine", "James", 2017)

#5
x = Person("Ian", "Jackson")
x.printname()

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = 2021

x = Student("Ian", "Jackson", 2021)