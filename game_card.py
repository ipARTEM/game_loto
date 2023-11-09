import random


class Game_Card:
    def card_selection(self):
        """
        Выбор игровай карточки
        :return:
        """
        print('Карточка выбрана!')
        random.randint(100)





if __name__=='__main__':

    # Создать объект карточки
    new_card=Game_Card()
    print(new_card)

    print(new_card.card_selection())