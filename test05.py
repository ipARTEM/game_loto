"""
Вы обрабатываете данные, но при работе со списком у вас происходит ошибка.
 Вам нужно понять, какие элементы вашего списка не числовые (тип не int и не float).
Задание 1. Выведите индексы всех таких элементов списка.
Пример:
для списка
[3, 124, 0.45, 'привет', {'ребята' : 2}, 31.4 , 'люди', 34, (12, 44)]
на выходе должно получиться: 3, 4, 6, 8
Замечание. (12, 44) - это не число, а кортеж из двух чисел.
Задание 2. Выведите новый список, содержащий только числа.
Для примера выше:

[3, 124, 0.45, 31.4, 34]
"""

lst = [3, 124, 0.45, 'привет', {'ребята': 2}, 31.4, 'люди', 34, (12, 44)]

def ind(lst):
    for i in lst:
        if type(i) == int:
            # print(i)
            pass
        elif type(i) == float:
            # print(i)
            pass
        elif lst.index(i) == len(lst)-1:
            print(lst.index(i), end='')
        else:
            print(lst.index(i), end=', ')

def num(lst):
    new_lst=[]
    for i in lst:
        if type(i) == int:
            new_lst.append(i)
        elif type(i) == float:
            new_lst.append(i)

    return  new_lst

ind(lst)
print()
new_lst=num(lst)
print(new_lst)


