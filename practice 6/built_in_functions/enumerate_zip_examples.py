#Examples for function 'enumerate()'

list_1 = list(map(str, input().split()))

for x, y in enumerate(list_1):
    print(x, y)

print(list(enumerate(list_1)))

#Examples for function 'zip()'

list_2 = list(map(int, input().split()))
list_3 = list(map(str, input().split()))

for a in zip(list_2, list_3):
    print(a)