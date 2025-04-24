# Дроби v0.7
# Примечание: знак дроби хранится в числителе, но не принадлежит числителю

import math


class Fraction:
    
    def __init__(self, *args):
        if len(args) == 1:
            if (type(args[0]) is str) and ("/" in args[0]):  # Fraction('2/3')
                self.top, self.bottom = map(int, args[0].split("/"))
            else:  # Fraction(2) и Fraction('2')
                self.top, self.bottom = int(args[0]), 1
        else:  # Fraction(2, 3)
            self.top, self.bottom = args[0], args[1]
        self.top, self.bottom = self.__check_fraction(self.top, self.bottom)
        self.top, self.bottom = self.__change_fraction(self.top, self.bottom)
    
    def numerator(self, number=None):
        if number is None:
            return abs(self.top)  # Возврат числителя БЕЗ ЗНАКА ДРОБИ
        sign = 1 if self.top > 0 else -1  # Знак дроби хранится в числителе
        self.top = number * sign  # Возвращение знака дроби
        self.top, self.bottom = self.__check_fraction(self.top, self.bottom)
        self.top, self.bottom = self.__change_fraction(self.top, self.bottom)
            
    def denominator(self, number=None):
        if number is None:
            return self.bottom
        self.bottom = number
        self.top, self.bottom = self.__check_fraction(self.top, self.bottom)
        self.top, self.bottom = self.__change_fraction(self.top, self.bottom)
        
    def __str__(self):
        return f"{self.top}/{self.bottom}"
    
    def __repr__(self):
        return f"Fraction('{self.top}/{self.bottom}')"
    
    def __check_fraction(self, top, bottom):  # Перенос минуса из знаменателя в числитель
        if bottom < 0:
            top *= -1
            bottom *= -1
        return top, bottom
    
    def __change_fraction(self, top, bottom):
        divisor = math.gcd(top, bottom)  # НОД
        sign = 1 if top > 0 else -1  # Определение знака дроби
        top *= sign                  # Отнятие знака у числителя (то есть дроби) 
        top //= divisor              # Сокращение числителя
        bottom //= divisor           # Сокращение знаменателя
        top *= sign                  # Восстановление знака числителя (то есть дроби)
        return top, bottom
        
    def __neg__(self):  # унарный "-"
        return Fraction(-self.top, self.bottom)

    def __add__(self, other):  # self + other
        other = other if type(other) is Fraction else Fraction(other)
        new_top, new_bottom = self.__sum(other, "+")
        return Fraction(new_top, new_bottom)
        
    def __sub__(self, other):  # self - other
        other = other if type(other) is Fraction else Fraction(other)
        new_top, new_bottom = self.__sum(other, "-")
        return Fraction(new_top, new_bottom)
    
    def __radd__(self, other):  # other + self
        other = other if type(other) is Fraction else Fraction(other)
        new_top, new_bottom = self.__sum(other, "+")
        return Fraction(new_top, new_bottom)  # <---- a + b = b + a
        
    def __rsub__(self, other):  # other - self
        other = other if type(other) is Fraction else Fraction(other)
        new_top, new_bottom = self.__sum(other, "-")
        return Fraction(new_top * -1, new_bottom)  # <---- a - b != b - a
    
    def __iadd__(self, other):  # self += other
        other = other if type(other) is Fraction else Fraction(other)
        self.top, self.bottom = self.__sum(other, "+=")
        return self
        
    def __isub__(self, other):  # self -= other
        other = other if type(other) is Fraction else Fraction(other)
        self.top, self.bottom = self.__sum(other, "-=")
        return self

    def __sum(self, other, action):  # сумма (разность) дробей
        actions = {"+": 1, "-": -1, "+=": 1, "-=": -1}
        lcm = math.lcm(self.bottom, other.bottom)  # НОК = знаменатель новой дроби
        top1 = self.top * (lcm // self.bottom)     # Домножение на НОК числителя 1-й дроби
        top2 = other.top * (lcm // other.bottom)   # Домножение на НОК числителя 2-й дроби
        new_top, new_bottom = self.__change_fraction(top1 + actions[action] * top2, lcm)  # Новая дробь
        return new_top, new_bottom

    def __mul__(self, other):  # self * other
        other = other if type(other) is Fraction else Fraction(other)
        new_top, new_bottom = self.__mul(self.top, other.top, self.bottom, other.bottom)
        return Fraction(new_top, new_bottom)
        
    def __truediv__(self, other):  # self / other
        other = other if type(other) is Fraction else Fraction(other)
        new_top, new_bottom = self.__mul(self.top, other.bottom, self.bottom, other.top)
        return Fraction(new_top, new_bottom)

    def __rmul__(self, other):  # other * self
        other = other if type(other) is Fraction else Fraction(other)
        new_top, new_bottom = self.__mul(self.top, other.top, self.bottom, other.bottom)
        return Fraction(new_top, new_bottom)  # <---- a * b = b * a
         
    def __rtruediv__(self, other):  # other / self
        other = other if type(other) is Fraction else Fraction(other)
        new_bottom, new_top = self.__mul(self.top, other.bottom, self.bottom, other.top)
        return Fraction(new_top, new_bottom)  # ^^^^^ a / b != b / a ^^^^^
        
    def __imul__(self, other):  # self *= other
        other = other if type(other) is Fraction else Fraction(other)
        self.top, self.bottom = self.__mul(self.top, other.top, self.bottom, other.bottom)
        return self
        
    def __itruediv__(self, other):  # self /= other
        other = other if type(other) is Fraction else Fraction(other)
        self.top, self.bottom = self.__mul(self.top, other.bottom, self.bottom, other.top)
        return self
    
    def __mul(self, top1, top2, bottom1, bottom2):  # умножение (деление) дробей
        new_top = top1 * top2
        new_bottom = bottom1 * bottom2
        new_top, new_bottom = self.__check_fraction(new_top, new_bottom)
        new_top, new_bottom = self.__change_fraction(new_top, new_bottom)
        return new_top, new_bottom

    def reverse(self):
        new_top, new_bottom = self.bottom, self.top
        new_top, new_bottom = self.__check_fraction(new_top, new_bottom)
        return Fraction(new_top, new_bottom)

    def __lt__(self, other):  # <                     # Идея: вычесть из self other
        other = other if type(other) is Fraction else Fraction(other)
        new_top, new_bottom = self.__sum(other, "-")  # и проверить результат
        return new_top < 0                            # Пример: 2/5 < 3/5 => 2/5 - 3/5 < 0
    
    def __le__(self, other):  # <=
        other = other if type(other) is Fraction else Fraction(other)
        new_top, new_bottom = self.__sum(other, "-")
        return new_top <= 0
    
    def __eq__(self, other):  # ==
        other = other if type(other) is Fraction else Fraction(other)
        new_top, new_bottom = self.__sum(other, "-")
        return new_top == 0
        
    def __ne__(self, other):  # !=
        other = other if type(other) is Fraction else Fraction(other)
        new_top, new_bottom = self.__sum(other, "-")
        return new_top != 0
        
    def __gt__(self, other):  # >
        other = other if type(other) is Fraction else Fraction(other)
        new_top, new_bottom = self.__sum(other, "-")
        return new_top > 0
        
    def __ge__(self, other):  # >=
        other = other if type(other) is Fraction else Fraction(other)
        new_top, new_bottom = self.__sum(other, "-")
        return new_top >= 0
