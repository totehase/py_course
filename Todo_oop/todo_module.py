class Task:
    """
    Класс одной задачи.
    Id, название, приоритет, пользовательский id, статус выполнения.
    """
    def __init__(self, tid, name, priority, user_id, completed=False):
        """
        Инициализация задачи.
        """
        self.tid = tid
        self.name = name
        self.priority = priority
        self.user_id = user_id
        self.completed = completed


class TodoList():
    """
    Класс списка.
    Создает, читает одну или все задачи, обновляет, удаляет.
    """
    def __init__(self):
        """
        Инициализация списка.
        tasks - словарь.
        """
        self.tasks = {}

    def create(self, name, priority, user_id, completed=False):
        """
        Создает задачу и добавляет в список.
        BadNameError - если имя пустое.
        BadPriorityError - если приоритет < 0.
        """
        if not name:
            raise BadNameError("Имя не может быть пустым")

        if priority < 0:
            raise BadPriorityError("Приоритет не может быть меньше 0")
        
        tid = max(self.tasks.keys(), default=0) + 1
        task = Task(tid, name, priority, user_id, completed)

        self.tasks[tid] = task

    def read(self, tid):
        """
        Выводит 1 задачу по id.
        BadIdError - если id не найден.
        """
        if tid not in self.tasks:
            raise BadIdError("Нет такого id")
        
        return self.tasks[tid]
    
    def read_all(self):
        """
        Выводит весь список задачь.
        """
        return self.tasks.values()
    
    def update(self, tid, name=None, priority=None, completed=None):
        """
        Находит задачу по id (BadIdError - если id не найден).
        Обновляет запрашивая:
        Новое имя (BadNameError - если имя пустое),
        Новый приоритет (BadPriorityError - если приоритет < 0),
        Новый статус выполнения.
        """
        if tid not in self.tasks:
            raise BadIdError("Нет такого id")
        
        task = self.tasks[tid]

        if name is not None:
            if not name:
                raise BadNameError("Имя не может быть пустым")
            task.name = name

        if priority is not None:
            if priority < 0:
                raise BadPriorityError("Приоритет меньше 0")
            task.priority = priority

        if completed is not None:
            task.completed = completed

    
    def delete(self, tid):
        """
        Находит задачу по id (BadIdError - если id не найден).
        Удаляет.
        """
        if tid not in self.tasks:
            raise BadIdError("Нет такого id")
        
        del self.tasks[tid]


class BadPriorityError(Exception):
    """
    Ошибка: приоритет < 0.
    """
    pass

class BadNameError(Exception):
    """
    Ошибка: имя пустое.
    """
    pass

class BadIdError(Exception):
    """
    Ошибка: Нет задачи с таким id.
    """
    pass