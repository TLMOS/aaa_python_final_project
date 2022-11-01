from final_project.pizza.pizza import Pizza
from final_project.pizza.pizza_processing import log, bake, deliver, pickup
from final_project.tests.utils import remove_digits


def test_log_default(capsys):
    """Test log decorator with default message."""
    @log()
    def test():
        pass
    test()
    captured = capsys.readouterr()
    assert remove_digits(captured.out) == 'test - c!\n'


def test_log_parametrized(capsys):
    """Test log decorator with custom message."""
    @log('Running test, duration: {}')
    def test():
        pass
    test()
    captured = capsys.readouterr()
    assert remove_digits(captured.out) == 'Running test, duration: \n'


def test_bake(capsys):
    """Test bake function."""
    pizza = Pizza('L')
    bake(pizza)
    captured = capsys.readouterr()
    assert remove_digits(captured.out) == '🍳 Приготовили за с!\n'


def test_deliver(capsys):
    """Test deliver function."""
    pizza = Pizza('L')
    deliver(pizza)
    captured = capsys.readouterr()
    assert remove_digits(captured.out) == '🛵 Доставили за с!\n'


def test_pickup(capsys):
    """Test pickup function."""
    pizza = Pizza('L')
    pickup(pizza)
    captured = capsys.readouterr()
    assert remove_digits(captured.out) == '🏠 Забрали за с!\n'


def test_bake_unwrapped(capsys):
    """Test bake function without decorator."""
    pizza = Pizza('L')
    result = bake.__wrapped__(pizza)
    captured = capsys.readouterr()
    assert captured.out == ''
    assert result is None


def test_deliver_unwrapped(capsys):
    """Test deliver function without decorator."""
    pizza = Pizza('L')
    result = deliver.__wrapped__(pizza)
    captured = capsys.readouterr()
    assert captured.out == ''
    assert result is None


def test_pickup_unwrapped(capsys):
    """Test pickup function without decorator."""
    pizza = Pizza('L')
    result = pickup.__wrapped__(pizza)
    captured = capsys.readouterr()
    assert captured.out == ''
    assert result is None
