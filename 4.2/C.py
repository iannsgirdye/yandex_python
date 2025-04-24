# Функциональный нод 2.0


def gcd(*numbers):
    all_dels = [f(number) for number in numbers]
    new_all_dels = list()
    for element in all_dels:
        new_all_dels += element
    
    dels_in_all = set()
    for delit in new_all_dels:
        if new_all_dels.count(delit) == len(all_dels):
            dels_in_all.add(delit)
    
    return max(dels_in_all)
    

def f(n):
    all_del = list()
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            all_del.append(d)
            if (n // d) != d:
                all_del.append(n // d)
    return all_del
