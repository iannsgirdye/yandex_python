# Работа не волк

class Programmer:
    
    def __init__(self, name, post):
        self.name = name                 # Фамилия и имя
        self.post = "Junior"             # Должность
        self.work_time = 0               # Отработанное время
        self.bank = 0                    # Накопленная зарплата
        match post:                      # Определение почасовой оплаты
            case "Junior":
                self.salary = 10
            case "Middle":
                self.salary = 15
            case "Senior":
                self.salary = 20
        
    def work(self, time):
        self.work_time += time           # Увеличение отработанного времени
        self.bank += time * self.salary  # Пополнение копилки зарплат
        
    def rise(self):
        match self.post:                 # Повышение зарплаты и должности
            case "Junior":
                self.post = "Middle"
                self.salary = 15
            case "Middle":
                self.post = "Senior"
                self.salary = 20
            case "Senior":
                self.salary += 1
            
    def info(self):
        return f"{self.name} {self.work_time}ч. {self.bank}тгр."
