from click.testing import CliRunner
from final_project.pizza.cli import cli
from final_project.tests.utils import remove_digits


def test_order_pickup():
    """Test order command."""
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'margherita', 'L'])
    assert result.exit_code == 0
    output_lines = remove_digits(result.output).splitlines()
    assert '🍳 Приготовили за с!' == output_lines[0]
    assert '🏠 Забрали за с!' == output_lines[1]


def test_order_deliver():
    """Test order command with delivery flag."""
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'margherita', 'L', '--delivery'])
    assert result.exit_code == 0
    output_lines = remove_digits(result.output).splitlines()
    assert '🍳 Приготовили за с!' == output_lines[0]
    assert '🛵 Доставили за с!' == output_lines[1]


def test_order_wrong_pizza_type():
    """Test order command with wrong pizza type."""
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'wrong', 'L'])
    assert result.exit_code == 2


def test_order_wrong_size():
    """Test order command with wrong size."""
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'margherita', 'M'])
    assert result.exit_code == 2


def test_menu():
    """Test menu command."""
    runner = CliRunner()
    result = runner.invoke(cli, ['menu'])
    assert result.exit_code == 0
    output_lines = remove_digits(result.output).splitlines()
    assert '- Margherita 🧀: tomato sauce, mozzarella, tomatoes' \
        == output_lines[0]
    assert '- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni' \
        == output_lines[1]
    assert '- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapple' \
        == output_lines[2]
