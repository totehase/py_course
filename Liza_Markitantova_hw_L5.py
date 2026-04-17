# Home work lab 5.0.
# Калькулятор
# Операции: + - / *


def get_operation(menu):    # Запрашивает выбор операции, пока не введено корректное значение(0-4).
    while True:
        try:
            operation = int(input(menu))
            if operation in [0, 1, 2, 3, 4]:
                return operation
            else:
                print("Ошибка: Введите число от 0 до 4.")
        except ValueError:  # Обработка ошибки, если ввели не число.
            print("Ошибка! Введите целое число.") 

            
def GetNumb(text):  # Запрашивает число, пока не введено корректное значение
    while True:
        try:
            return float(input(text))
        except ValueError:  # Обработка ошибки, если ввели не число.
            print("Ошибка! Введите число.")


def calculate(a, b, operation):     # Выполнение выбранной операции.
    if operation == "+":
        return a+b
    elif operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/":
        if b == 0:
            return "Ошибка: делить на 0 нельзя!"
        return a/b


def run_calculator():   # Отображает меню и запускает цикт калькулятора.
    menu = """
_________________________________________________________
|             Добро пожаловать в калькулятор!
|      
|    Выберите операцию:
|    1 -   Сложение 
|    2 -   Вычитание
|    3 -   Умножение
|    4 -   Деление
|    0 -   Выход
|________________________________________________________

-----> """ 

    operation = get_operation(menu)     # Получили операцию от пользователя.

    while operation != 0:
        num1 = GetNumb("Введите 1 число:")  # Получаем 1 число.
        num2 = GetNumb("Введите 2 число:")  # Получаем 2 число.
    
        if operation == 1:
            result = num1 + num2
        elif operation == 2:
            result = num1 - num2
        elif operation == 3:
            result = num1 * num2
        elif operation == 4:
            if num2 == 0:   # Проверяем деление на 0.
                print("Ошибка: Делить на 0 нельзя!")
                operation = get_operation(menu)     # Повторно запрашиваем операцию.
                continue
            result = num1 / num2

        print("Результат:", result)     # Выводим результат.
            
        operation = get_operation(menu)     # запрашиваем операцию снова.


run_calculator()


    


# Home work 5.1 a leap year.


def is_year_leap(year):     # Проверяем високосный ли год.
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    

test_data = [1500, 1900, 2000, 2016, 1987]
test_results = [False, False, True, True, False]


for year, result in zip(test_data, test_results):
    if is_year_leap(year) == result:
        print(year, 'is leap? -->', result)
    else:
        print(year, 'from your func -->', \
              is_year_leap(year))
        print('but expected -->', result)


# Home work 5.4 Fibonacci numbers.


def fibo(n):    # Вычисляет число Фибоначчи.
    fib1, fib2 = 1, 1
    
    if n < 1:
        return None
        
    if n < 3:
        return 1

    for i in range(3, n + 1):   # Вычисляет числа Фибоначчи от 3 до n.
        fib1, fib2 = fib2, fib1 + fib2
        
    return fib2

    
n = int(input("Введите число больше 0 --> "))   # Ввод числа от пользоватея.
result = fibo(n)    # Вызов функции.

if result is None:  # Проверка и вывод результата.
    print("Число должно быть больше 0")
else:
    print(f"Fibonacci {n} = {result}")


    