from final_project.pizza.pizza import Pizza, Size
from final_project.pizza.pizza import Margherita, Pepperoni, Hawaiian


def test_pizza():
    """Test pizza class."""
    pizza = Pizza(Size.L)
    assert pizza.size == Size.L
    assert pizza.icon == '🍕'
    assert pizza.components == []


def test_margherita():
    """Test margherita class."""
    pizza = Margherita(Size.L)
    assert pizza.size == Size.L
    assert pizza.icon == '🧀'
    assert pizza.components == ['tomato sauce', 'mozzarella', 'tomatoes']


def test_pepperoni():
    """Test pepperoni class."""
    pizza = Pepperoni(Size.L)
    assert pizza.size == Size.L
    assert pizza.icon == '🍕'
    assert pizza.components == ['tomato sauce', 'mozzarella', 'pepperoni']


def test_hawaiian():
    """Test hawaiian class."""
    pizza = Hawaiian(Size.L)
    assert pizza.size == Size.L
    assert pizza.icon == '🍍'
    assert pizza.components == ['tomato sauce', 'mozzarella', 'chicken',
                                'pineapple']


def test_equal_pizza():
    """Test equal pizza."""
    pizza1 = Margherita(Size.L)
    pizza2 = Margherita(Size.L)
    assert pizza1 == pizza2


def test_unequal_pizza():
    """Test unequal pizza."""
    pizza1 = Margherita(Size.L)
    pizza2 = Pepperoni(Size.L)
    assert pizza1 != pizza2

    pizza1 = Margherita(Size.L)
    pizza2 = Margherita(Size.XL)
    assert pizza1 != pizza2


def test_equal_other_type():
    """Test equal other type."""
    pizza = Margherita(Size.L)
    assert pizza != 'pizza'


def test_pizza_dict():
    """Test pizza dict."""
    pizza = Margherita(Size.L)
    assert pizza.dict() == {'Margherita': ['tomato sauce', 'mozzarella',
                                           'tomatoes']}
