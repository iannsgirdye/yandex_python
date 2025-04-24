# Дроби v0.2
# Примечание: знак дроби хранится в числителе, но не принадлежит числителю

import math


class Fraction:
    
    def __init__(self, *args):
        if len(args) == 1:
            self.top, self.bottom = map(int, args[0].split("/"))
        else:
            self.top, self.bottom = args[0], args[1]
        self.__check_fraction()
        self.__change_fraction()
    
    def numerator(self, number=None):
        if number is None:
            return abs(self.top)  # Возврат числителя БЕЗ ЗНАКА ДРОБИ
        sign = 1 if self.top > 0 else -1  # Знак дроби хранится в числителе
        self.top = number * sign  # Возвращение знака дроби
        self.__check_fraction()
        self.__change_fraction()
            
    def denominator(self, number=None):
        if number is None:
            return self.bottom
        self.bottom = number
        self.__check_fraction()
        self.__change_fraction()
        
    def __str__(self):
        return f"{self.top}/{self.bottom}"
    
    def __repr__(self):
        return f"Fraction('{self.top}/{self.bottom}')"
    
    def __change_fraction(self):
        divisor = math.gcd(self.top, self.bottom)
        sign = 1 if self.top > 0 else -1  # Определение знака дроби
        self.top *= sign                  # Отнятие знака у числителя (то есть дроби) 
        self.top //= divisor              # Сокращение числителя
        self.bottom //= divisor           # Сокращение знаменателя
        self.top *= sign                  # Восстановление знака числителя (то есть дроби)
        
    def __neg__(self):
        return Fraction(-self.top, self.bottom)
        
    def __check_fraction(self):  # Перенос минуса из знаменателя в числитель
        if self.bottom < 0:
            self.top *= -1
            self.bottom *= -1
