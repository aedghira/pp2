#Example on W3schools
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


#My own examples
#1
print(y["name"])

#2
print(y["city"])

#3
a = {"state":"liquid", "density":"890 kg/m^3", "name":"fossil"}

b = json.loads(a)
print(b["state"])

#4
print(b["name"])

#5
print(b["density"])
#Example on W3schools

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


#My own examples
#1
w = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(w)

print(y)

#2
z = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(z)

print(y)

#3
v = {
  "name": "Aelita",
  "age": 16,
  "city": "New York"
}

y = json.dumps(v)

print(y)

#4
l = {
  "name": "Johnny",
  "age": 41,
  "city": "New York"
}

y = json.dumps(l)

print(y)

#5
i = {
  "name": "Algida",
  "age": 18,
  "city": "New York"
}

y = json.dumps(i)

print(y)


#Example on W3schools
print(json.dumps(x, indent=4))



#My own examples
#1
print(json.dumps(l, indent=8))

#2
print(json.dumps(w, indent=2))

#3
print(json.dumps(z, indent=5))

#4
print(json.dumps(v, indent=9))

#5
print(json.dumps(i, indent=11))

#Example on W3schools
json.dumps(x, indent=4, separators=(". ", " = "))


#My own examples
#1
json.dumps(v, indent=4, separators=(", ", " = "))

#2
json.dumps(w, indent=10, separators=(", ", " = "))

#3
json.dumps(z, indent=6, separators=(", ", " = "))

#4
json.dumps(l, indent=7, separators=(", ", " = "))

#5
json.dumps(i, indent=9, separators=(", ", " = "))


#Example on W3schools
json.dumps(x, indent=4, sort_keys=True)


#My own examples
#1
json.dumps(w, indent=4, sort_keys=True)

#2
json.dumps(z, indent=4, sort_keys=True)

#3
json.dumps(l, indent=4, sort_keys=True)

#4
json.dumps(v, indent=4, sort_keys=True)

#5
json.dumps(i, indent=4, sort_keys=True)

