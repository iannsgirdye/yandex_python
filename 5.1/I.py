# Очередь

class Queue:
    
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        return self.stack.pop(0)
        
    def is_empty(self):
        return len(self.stack) == 0
