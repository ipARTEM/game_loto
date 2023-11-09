phrase = "В чащах юга жил бы цитрус? Да, но фальшивый экземпляр!"

lst = list(phrase)

print(f'Количество символов во фразе до буквы "e": {lst.index("е")}')


def to_list(arg):
    new_list = []
    new_list.append(arg)
    return new_list


ans = to_list((1, 2, 3))
print(ans)

ans = to_list(('Молоко', 5, '2020 года'))
print(ans)

ans = to_list(([3, 4, 7], 8.3, True, 'Строка'))
print(ans)

while True:
    try:
        num = int(input('Введите цифру от 1 до 9 и увидите таблицу умножения для данного числа: '))
        if 0 < num < 10:
            for i in range(0, 10):
                print(f'{i}*{num}={num * i}')
            break
    except:
        print('Вы ввели не целочисленное число')



