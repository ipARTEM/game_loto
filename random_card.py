import random


def barrels_mix():
    """
    Создание и перемешивание боченков
    :return:
    """
    barrels = [i for i in range(1, 91)]
    # print(barrels)
    random.shuffle(barrels)
    return barrels


def new_card():
    # card=random.randint(100)
    card_mix = []
    barrels = barrels_mix()

    # print(barrels)
    # line1 = barrels[:10]
    # line2 = barrels[10:20]
    # line3 = barrels[20:30]
    #
    # print(line1)
    # print(line2)
    # print(line3)
    numbers1_10 = []
    numbers11_20 = []
    numbers21_30 = []
    numbers31_40 = []
    numbers41_50 = []
    numbers51_60 = []
    numbers61_70 = []
    numbers71_80 = []
    numbers81_90 = []

    new_barrels = []

    for i in barrels:
        # print(barrels[i])
        if 0 < i <= 10:
            numbers1_10.append(i)
    new_barrels.append(numbers1_10)
    # print(numbers1_10)
    # print(new_barrels)

    for i in barrels:
        # print(barrels[i])
        if 10 < i <= 20:
            numbers11_20.append(i)
    new_barrels.append(numbers11_20)

    for i in barrels:
        # print(barrels[i])
        if 20 < i <= 30:
            numbers21_30.append(i)
    new_barrels.append(numbers21_30)

    for i in barrels:
        # print(barrels[i])
        if 30 < i <= 40:
            numbers31_40.append(i)
    new_barrels.append(numbers31_40)

    for i in barrels:
        # print(barrels[i])
        if 40 < i <= 50:
            numbers41_50.append(i)
    new_barrels.append(numbers41_50)

    for i in barrels:
        # print(barrels[i])
        if 50 < i <= 60:
            numbers51_60.append(i)
    new_barrels.append(numbers51_60)

    for i in barrels:
        # print(barrels[i])
        if 60 < i <= 70:
            numbers61_70.append(i)
    new_barrels.append(numbers61_70)

    for i in barrels:
        # print(barrels[i])
        if 70 < i <= 80:
            numbers71_80.append(i)
    new_barrels.append(numbers71_80)

    for i in barrels:
        # print(barrels[i])
        if 80 < i <= 90:
            numbers81_90.append(i)
    new_barrels.append(numbers81_90)

    # for n in numbers1_10:
    #     print(n)
    # print(numbers1_10)
    # print(numbers11_20)
    # print(numbers21_30)
    # print(numbers31_40)
    # print(numbers41_50)
    # print(numbers51_60)
    # print(numbers61_70)
    # print(numbers71_80)
    # print(numbers81_90)

    x = [i for i in range(9)]
    random.shuffle(x)
    # print(x)
    x1 = x[:5]
    # print(x1[0])
    random.shuffle(x)
    # print(x)
    x2 = x[:5]
    random.shuffle(x)
    # print(x)
    x3 = x[:5]
    # print(x1)
    line1 = []
    line2 = []
    line3 = []
    # print(new_barrels)
    random.shuffle(new_barrels)
    # print(new_barrels)
    # print()
    for i in range(5):
        line1.append(new_barrels[x1[i]][0])
    for i in range(5):
        line2.append(new_barrels[x2[i]][1])
    for i in range(5):
        line3.append(new_barrels[x3[i]][2])
    #
    # print(line1)
    # print(line2)
    # print(line3)

    line1 = sorted(line1)
    line2 = sorted(line2)
    line3 = sorted(line3)

    # print()
    # print(line1)
    # print(line2)
    # print(line3)

    def end_line(line1):
        line1end = ['_', '_', '_', '_', '_', '_', '_', '_', '_', ]
        for i in line1:
            if 0 < i <= 10:
                line1end[0] = i

            if 10 < i <= 20:
                line1end[1] = i

            if 20 < i <= 30:
                line1end[2] = i

            if 30 < i <= 40:
                line1end[3] = i

            if 40 < i <= 50:
                line1end[4] = i

            if 50 < i <= 60:
                line1end[5] = i

            if 60 < i <= 70:
                line1end[6] = i

            if 70 < i <= 80:
                line1end[7] = i

            if 80 < i <= 90:
                line1end[8] = i

        return line1end

    # print()

    end_barrels = [[], [], []]
    end_barrels[0] = end_line(line1)
    end_barrels[1] = end_line(line2)
    end_barrels[2] = end_line(line3)

    # print(end_barrels)
    return end_barrels

# new_card()
