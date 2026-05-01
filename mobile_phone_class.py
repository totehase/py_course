class MobilePhone:
    """
    Класс передставляющий мобильный телефон.
    Атрибуты: number - номер телефона,
    switch - состояние телфона (включен/выключен).
    """
    def __init__(self, number):
        """
        Инициализация телефона.
        """
        self.number = number
        self.switch = False

    def turn_on(self):
        """
        Включает телефон.
        Возвращает сообщение о включении телефона
        """
        self.switch = True
        return f'mobile phone {self.number} is turned  on'

    def turn_off(self):
        """
        Выключает телефон.
        Возвращает сообщение о выключении телефона
        """
        self.switch = False
        return f'mobile phone {self.number} is turned  off'

    def call(self, cally):
        """
        Выполняет звонок на указанный номер телефона.
        Возвращает: номер, на который совершается звонок,
        результат звонка.
        """
        if self.switch == True:
            return f'calling {cally}'
        return "Phone is off"
    
    