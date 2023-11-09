"""
Напишите функцию, которая выбирает 2-х значные числа из списка с помощью функции filter
 и возвращает результат новым списком.


"""
import os
# Возвращает True для чётных чисел.
def is_even(x):
    return x % 2 == 0

# у нас есть некий список numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Вызываем функцию filter для нашего списка, используя функцию
list(filter(is_even, numbers))

lst = [96, 186, 11, 116, 183,  95, 181, 95, 55, 128, 54, 24, 21, 198, 118, 46, 166, 137, 24]

# new_lst=[]
# def double_digit(lst):
#     for i in lst:
#         if 9<i<100:
#             new_lst.append(i)
#     return new_lst
#
# new_lst=double_digit(lst)

# print(new_lst)


def is_dbl_digit(lst):
    return 9<lst<100
lst_new=list(filter(is_dbl_digit,lst))

print(lst_new)

"""
Создайте в директории /content папку my_folder и запишите в ней 10 файлов.
"""
#
# name_dir='content'
# if not os.path.exists(name_dir):
#     os.mkdir(name_dir)
# os.chdir(name_dir)
# for i in range(10):
#     fl=f'test{i}.txt'
#     if not os.path.exists(fl):
#         new_file = open(fl, 'w')
#         new_file.close()


""""
Создайте код, который применяет функцию map к списку слов
 и использует анонимную функцию lambda для инвертирования порядка букв в каждом слове.
"""

lst=['дом', 'квартира', 'поместье']
print(lst)

def inverting(lst):
    inv=''
    for i in lst:
        inv=''.join(reversed(lst))
    return inv

new_lst=list(map(inverting,lst))
print(new_lst)