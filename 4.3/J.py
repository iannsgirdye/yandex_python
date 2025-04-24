# "Выпрямление" списка

def make_linear(data):
    new_data = []
    
    for element in data:
        if type(element) is list:
            new_data += [subelement for subelement in make_linear(element)]
        else:
            new_data += [element]
    
    return new_data
