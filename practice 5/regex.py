#Example on W3schools

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#My own examples
#1
txt = 'We see the beautiful vision'
x = re.findall('is', txt)

print(x)

#2
txt = 'We see the beautiful vision'
x = re.findall('the', txt)

print(x)

#3
txt = 'We see the beautiful vision'
x = re.findall('se', txt)

print(x)

#4
txt = 'We see the beautiful vision'
x = re.findall('be', txt)

print(x)

#5
txt = 'We see the beautiful vision'
x = re.findall('we', txt)

print(x)

#Example on W3schools
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#My own examples
#1
txt = "My mother is a doctor."
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#2
txt = "I go to school by bus"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#3
txt = "The store is closed now."
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#4
txt = "It is 5 o'clock."
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#5
txt = "The sun is bright. The sky is blue."
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


#Example on W3schools
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#My own examples
#1
txt = "My mother is a doctor."
x = re.split("\s", txt)
print(x)

#2
txt = "I go to school by bus"
x = re.split("\s", txt)
print(x)

#3
txt = "The store is closed now."
x = re.split("\s", txt)
print(x)

#4
txt = "It is 5 o'clock."
x = re.split("\s", txt)
print(x)

#5
txt = "The sun is bright. The sky is blue."
x = re.split("\s", txt)
print(x)

#Example on W3schools
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


#My own examples
#1
txt = "The rain in Spain"
x = re.sub("a", "9", txt)
print(x)

#2
txt = "The rain in Spain"
x = re.sub("r", "9", txt)
print(x)

#3
txt = "The rain in Spain"
x = re.sub("S", "9", txt)
print(x)

#4
txt = "The rain in Spain"
x = re.sub("n", "9", txt)
print(x)

#5
txt = "The rain in Spain"
x = re.sub("in", "9", txt)
print(x)