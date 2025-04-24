# Чек - 2

import pandas as pd


def cheque(price_list, **shopping_list) -> pd.DataFrame:
    shopping_list = dict(sorted(shopping_list.items()))  # Сортировка списка покупок по названиям
    total = dict()                                       # Формирование таблицы
    total["product"] = [product for product in shopping_list.keys()]
    total["price"] = [int(price_list[product]) for product in total["product"]]
    total["number"] = [number for number in shopping_list.values()]
    total["cost"] = [total["price"][i] * total["number"][i] for i in range(len(shopping_list))]

    return pd.DataFrame(total)
