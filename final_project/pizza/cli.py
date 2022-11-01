"""Command line interface for pizza ordering."""

import click
from final_project.pizza.pizza import Pizza, PIZZA_SIZES
from final_project.pizza.pizza_processing import bake, pickup, deliver

MENU = {}
for child in Pizza.__subclasses__():
    MENU[child.__name__.lower()] = child
PIZZA_TYPES = list(MENU.keys())


@click.group()
def cli():
    """Pizza ordering CLI."""


@cli.command()
@click.option('--delivery', default=False, is_flag=True, help='Deliver pizza.')
@click.argument('pizza_type', nargs=1,
                type=click.Choice(PIZZA_TYPES, case_sensitive=False))
@click.argument('size', nargs=1, type=click.Choice(PIZZA_SIZES))
def order(pizza_type: str, size: str, delivery: bool):
    """Order a pizza."""
    pizza_type = pizza_type.lower()
    pizza = MENU[pizza_type](size)
    bake(pizza)
    if delivery:
        deliver(pizza)
    else:
        pickup(pizza)


@cli.command()
def menu():
    """Show menu."""
    for key, pizza in MENU.items():
        key = key.capitalize()
        components = ', '.join(pizza.components)
        print(f'- {key} {pizza.icon}: {components}')
