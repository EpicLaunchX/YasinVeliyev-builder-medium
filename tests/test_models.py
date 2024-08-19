from src.pytemplate.domain import Burger


def test_burger():
    burger = Burger()
    assert burger.__str__() == f"Burger{{{burger.bread}\n\t{burger.sauce or "no sauce"}\n\t{burger.patty}\n\t{burger.toppings or "no toppings"}\n\t}}"


def test_burger_if_sauce_is_none():
    burger = Burger()
    burger.sauce =None
    assert burger.__str__() == f"Burger{{{burger.bread}\n\tno sauce\n\t{burger.patty}\n\tno toppings\n\t}}"


def test_burger_if_toppings_is_none():
    burger = Burger()
    burger.toppings =None
    assert burger.__str__() == f"Burger{{{burger.bread}\n\t{burger.sauce}\n\t{burger.patty}\n\tno toppings\n\t}}"