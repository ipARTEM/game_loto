game LOTO

Программа представляет собой простую реализацию игры в лото по специальным правилам, взаимодействует с пользователем при помощи интерфейса командной строки.

Правила игры:
Игра ведется с помощью специальных карточек, на которых отмечены числа, и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, расположенных в соответствии с ячейкой десятка.
Все цифры в карточке уникальны.

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран. Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.

Если игрок выбрал "зачеркнуть":

если цифра есть на карточке - она зачеркивается и игра продолжается.
если цифры на карточке нет - игрок проигрывает и игра завершается.

Если игрок выбрал "продолжить":

если цифра есть на карточке - игрок проигрывает и игра завершается.
если цифры на карточке нет - игра продолжается. Побеждает тот, кто первый закроет все числа на своей карточке.