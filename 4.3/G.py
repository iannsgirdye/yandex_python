# Однотипность не порок

def same_type(f):
    def decorator(*args):
        message = "Обнаружены различные типы данных"
        
        if not (type(args[0]) is type(args[1])):
            print(message)
            return 0
        else:
            return f(*args)
        
    return decorator