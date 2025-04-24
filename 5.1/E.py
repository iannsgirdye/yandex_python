# Классный прямоугольник

class Rectangle:
    
    def __init__(self, corner1, corner2):
        self.x1, self.y1 = corner1[0], corner1[1]
        self.x2, self.y2 = corner2[0], corner2[1]
        self.side1 = abs(self.x1 - self.x2)
        self.side2 = abs(self.y1 - self.y2)
    
    def perimeter(self):
        return round(self.side1 * 2 + self.side2 * 2, 2)
        
    def area(self):
        return round(self.side1 * self.side2, 2)
