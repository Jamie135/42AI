from datetime import datetime
from book import Book
from recipe import Recipe

# Create a new book
my_book = Book(
    name="My Recipe Book",
    last_update=datetime.now(),
    creation_date=datetime.now(),
    recipes_list={"starter": [], "lunch": [], "dessert": []}
)

# Create a recipe
my_recipe = Recipe(
    name="Pancakes",
    cooking_lvl=2,
    cooking_time=20,
    ingredients=["flour", "milk", "eggs", "sugar"],
    description="A simple pancake recipe.",
    recipe_type="dessert"
)

# Add the recipe to the book
my_book.add_recipe(my_recipe)

# Print the book to verify the recipe is added
print(my_book)
