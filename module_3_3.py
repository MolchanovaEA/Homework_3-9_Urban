#Задача  "Распаковка"
print()
print('1. Функция с параметрами по умолчанию:')
print()
def print_params (a=1, b='строка', c=True):
    print (a, b, c)
print_params()
print_params(1)
print_params(1, 'строка')
print_params(1, 'строка', True)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(1, b=False)
print_params(True, 'строка', 1)
print_params(12, '+++', {2, 2, 2})
#print_params(a=3, 'строка', True)   # Ошибка, т.к именованный параметр стоит перед позиционными параметрами)

print()
print('2. Распаковка  параметров:')
print()
values_list = [7, 'Azerty', (True, False)]
values_dict = {'a':11.01, 'b':'You', 'c':[10, 20, 30, 40, 50]}
print_params(*values_list)
print_params(**values_dict)

print()
print('2. Распаковка + отдельные параметры:')
print()
values_list_2 = [{'яблоки':'1 кг', 'сливы':'0,5 кг'}, 'Москва']
print_params(*values_list_2, 42)