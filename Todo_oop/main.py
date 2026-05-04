from todo_module import TodoList, BadIdError, BadNameError, BadPriorityError
"""
Импортирует модули из файла todo_module.
"""


class App():
    """
    Класс для взаимодействия с пользователем.
    Позволяет создавать, просматривать, обновлять и удалять задачи.
    """
    def __init__(self):
        self.todo = TodoList()

    def run(self):
        """
        Запускает основной цикл программы.
        Выводит меню и обрабатывает ввод пользвателя.
        """
        while True:
            print("""
    1 - Создать задачу
    2 - Прочитать 1 задачу по id
    3 - Вывести все задачи
    4 - Удалить задачу по id
    5 - Обновить              
    6 - Выход""")
            
            try:
                operation = int(input("--> "))

                if operation == 1:
                    name = input("Что надо сделать:")
                    priority = int(input("Приоритет:"))        
                    user_id = int(input("userId:"))
                    completed = input("Выполнено? (1 - True, 2 - False):")

                    if completed == "1":
                        completed = True
                    elif completed == "2":
                        completed = False
                    else:
                        completed = None

                    self.todo.create(name, priority, user_id, completed)

                elif operation == 2:
                    tid = int(input("Введи id:"))
                    task = self.todo.read(tid)
                    print(f"""
                    ID: {task.tid} 
                    Название: {task.name} 
                    Приоритет: {task.priority} 
                    User ID: {task.user_id} 
                    Выполнено: {task.completed}
                    """)
                          
                elif operation == 3:
                    for task in self.todo.read_all():
                        print(f"""
                        ID: {task.tid}
                        Название: {task.name}
                        Приоритет: {task.priority}
                        User ID: {task.user_id}
                        Выполнено: {task.completed}
                        """)
                          

                elif operation == 4:
                    tid = int(input("Введи id:"))
                    self.todo.delete(tid)

                elif operation == 5:
                    tid = int(input("Введи id:"))

                    name = input("Новое имя задачи (enter чтобы пропустить): ")
                    name = name if name else None  

                    new_priority = input("Новый приоритет:")  
                    priority = int(new_priority) if new_priority else None   

                    new_completed = input("Выполнено? (1 - True, 2 - False):")
                    if new_completed == "1":
                        completed = True
                    elif new_completed == "2":
                        completed = False
                    else:
                        completed = False

                    self.todo.update(tid, name, priority, completed)


                elif operation == 6:
                    print("Пока-пока")
                    break

                else:
                    print("Неверная команда")
                
            except BadPriorityError as p:
                print("Ошибка: ", p)

            except BadNameError as n:
                print("Ошибка: ", n)

            except BadIdError as i:
                print("Ошибка: ", i)

            except ValueError:
                print("Ошибка, ввод должен быть числом!")


if __name__ == "__main__":
    app = App()
    app.run()
