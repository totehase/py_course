# home work 2.1
# Найдите наибольшее из четырех чисел

largest_from_number1_number2 = 0
largest_from_number3_number4 = 0
number1, number2, number3, number4 = int(input("Введите число 1: ")),\
      int(input("Введите число 2: ")),\
          int(input("Введите число 3: ")),\
              int(input("Введите число 4: "))

if number1 >= number2:
    largest_from_number1_number2 = number1
else:
    largest_from_number1_number2 = number2

if number3 >= number4:
    largest_from_number3_number4 = number3
else:
    largest_from_number3_number4 = number4

if largest_from_number1_number2 > largest_from_number3_number4:
    largest_of_all_numbers = largest_from_number1_number2
else:
     largest_of_all_numbers = largest_from_number3_number4
print("Наибольшее число: ", largest_of_all_numbers)

# home work 2.5

name = input("Введите слово: ")
name = name.upper()
for i in name:
    if i in "AEIOU":
        continue
    print(i)

# home work 2.6
# программа калькулятор 

operation = input("Выберите + - * / или exit - ")

while operation != "exit":

    number_one = int(input('Введите первое число: '))
    number_two = int(input('Введите второе число: '))

    if operation == "+":
        print(number_one + number_two)
    elif operation == "-":
        print(number_one - number_two)
    elif operation == "/":
        print(number_one / number_two)
    elif operation == "*":
        print(number_one * number_two)
    else:
        print(f'Неправильный тип операции - {operation}')
