import random_card
import main

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


# def test_steep():
#     rtn = main.steep()
#     print(rtn)
#     assert rtn == None
