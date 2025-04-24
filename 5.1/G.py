# Классный прямоугольник 3.0 | программа не прошла все тесты

class Rectangle:
    
    def __init__(self, corner1: float, corner2: float) -> None:
        self.x = min(corner1[0], corner2[0])  # Абсцисса левой верхней точки
        self.y = max(corner1[1], corner2[1])  # Ордината левой верхней точки
        self.width = max(corner1[0], corner2[0]) - self.x   # Ширина
        self.height = self.y - min(corner1[1], corner2[1])  # Высота
    
    def perimeter(self) -> float:  # Периметр
        return round(self.width * 2 + self.height * 2, 2)
        
    def area(self) -> float:  # Площадь
        return round(self.width * self.height, 2)
    
    def get_pos(self) -> tuple:  # Координаты левой верхней точки
        return round(self.x, 2), round(self.y, 2)
    
    def get_size(self) -> tuple:  # Ширина и высота
        return round(self.width, 2), round(self.height, 2)
    
    def move(self, dx: float, dy: float) -> None:  # Перемещение левой верхней точки
        self.x += dx
        self.y += dy
        
    def resize(self, new_width: float, new_height: float) -> None:  # Изменение ширины и длины
        self.width = new_width
        self.height = new_height
        
    def turn(self) -> None:  # Поворот на 90 градусов по часовой стрелке
        delta = (self.width - self.height) / 2                     # Величина перемещения координат
        self.move(dx=delta, dy=delta)                              # Перемещение левой верхней точки
        self.resize(new_width=self.height, new_height=self.width)  # Смена сторон местами
        
    def scale(self, factor: float) -> None:
        new_width = self.width * factor      # Будущая ширина
        new_height = self.height * factor    # Будущая высота
        dx = (new_width - self.width) / -2   # Величина изменения абсциссы левой верхней точки
        dy = (new_height - self.height) / 2  # Величина изменения ординаты левой верхней точки
        self.move(dx=dx, dy=dy)                                  # Перемещение левой вехней точки
        self.resize(new_width=new_width, new_height=new_height)  # Изменение длин сторон
