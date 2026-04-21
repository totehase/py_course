# https://dummyjson.com/todos|

# ToDoList
# хранит задачи
# добавляет задачи         create
# печатает задачи          read
# Обновляет список задач   update
# удаляет задачи           delete


def create_task(max_id):
    """
    Создает задачу запрашивая данные.
    Увеличивает айди на 1.
    Формирует и возвращает задачу в виде словаря.
    """
    auto_id = max_id + 1

    todo = input("Что надо сделать:")
    completed = input("Выполнено? (1 - True, пустой ввод - False):") == "1"   # Не bool - выдает всегда True, без int - при вводе не цифр крашнется  
    userId = int(input("userId:"))
    priority = int(input("Приоритет:"))

    new_task = {auto_id:{
                "Что надо сделать": todo,
                "Выполнено?": completed,
                "userId": userId,
                "Приоритет": priority,
            }
        }

    return new_task


def read_tasks():
    """
    Выводит все задачи из словаря: todos.
    """
    for tk, tdi in todos.items():

        print("Task id:", tk)

        for k, v in tdi.items():
            print("    ", k, ":", v)
        print("__________________________________")


def read_task(tid):
    """
    Выводит 1 задачу по айди.
    """
    res_task = todos.get(tid, -1)

    if res_task == -1:
        print("задача не найдена с id:", tid)
        return

    print("Task id:", tid)

    for k, v in res_task.items():
        print(" ", k, ":", v)

    print("__________________________________")


def delete_task(tid):
    """
    Находит задачу по айди и удаляет ее
    """
    res_task = todos.get(tid, -1)

    if res_task == -1:
        print("задача не найдена с id:", tid)
        return

    print("Task id:", tid)
    todos.pop(tid)

    print("задача с id:", tid, "удалена.")
    print("__________________________________")


# Все задачи в виде словаря.
todos = {
    1:{
        "Что надо сделать": "Do something nice for someone you care about",
        "Выполнено?": False,
        "userId": 152,
        'Приоритет': 1
    },
    2: {
        "Что надо сделать": "Memorize a poem",
        "Выполнено?": True,
        "userId": 13,
        'Приоритет': 2
    },
    3: {
        "Что надо сделать": "Watch a classic movie",
        "Выполнено?": True,
        "userId": 68,
        'Приоритет': 3
    },
}


def main():
    """
    Выводит меню
    Обрабатывает операции введенные пользователем.
    При неверном вводе снова выводит меню.
    """
    print("""
    1 - Создать задачу
    2 - Прочитать задачу по id
    3 - Вывести все задачи
    4 - Удалить задачу по id
    5 - Выход""")
    operation = int(input("-->"))

    while operation != 5:
        if operation == 1:
            task = create_task(max(todos.keys()))
            todos.update(task)
        elif operation == 2:
            tid = int(input("Введи таск id:"))
            read_task(tid)
        elif operation == 3:
            read_tasks()
        elif operation == 4:
            tid = int(input("Введи таск id:"))
            delete_task(tid)
        else:
            print("я не понял попробуй ещё раз.")
    
        print("""
        1 - Создать задачу 
        2 - Прочитать задачу по id
        3 - Вывести все задачи
        4 - Удалить задачу по id
        5 - Выход""")
        operation = int(input("-->"))
    
    print("пока пока")


# Вызов функции.
main()