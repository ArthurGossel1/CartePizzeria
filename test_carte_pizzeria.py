from unittest.mock import PropertyMock

from mock import Mock, patch

from carte_pizzeria import CartePizzeria, CartePizzeriaException


def test_carte_pizza_is_empty():
    c = CartePizzeria()
    assert c.is_empty()


@patch('carte_pizzeria.CartePizzeria.pizzas', new_callable=PropertyMock)
def test_carte_pizza_is_not_empty(mock_pizzas):
    c = CartePizzeria()
    element = Mock()
    mock_pizzas.return_value = [element]
    assert not c.is_empty()


def test_carte_pizza_nb_pizzas_with_no_pizzas():
    c = CartePizzeria()
    assert c.nb_pizzas() == 0

#slt


