"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)
from sets_categories_data import ALCOHOLS
from sets_categories_data import VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE
from sets_categories_data import SPECIAL_INGREDIENTS
from sets_categories_data import example_dishes, EXAMPLE_INTERSECTION


def clean_ingredients(dish_name, dish_ingredients):
    set_ingredinents = set(dish_ingredients)
    return (dish_name,set_ingredinents)
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    pass


def check_drinks(drink_name, drink_ingredients):
    if ALCOHOLS.isdisjoint(drink_ingredients):
        drink_name += " Mocktail"
    else:
        drink_name += " Cocktail"
    return drink_name
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """

    pass

#task 3
def categorize_dish(dish_name, dish_ingredients):
    categories = {'VEGAN': VEGAN, 
        'VEGETARIAN': VEGETARIAN,
        'PALEO': PALEO,
        'KETO': KETO,
        'OMNIVORE': OMNIVORE}
    for category_name , category_ingredients in categories.items():
        if set(dish_ingredients).issubset(category_ingredients):
             return f'{dish_name}: {category_name}'
           
        
        

    

    
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: set - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """

    pass


def tag_special_ingredients(dish):
    return (dish[0], SPECIAL_INGREDIENTS.intersection(dish[1]))
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """

    pass


def compile_ingredients(dishes):
    compiled = set()
    for dish in dishes:
        compiled |= dish
    return compiled
     
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """

    pass


def separate_appetizers(dishes, appetizers):
    dishes_set = set( dishes )
    result= dishes_set.difference(appetizers)
    return list(result)
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    pass


def singleton_ingredients(dishes, intersection):
    single = set()
    for dish in dishes:
        single |= (dish.difference(intersection))
    return single
   
    """Determine which `dishes` have a singleton ingredi ent (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """

    pass
