"""Pizza recipes."""

from enum import Enum
from typing import List


class Size(Enum):
    L = 1
    XL = 2


class Pizza:
    """Pizza recipe superclass."""

    icon = '🍕'
    components: List[str] = []

    def __init__(self, size: Size):
        self.size = size

    @classmethod
    def dict(cls) -> dict:
        """Return a dictionary representation of the pizza."""
        return {cls.__name__: cls.components}

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pizza):
            return NotImplemented
        return self.size == other.size and self.components == other.components


class Margherita(Pizza):
    """Margherita pizza recipe."""
    icon = '🧀'
    components = ['tomato sauce', 'mozzarella', 'tomatoes']


class Pepperoni(Pizza):
    """Pepperoni pizza recipe."""
    icon = '🍕'
    components = ['tomato sauce', 'mozzarella', 'pepperoni']


class Hawaiian(Pizza):
    """Hawaiian pizza recipe."""
    icon = '🍍'
    components = ['tomato sauce', 'mozzarella', 'chicken', 'pineapple']
