#Create a generator that generates the squares of numbers up to some number N

def my_func():
    n = int(input())

    for i in range(n + 1):
        yield i * i

a = my_func()

for x in a:
    print(x)