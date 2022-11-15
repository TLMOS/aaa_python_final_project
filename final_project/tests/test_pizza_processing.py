from unittest.mock import patch
from final_project.pizza.pizza import Pizza, Size
from final_project.pizza.pizza_processing import log, bake, deliver, pickup


@patch('random.randint', side_effect=lambda a, b: 1)
def test_log_default(mocked_randint, capsys):
    """Test log decorator with default message."""
    @log()
    def test():
        pass
    test()
    captured = capsys.readouterr()
    assert captured.out == 'test - 1c!\n'


@patch('random.randint', side_effect=lambda a, b: 1)
def test_log_parametrized(mocked_randint, capsys):
    """Test log decorator with custom message."""
    @log('Running test, duration: {}')
    def test():
        pass
    test()
    captured = capsys.readouterr()
    assert captured.out == 'Running test, duration: 1\n'


@patch('random.randint', side_effect=lambda a, b: 1)
def test_bake(mocked_randint, capsys):
    """Test bake function."""
    pizza = Pizza(Size.L)
    bake(pizza)
    captured = capsys.readouterr()
    assert captured.out == '🍳 Приготовили за 1с!\n'


@patch('random.randint', side_effect=lambda a, b: 1)
def test_deliver(mocked_randint, capsys):
    """Test deliver function."""
    pizza = Pizza(Size.L)
    deliver(pizza)
    captured = capsys.readouterr()
    assert captured.out == '🛵 Доставили за 1с!\n'


@patch('random.randint', side_effect=lambda a, b: 1)
def test_pickup(mocked_randint, capsys):
    """Test pickup function."""
    pizza = Pizza(Size.L)
    pickup(pizza)
    captured = capsys.readouterr()
    assert captured.out == '🏠 Забрали за 1с!\n'


def test_bake_unwrapped(capsys):
    """Test bake function without decorator."""
    pizza = Pizza(Size.L)
    result = bake.__wrapped__(pizza)
    captured = capsys.readouterr()
    assert captured.out == ''
    assert result is None


def test_deliver_unwrapped(capsys):
    """Test deliver function without decorator."""
    pizza = Pizza(Size.L)
    result = deliver.__wrapped__(pizza)
    captured = capsys.readouterr()
    assert captured.out == ''
    assert result is None


def test_pickup_unwrapped(capsys):
    """Test pickup function without decorator."""
    pizza = Pizza(Size.L)
    result = pickup.__wrapped__(pizza)
    captured = capsys.readouterr()
    assert captured.out == ''
    assert result is None
