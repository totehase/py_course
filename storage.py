# Lab queue.py


class EmptyStorageError(Exception):
    pass


# Очередь
# Кладем в конец
# Достаем с начала
# фикстуры

class storage:
    def __init__(self):
        self.__items = []
        
    def priemka(self, value):
        self.__items.append(value)
        print("Приемка товара на склад:", value)
        
    def otgruzka(self):
        if len(self.__items) == 0:
            raise EmptyStorageError("На складе закончился товар!") 
            
        res = self.__items.pop()
        print("Отгрузка товара со склада:", res)
            
    def get_items(self):
        return self.__items


class App:
    def __init__(self, storage):
        self.__storage = storage
        
    def run(self):
        oper = input("1 - Приемка, 2 - отгрузка, 3 - вывод всех товаров на складе, 4 - exit")
        while oper != "exit":
            if oper == "1":
                self.__storage.priemka(input("введи товар"))
            elif oper == "2":
                try:
                    self.__storage.otgruzka()
                except EmptyStorageError as e:
                    print("Склад пуст!")
                else:
                    print("Отгрузка прошла успешно.")
            elif oper == "3":
                self.__storage.get_items()
            elif oper == "exit":
                break
            else:
                print("не понимаю")
            oper = input("1 - Приемка, 2 - отгрузка, 3 - вывод всех товаров на складе, 4 - exit") 
        print("Пока")


app = App(storage())
app.run()