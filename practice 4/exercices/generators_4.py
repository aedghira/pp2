#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

def squares():
    x = list(map(int, input().split()))
    a = x[0]
    b = x[1]

    for i in range(a, b + 1):
        yield i * i


print(*squares())