"""
Попробуйте написать простую карточную игру. Играют два игрока - player_1 и player_2. У каждого из них по 6 карт.

player_1 = [6, 10, 7, 8, 9, 6]
player_2 = [10, 7, 9, 6, 10, 7]
Необходимо, используя операторы for, if и elif, сыграть одну партию. Игроки ходят по очереди, и тот,
 у кого достоинство карты больше, забирает себе карту противника. Сыгранные карты больше не используются.
  Достоинства карт в списке берутся по порядку, например:

первый ход: (6, 10);
второй ход: (10, 7).
Побеждает тот, у кого по окончании игры на руках меньшая сумма достоинств карт.

Кто победил, player_1 или player_2?
"""
import time

player_1 = [6, 10, 7, 8, 9, 6]
player_2 = [10, 7, 9, 6, 10, 7]

bag_1=[]
bag_2=[]
print('Игра началась)) ')

score_1=0
score_2=0
for i in range(6):
    print(f'Ход {i+1}:')
    print(f'player_1: {player_1[i]};   player_2: {player_2[i]}')
    if player_1[i]>player_2[i]:
        print('Карты забрал player_1')
        bag_1.append(player_1[i])
        bag_1.append(player_2[i])
        score_1+=player_1[i]
        score_1+=player_2[i]

    if player_1[i]<player_2[i]:
        print('Карты забрал player_2')
        bag_2.append(player_1[i])
        bag_2.append(player_2[i])
        score_2 += player_1[i]
        score_2 += player_2[i]
    print()
    time.sleep(2)

print(f'player_1 забрал карты: {bag_1}; на сумму: {score_1}')
print(f'player_2 забрал карты: {bag_2}; на сумму: {score_2}')
print()
if score_1<score_2:
    print(f'Победил player_1')
else:
    print(f'Победил player_2')




