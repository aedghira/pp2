def my_func():
    n = int(input())

    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print(*my_func())