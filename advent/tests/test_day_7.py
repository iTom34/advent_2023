import pytest

from advent.day_7 import Card, car_to_card


@pytest.mark.parametrize("car, expected", [('A', Card.a),
                                                ('K', Card.k),
                                                ('Q', Card.q),
                                                ('J', Card.j),
                                                ('T', Card.t),
                                                ('9', Card.nine),
                                                ('8', Card.height),
                                                ('7', Card.seven),
                                                ('6', Card.six),
                                                ('5', Card.five),
                                                ('4', Card.four),
                                                ('3', Card.three),
                                                ('2', Card.two)])
def test_car_to_card(car: str, expected: Card):
    assert car_to_card(car) == expected
