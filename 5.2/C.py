# Классная точка 5.0

import math


class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self, dx, dy):  # dx = delta x, dy = delta y
        self.x += dx
        self.y += dy
        
    def length(self, second_point):  # nx = necessary x, ny = necessary y
        nx, ny = self.__get_location(second_point)
        dx = self.x - nx
        dy = self.y - ny
        result = math.sqrt(dx ** 2 + dy ** 2)
        return round(result, 2)
    
    def __get_location(self, point):
        return point.x, point.y


class PatchedPoint(Point):
    
    def __init__(self, x=0, y=0):
        if type(x) is tuple:  # Передан 1 параметр
            self.x = x[0]
            self.y = x[1]
        else:                 # Передано 0 или 2 параметра
            self.x = x
            self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"

    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])
    
    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self
