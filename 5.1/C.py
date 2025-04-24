# Не нажимай красную кнопку!

class RedButton:
    
    def __init__(self):
        self.clicks = 0
    
    def click(self):
        print("Тревога!")
        self.clicks += 1
        
    def count(self):
        return self.clicks
