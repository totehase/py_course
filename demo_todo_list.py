# # https://dummyjson.com/todos|

# CRUD
# хранить задачи
# добавить задачу   create
# печатать задачи   read
# Обновляем         update
# удалить           delete

# менюшка
# общая функция с циклом внутри и тп


def create_task(max_id):
    auto_id = max_id + 1

    todo = input("Что надо сделать:")
    completed = bool(input("Выполнено? (1 - True, пустой ввод - False):"))
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
    for tk, tdi in todos.items():

        print("Task id:", tk)

        for k, v in tdi.items():
            print("    ", k, ":", v)
        print("__________________________________")


def read_task(tid):
    res_task = todos.get(tid, -1)

    if res_task == -1:
        print("задача не найдена с id:", tid)
        return

    print("Task id:", tid)

    for k, v in res_task.items():
        print(" ", k, ":", v)

    print("__________________________________")


def delete_task(tid):
    res_task = todos.get(tid, -1)

    if res_task == -1:
        print("задача не найдена с id:", tid)
        return

    print("Task id:", tid)
    todos.pop(tid)

    print("задача с id:", tid, "удалена.")
    print("__________________________________")


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


main()