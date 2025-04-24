# Дроби v0.1

import math


class Fraction:
    
    def __init__(self, *args):
        if len(args) == 1:
            self.top, self.bottom = map(int, args[0].split("/"))
        else:
            self.top, self.bottom = args[0], args[1]
        self.__change_fraction()
        
    def numerator(self, number=None):
        if number is None:
            return self.top
        self.top = number
        self.__change_fraction()
            
    def denominator(self, number=None):
        if number is None:
            return self.bottom
        self.bottom = number
        self.__change_fraction()
        
    def __str__(self):
        return f"{self.top}/{self.bottom}"
    
    def __repr__(self):
        return f"Fraction({self.top}, {self.bottom})"

    def __change_fraction(self):
        divisor = math.gcd(self.top, self.bottom)
        self.top //= divisor
        self.bottom //= divisor
