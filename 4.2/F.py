# Кофейня

recipes = {
    "Эспрессо": (1, 0, 0), 
    "Капучино": (1, 3, 0), 
    "Макиато": (2, 1, 0), 
    "Кофе по-венски": (1, 0, 2), 
    "Латте Макиато": (1, 2, 1), 
    "Кон Панна": (1, 0, 1)
}


def order(*coffee):
    global recipes, in_stock
    message = 'К сожалению, не можем предложить Вам напиток'
    for drink in coffee:
        in_stock["coffee"] -= recipes[drink][0]
        in_stock["milk"] -= recipes[drink][1]
        in_stock["cream"] -= recipes[drink][2]
        if all([in_stock["coffee"] >= 0, in_stock["milk"] >= 0, in_stock["cream"] >= 0]):
            return drink
        else:
            in_stock["coffee"] += recipes[drink][0]
            in_stock["milk"] += recipes[drink][1]
            in_stock["cream"] += recipes[drink][2]
    return message
