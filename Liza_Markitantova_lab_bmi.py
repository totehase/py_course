# project_lab_bmi.
# https://gkb81.ru/sovety/kalkulyator-imt/
# Расчет BMI.
# BMI (индекс массы тела) рассчитывается по формуле:
# BMI = weight (kilograms) / • height (meters) ** 2.

# Запрашивает у пользователя вес и рост.
# Проверяет корректность данных
# Вычисляет BMI.
# Выводит результат и категорию.
# Меню.

def calculate_bmi():    # Запрашивает данные, проверяет их корректность, возвращает float
    while True:
        try:
            weight = float(input("Введите вес от 20 до 200 (кг) --> "))
            height = float(input("Введите рост от 1.0 до 2.5 (м) --> "))
        except ValueError:
            print("Ошибка: введено не число. Попробуйте снова.")
            continue

        # Проверка диапазона значений.     
        if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
            print("Ошибка: данные вне допустимого диапазона.")
            continue

        # Расчет BMI.    
        bmi = weight / height ** 2
        return bmi

def show_bmi():     # Вызывает функцию рассчета BMI, выводит результат и категорию.
    result = calculate_bmi()
    
    print("Ваш BMI:", result)

    # Подбирает категорию.
    if result < 18.5:
        print("Дефицит массы тела")
    elif result < 25:
        print("Норма")
    elif result < 30:
        print("Предожирение, избыточный вес")
    else:
        print("Ожирение")


def run_menu():     # Меню и выбор пользователя. 
    menu = """
______________________________________________________________________
|             Добро пожаловать! Давай рассчитаем ваш ИМТ
|      
|    Выберите операцию:
|    1 -   Рассчитать ИМТ 
|    2 -   Выход
|_____________________________________________________________________

"""
    while True:
        print(menu)
        try:
            operation = int(input("-->"))
        except ValueError:
            print("Ошибка: введите число (1 или 2)")
            continue
            
        if operation == 1:
            show_bmi()
        elif operation == 2:
            print("Пока-пока!")
            break
        else: 
            print("Я тебя не понял, попробуй снова")


# Вызов программы.
run_menu()