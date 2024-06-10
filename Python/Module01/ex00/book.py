from datetime import datetime
from recipe import Recipe
class Book:

    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name
        self.creation_date = self.checkCreation(creation_date)
        self.last_update = self.creation_date
        self.recipes_list = self.checkRecipes(recipes_list)

    
    def checkCreation(self, creation_date):
        if not isinstance(creation_date, datetime):
            raise ValueError("Creation date must be a datetime object.")
        return creation_date
    

    def checkRecipes(self, recipes_list):
        if not isinstance(recipes_list, dict):
            raise ValueError("Recipes must be a dictionary with keys 'starter', 'lunch', and 'dessert'.")
        if len(recipes_list) != 3:
            raise ValueError("Recipes must have exactly: 'starter', 'lunch', 'dessert'")
        for key in recipes_list:
            if key not in ["starter", "lunch", "dessert"]:
                raise ValueError("Recipes must have exactly: 'starter', 'lunch', 'dessert'")
            if not isinstance(recipes_list[key], list):
                raise ValueError(f"recipes_list['{key}'] must be a list.")
        return recipes_list
    

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for recipe_type, recipes in self.recipes_list.items():
            for recipe in recipes:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print(f"No recipe found with the name '{name}'.")
        return None



    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("Invalid recipe type. Must be one of 'starter', 'lunch', or 'dessert'.")
        recipes = self.recipes_list.get(recipe_type, [])
        return [recipe.name for recipe in recipes]


    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise ValueError("The recipe must be an instance of the Recipe class.")
        if recipe.recipe_type not in self.recipes_list:
            raise ValueError(f"Invalid recipe type: {recipe.recipe_type}. Must be one of starter/lunch/dessert.")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()