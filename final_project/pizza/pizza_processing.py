"""Collection of functions for processing pizza orders."""

import random
from typing import Callable
from functools import wraps
from final_project.pizza.pizza import Pizza


def log(log_format: str = None) -> Callable:
    """Log a function call to the console."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            duration = random.randint(1, 10)
            if log_format:
                print(log_format.format(duration))
            else:
                print(f'{func.__name__} - {duration}c!')
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log('🍳 Приготовили за {}с!')
def bake(pizza: Pizza):
    """Bake a pizza."""


@log('🏠 Забрали за {}с!')
def pickup(pizza: Pizza):
    """Pickup a pizza."""


@log('🛵 Доставили за {}с!')
def deliver(pizza: Pizza):
    """Deliver a pizza."""
