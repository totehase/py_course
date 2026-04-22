class storage:
    def __init__(self):
        self.__items = []
    def priemka(self, value):
        self.__items.append(value)
        print("Приемка товара на склад:", value)
    def otgruzka(self):
        try:
            res = self.__items.pop()
            print("Отгрузка товара со склада:", res)
        except IndexError:
            print("Твой склад пуст")
        except:
            print("Какая-то ошибка отгрузки на складе.")
    def get_items(self):
        return self.__items