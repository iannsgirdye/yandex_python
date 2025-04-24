# Модернизация системы вывода

printed = set()


def modern_print(line):
    global printed
    if line not in printed:
        print(line)
        printed.add(line)
