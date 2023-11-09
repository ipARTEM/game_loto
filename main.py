import sys
import time

import game_card
import random_card

if __name__=='__main__':
    play1 = []
    comp = []
    answer = 'ку'
    name='No name'
    data = {'ans': 0, 'barrels_comp': 15, 'barrels_play1': 15}

    print('Добро пожаловать в игру ЛОТО')
    name = input('Как к Вам обращаться: ')
    input('Выберите карточку, нажав любую клавишу!')


    # play1=game_card.Game_Card
    # play1.card_selection()


    def pr_card(card):
        """
        Печать карточки
        :param card:
        :return:
        """
        print('*' * 40)
        print(card[0])
        print(card[1])
        print(card[2])
        print('*' * 40)
        print()


    def field():
        """
        Печать поля
        :return:
        """
        print('Карточка компьютера: ')
        pr_card(comp)
        print()
        print(f'Карточка игрока {name}: ')
        pr_card(play1)
        print()


    def steep():
        """
        Шаг игры
        :return:
        """
        print()
        print('Происходит перемешивание бочонков.....')
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print('Бочонки перемешаны. Начинаем игру!')
        time.sleep(1)


    # Боченки текущей игры
    barrels_game = random_card.barrels_mix()


    def check_card(play, barrel):
        pass


    def checking_cards(play1, comp, barrel, answer):
        """
        Проверка карточек
        :param play1:
        :param comp:
        :param barrel:
        :return:
        """

        for line in comp:
            for index, item in enumerate(line):
                if item == barrel:
                    line[index] = 'XX'
                    data['barrels_comp'] -= 1

        for line in play1:
            for index, item in enumerate(line):
                if item == barrel:
                    line[index] = 'XX'
                    data['barrels_play1'] -= 1
                    if answer == '0':
                        print(f'Вы проиграли, так как у Вас есть бочонок №{barrel}')
                        data['ans'] = 0
                        return data
                    data['ans'] = 1
                    return data
        if answer == '1':
            print(f'Вы проиграли, так как у Вас нет бочонка №{barrel}, а Вы отметили, что есть!')
            data['ans'] = 0
            return data
        print(f'Значение answer: {answer}')
        data['ans'] = 1
        return data


    # print(barrels_game)
    def game():
        """
        Игра
        :return:
        """
        counter = 0
        while True:
            steep()

            for barrel in barrels_game:
                field()
                print(f'Вытащен бочонок №{barrel}:')
                print()
                while True:
                    answer = input('Если у Вас есть данный бочонок нажмите "1", если нет, то "0" ')
                    if answer == '1':
                        print('1')
                        break
                    if answer == '0':
                        print('0')
                        break

                data = checking_cards(play1, comp, barrel, answer)
                if data['ans'] == 0:
                    sys.exit(0)
                print('Прошёл проверку')
                print(f'Ответ: {data} ')

                for k, v in data.items():
                    if k == 'barrels_comp' and v == 0:
                        print('Компьютер выиграл!')
                        sys.exit(0)

                for k, v in data.items():
                    if k == 'barrels_play1' and v == 0:
                        print('Вы выиграли! УРА!!!')
                        sys.exit(0)


    while True:
        play1 = random_card.new_card()
        pr_card(play1)
        select = input('Нажмите "1" для выбора данной карточки или любую клавишу для продолжения выбора: ')

        if select == '1':
            break

        print()
        print()

    # print('333')
    # print(play1)

    print('Компьютер выбирает такую карточку: ')
    comp = random_card.new_card()
    pr_card(comp)

    game()
