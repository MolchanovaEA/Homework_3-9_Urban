# Вариант № 1.

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
count_ = 0

def calk(i):
    global count_       # Объявляем, что будем использовать глобальную переменную
    if isinstance(i, str):
        count_ += len(i)
    if isinstance(i, (int, float)):
        count_ += i
    if isinstance(i, dict):
        for key, value in i.items():
            if isinstance(key, str):
                count_ += len(key)
            if isinstance(value, str):
                count_ += len(value)
            if isinstance(key, int):
                count_ += key
            if isinstance(value, int):
                count_ += value
    return count_

def unpacking(args):
    for i in args:
        if isinstance(i, (str, int, dict)):
            calk(i)         # Обрабатываем текущий элемент
        else:
            unpacking(i)    # Рекурсивный вызов для вложенных структур

    return count_

result = unpacking(data_structure)
print(result)


# Вариант № 2.

def calculate_structure_sum(data_structure):
    summa = 0
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summa += calculate_structure_sum(item)
    elif isinstance(data_structure, (int, float)):
        summa += data_structure
    elif isinstance(data_structure, str):
        summa += len(data_structure)
    return summa

result = calculate_structure_sum(data_structure)
print(result)