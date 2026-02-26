#Implement a generator that returns all numbers from (n) down to 0.

def substr():
    n = int(input())

    for i in range(n, -1, -1):
        yield i

print(*substr())