my_dict = {}
# print(type(my_dict))

rainbow = ["каждый", "охотник", "желает", "знать", "где", "сидит", "фазан"]

string = ''

for el in rainbow:
    string += el + ' '
# print(string)

purchases = [1200, 800, 468, 235, 5800, 1350, 110, 243,
             767, 3500, 5400, 4389, 3690, 2420, 894,
             1766, 2100, 450, 328, 1890, 233, 766, 1765,
             237, 679, 1983, 389, 1760, 2100, 253, 789]

counter = 0
sum_pch_while = 0
sum_pch_for = 0
sum_pch_sum = 0
while True:
    try:
        sum_pch_while += purchases[counter]
    except:
        break
    counter += 1
# print(sum_pch_while)

for i in purchases:
    sum_pch_for += i
# print(sum_pch_for)

sum_pch_sum = sum(purchases)


# print(sum_pch_sum)

# print(f'Траты за месяц составили: {sum_pch_while} рубля')
# print(f'Траты за месяц составили: {sum_pch_for} рубля')
# print(f'Траты за месяц составили: {sum_pch_sum} рубля')


# print(type(tpl))
def del_from_tuple(tpl, elem):
    tpl = list(tpl)
    for el in tpl:
        if el == elem:
            tpl.remove(elem)
            break
    # print(tpl)
    return tuple(tpl)


# Вариант 1
tpl = 1, 2, 3
print(f'Кортеж:{tpl}')
elem = 1
print(f'Элемент: {elem}')
tpl = del_from_tuple(tpl, elem)
print(type(tpl))
print(f'Кортеж без заданного элемента: {tpl}')

# Вариант 2
tpl = 1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2
print(f'Кортеж:{tpl}')
elem = 3
print(f'Элемент: {elem}')
tpl = del_from_tuple(tpl, elem)
print(type(tpl))
print(f'Кортеж без заданного элемента: {tpl}')

# Вариант 3
tpl = 2, 4, 6, 6, 4, 2
print(f'Кортеж:{tpl}')
elem = 9
print(f'Элемент: {elem}')
tpl = del_from_tuple(tpl, elem)
print(type(tpl))
print(f'Кортеж без заданного элемента: {tpl}')
