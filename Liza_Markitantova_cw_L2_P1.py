# 1. Int, 2. myVariable, 3. 23true, 4. love_python
Int = 99
myVariable = 999
# 23true = 99
love_python = 99
print(Int)

# type casting
a = "hello"
b = 100
c = 3.14
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

age = input("Сколько тебе лет?")
print(age)

print(int(123))
print(int(3.14))
print(float("3.143543"))

print(isinstance(a, bool))
print(isinstance(a, str))

print(2 ** 3)
print(2 ** 3 ** 2 )  # работает с права на лево 
print(2 ** (3 ** 2 ))

# на ноль делить нельзя, но ноль делить на что угодно можно 

# print(10/0)
print(0/10)

# конкотенация или сложение строк 

name = "Liza"
phone = "3546"
age = "20"
separator = "__"
userData = name + separator + age + separator + phone
print(userData)

# репликация строк, то есть умножение строки на число

userData = f'{name} {separator} {age} {separator} {phone}' 
print(userData)

#  ключевые слова

import keyword
keyword.kwlist

#  'False', 'None', 'True', 'and', 'as', 'assert',
#  'async', 'await', 'break', 'class', 'continue', 'def',
#  'del', 'elif', 'else', 'except', 'finally', 'for', 'from',
#  'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
#  'not', 'or', 'pass', 'raise', 'return', 'try', 'while',
#  'with', 'yield'

# программа калькулятор 

one = int(input('Введите первое число'))
two = int(input('Введите второе число'))
three = int(input('Введите третье число'))
print(f'{one} + {two} = {one + two}')
print(f'{one} * {three} = {one * three}')
print(f'{one} / {three} = {one / three}')

# the zen of python
# import this
