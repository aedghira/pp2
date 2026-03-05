#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

def func(a):
    a = int(input())
    return bool(re.fullmatch(r'ab*', a))

#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
def func2(a):
    a = int(input())
    return bool(re.fullmatch(r'ab{2,3}', a))

#Write a Python program to find sequences of lowercase letters joined with a underscore.
def func3(a):
    a = int(input())
    return re.findall(r'[a-z]+_[a-z]+', a)

#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def func4(a):
    a = int(input())
    return re.findall(r'[A-Z][a-z]+', a)

#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
def func5(a):
    a = int(input())
    return bool(re.fullmatch(r'a.*b', a))

#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
def func6(a):
    a = int(input())
    return re.sub(r'[ ,.]', ':', a)

#Write a python program to convert snake case string to camel case string.
def func7(a):
    a = int(input())
    parts = a.split('_')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

#Write a Python program to split a string at uppercase letters.
def func8(s):
    a = int(input())
    return re.findall(r'[A-Z][a-z]*', a)

#Write a Python program to insert spaces between words starting with capital letters.
def func9(a):
    a = int(input())
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', a)

#Write a Python program to convert a given camel case string to snake case.
def func10(a):
    a = int(input())
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', a).lower()



