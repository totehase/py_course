from mobile_phone_class import MobilePhone

def main():
    """
    Основная функция программы.

    Выводит меню позволяя:
    - Сменить номер
    - Включить/Выключить
    - Позвонить на указанный номер
    """
    phone1 = MobilePhone(input("Добавьте номер телевона --> "))
    phone2 = MobilePhone(input("Добавьте номер телевона --> "))

    default_phone = phone1   # По умолчанию первый номер.

    while True:
        print(f"Текущий номер телефона: {default_phone.number}")

        print("""
========================
       Действие 
========================
0 - Сменить номер телефона
1 - Включить
2 - Выключить
3 - Позвонить
4 - Выход
""")
        
        try:
            choice = int(input("-->"))
        except ValueError:
            print("Ошибка: нужно ввести число от 1 до 4")
            continue

        if choice == 0:
            if default_phone == phone1:
                default_phone = phone2
            else:
                default_phone = phone1

        elif choice == 1:
            print(default_phone.turn_on())

        elif choice == 2:
            print(default_phone.turn_off())

        elif choice == 3:
            number = input("Введите номер для звонка: ")
            print(default_phone.call(number))

        elif choice == 4:
            print("Пока-пока")
            break

        else:
            print("Неверный выбор. Введите число от 1-4")


if __name__ == '__main__':
    main()
        