# Final project
AAA python course final project.

## Command line interface
You can access cli by running *final_project* module:

```console
$ python -m final_project --help
Usage: python -m final_project [OPTIONS] COMMAND [ARGS]...

  Pizza ordering CLI.

Options:
  --help  Show this message and exit.

Commands:
  menu   Show menu.
  order  Order a pizza.
```

### Menu
You can show menu by running *menu* command:

```console
$ python -m final_project menu
- Margerita 🧀: tomato sauce, mozzarella, tomatoes
- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni
- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapple
```

### Order
You can order a pizza by running *order* command:

```console
$ python -m final_project order [OPTIONS] {Margherita|Pepperoni|Hawaiian} {L|XL}
```

Options:
* *--delivery* - deliver pizza. By default pizza is for self-service.

For example:

```console
$ python -m final_project order Margherita L
🍳 Приготовили за 5с!
🏠 Забрали за 6с!

$ python -m final_project order Margherita L --delivery
🍳 Приготовили за 5с!
🛵 Доставили за 10с!
```

## Adding new recepies
To add new recepies you just need to add new class to *final_project/pizza/pizza.py*.

For example:

```python
class MeatLovers(Pizza):
    """MeatLovers pizza recipe."""
    icon = '🍖'
    components = ['tomato sauce', 'mozzarella', 'pepperoni', 'chicken',
                  'sausage']

```


## Tests
To start tests run following command:
```console
$ coverage run -m pytest -v
```
To create html coverage report:
```console
$ coverage html
```
Tests coverage is 100%.
