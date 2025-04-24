# Акция

import pandas as pd


def cheque(price_list: pd.Series, **shopping_list) -> pd.DataFrame:
    shopping_list = dict(sorted(shopping_list.items()))  # Сортировка списка покупок по названиям
    total = dict()                                       # Формирование таблицы
    total["product"] = [product for product in shopping_list.keys()]
    total["price"] = [int(price_list[product]) for product in total["product"]]
    total["number"] = [number for number in shopping_list.values()]
    total["cost"] = [total["price"][i] * total["number"][i] for i in range(len(shopping_list))]

    return pd.DataFrame(total)


def discount(total: pd.DataFrame) -> pd.DataFrame:
    new_total = total.copy()
    for i in range(len(new_total)):
        if new_total["number"][i] > 2:
            new_total["cost"][i] = new_total["cost"][i] / 2.0
        else:
            new_total["cost"][i] = new_total["cost"][i] / 1.0

    return new_total
