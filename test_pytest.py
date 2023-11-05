import random_card
import main


def test_barrels_mix():
    barrels = random_card.barrels_mix()
    assert len(barrels) == 90


def test_field():
    rtn = main.field()
    assert rtn == None



