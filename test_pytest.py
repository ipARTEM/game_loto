import random_card
import main
import magic_game


class TestGameLoto:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_barrels_mix(self):
        barrels = random_card.barrels_mix()
        assert len(barrels) == 90

    def test_end_line(self):
        end_barrels = random_card.new_card()
        assert type(end_barrels) == list

    def test_number_of_barrels(self):
        m=magic_game.Magic_game('Cris', 'Sofia').number_of_barrels()
        assert  m==90

    def test_equality(self):
        m1 = magic_game.Magic_game('Cris', 'Sofia')
        assert str(m1) == 'Имя игрока 1: Cris. Имя игрока 2: Sofia'

    def test_not_equality(self):
        m=magic_game.Magic_game('Cris', 'Sofia')
        assert m.player1!=m.player2

    def test_more(self):
        m=magic_game.Magic_game('Cris', 'Sofia')
        assert m.player2>m.player1

# def test_steep():
#     rtn = main.steep()
#     print(rtn)
#     assert rtn == None
