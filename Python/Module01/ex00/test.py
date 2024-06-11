from datetime import datetime
from book import Book
from recipe import Recipe

try:
    my_book = Book(
        name="My Recipe Book",
        creation_date=datetime.now(),
        last_update=datetime.now(),
        recipes_list={"starter": [], "lunch": [], "dessert": []}
    )
    
    # Adding some recipes for demonstration
    salad = Recipe(
        name="Salad",
        cooking_lvl=1,
        cooking_time=10,
        ingredients=["lettuce", "tomato", "cucumber"],
        description="A healthy salad recipe.",
        recipe_type="starter"
    )
    my_book.add_recipe(salad)
    
    burger = Recipe(
        name="Burger",
        cooking_lvl=4,
        cooking_time=20,
        ingredients=["bun", "beef patty", "cheddar"],
        description="A nice cheatmeal.",
        recipe_type="lunch"
    )
    my_book.add_recipe(burger)

    pancake = Recipe(
        name="Pancakes",
        cooking_lvl=2,
        cooking_time=20,
        ingredients=["flour", "milk", "eggs", "sugar"],
        description="A simple pancake recipe.",
        recipe_type="dessert"
    )
    my_book.add_recipe(pancake)


    # Test get_recipe_by_name
    print("Testing get_recipe_by_name:")
    my_book.get_recipe_by_name("Burger")
    my_book.get_recipe_by_name("Pancakes")
    my_book.get_recipe_by_name("Pizza")

    # Test get_recipes_by_types
    print("\nTesting get_recipes_by_types:")
    print(my_book.get_recipes_by_types("dessert"))
    print(my_book.get_recipes_by_types("lunch"))
    print(my_book.get_recipes_by_types("starter"))

except ValueError as e:
    print(e)
