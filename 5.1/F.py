# Классный прямоугольник 2.0

class Rectangle:
    
    def __init__(self, corner1, corner2):
        self.left_x, self.right_x = sorted([corner1[0], corner2[0]])
        self.right_y, self.left_y = sorted([corner1[1], corner2[1]])
        self.side_x = self.right_x - self.left_x
        self.side_y = self.left_y - self.right_y
    
    def perimeter(self):
        return round(self.side_x * 2 + self.side_y * 2, 2)
        
    def area(self):
        return round(self.side_x * self.side_y, 2)
    
    def get_pos(self):
        return round(self.left_x, 2), round(self.left_y, 2)
    
    def get_size(self):
        return round(self.side_x, 2), round(self.side_y, 2)
    
    def move(self, dx, dy):
        self.left_x += dx
        self.right_x += dx
        self.left_y += dy
        self.right_y += dy
        
    def resize(self, width, height):
        self.side_x = width
        self.side_y = height
        self.right_x = self.left_x + self.side_x
        self.right_y = self.left_y + self.side_y
