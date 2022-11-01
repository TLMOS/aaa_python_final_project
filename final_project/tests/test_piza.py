import pytest
from final_project.pizza.pizza import Pizza, Margherita, Pepperoni, Hawaiian


def test_pizza():
    """Test pizza class."""
    pizza = Pizza('L')
    assert pizza.size == 'L'
    assert pizza.icon == '🍕'
    assert pizza.components == []


def test_margherita():
    """Test margherita class."""
    pizza = Margherita('L')
    assert pizza.size == 'L'
    assert pizza.icon == '🧀'
    assert pizza.components == ['tomato sauce', 'mozzarella', 'tomatoes']


def test_pepperoni():
    """Test pepperoni class."""
    pizza = Pepperoni('L')
    assert pizza.size == 'L'
    assert pizza.icon == '🍕'
    assert pizza.components == ['tomato sauce', 'mozzarella', 'pepperoni']


def test_hawaiian():
    """Test hawaiian class."""
    pizza = Hawaiian('L')
    assert pizza.size == 'L'
    assert pizza.icon == '🍍'
    assert pizza.components == ['tomato sauce', 'mozzarella', 'chicken',
                                'pineapple']


def test_wrong_size():
    """Test wrong size."""
    with pytest.raises(ValueError):
        Pizza('M')


def test_equal_pizza():
    """Test equal pizza."""
    pizza1 = Margherita('L')
    pizza2 = Margherita('L')
    assert pizza1 == pizza2


def test_unequal_pizza():
    """Test unequal pizza."""
    pizza1 = Margherita('L')
    pizza2 = Pepperoni('L')
    assert pizza1 != pizza2

    pizza1 = Margherita('L')
    pizza2 = Margherita('XL')
    assert pizza1 != pizza2


def test_equal_other_type():
    """Test equal other type."""
    pizza = Margherita('L')
    assert pizza != 'pizza'


def test_pizza_dict():
    """Test pizza dict."""
    pizza = Margherita('L')
    assert pizza.dict() == {'Margherita': ['tomato sauce', 'mozzarella',
                                           'tomatoes']}
