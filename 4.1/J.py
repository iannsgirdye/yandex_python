# Слияние


def merge(first, second):
    data_in = list(first) + list(second)
    data_out = []
    while len(data_in) > 0:
        data_out.append(min(data_in))
        data_in.remove(min(data_in))
    return tuple(data_out)
