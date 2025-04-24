# Классная точка 2.0

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
