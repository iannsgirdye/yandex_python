# Шашки

class Checkers:
    
    def __init__(self):
        self.free_cells = set()      # Свободные клетки
        self.black_checkers = set()  # Чёрные шашки
        self.white_checkers = set()  # Белые шашки
        
        # Генерация поля
        for letter in "ABCDEFGH":
            for number in "12345678":
                if (number in "45") or ((ord(letter) + int(number)) % 2 == 1):
                    self.free_cells.add(letter + number)  # Пустые клетки = белые или на рядах 4 и 5
                else:  # Занятые клетки = чёрные клетки не на рядах 4 и 5
                    if number in "123":
                        self.white_checkers.add(letter + number)  # Добавление к белым шашкам
                    if number in "678":
                        self.black_checkers.add(letter + number)  # Добавление к чёрным шашкам
        
    def move(self, f, t):
        self.free_cells.add(f)       # Клетка теперь свободна
        self.free_cells.remove(t)    # Кленка теперь занята
        if f in self.black_checkers:
            self.black_checkers.add(t)     # Перемещение чёрной шашки на это вместо
            self.black_checkers.remove(f)  # с этого 
        else:
            self.white_checkers.add(t)     # Перемещение белой шашки на это место
            self.white_checkers.remove(f)  # с этого
        
    def get_cell(self, p):
        if p in self.free_cells:
            return Cell("X")
        if p in self.white_checkers:
            return Cell("W")
        if p in self.black_checkers:
            return Cell("B")
    
    
class Cell:
    
    def __init__(self, p):
        self.type = p
        
    def status(self):
        return self.type
