import useful_funcs as u

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
    print("""
    1 - Создать задачу
    2 - Прочитать задачу по id
    3 - Вывести все задачи
    4 - Удалить задачу по id
    5 - Выход""")
    operation = int(input("-->"))

    while operation != 5:
        if operation == 1:
            task = u.create_task(max(todos.keys()))
            todos.update(task)
        elif operation == 2:
            tid = int(input("Введи таск id:"))
            u.read_task(tid, todos)
        elif operation == 3:
            u.read_tasks(todos)
        elif operation == 4:
            tid = int(input("Введи таск id:"))
            u.delete_task(tid, todos)
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


main()
