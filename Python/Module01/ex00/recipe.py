class Recipe:
    # constructor
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = self.checkLevel(cooking_lvl)
        self.cooking_time = self.checkTime(cooking_time)
        self.ingredients = self.checkIngredients(ingredients)
        self.description = description
        self.recipe_type = self.checkType(recipe_type)


    def checkLevel(self, cooking_lvl):
        if not isinstance(cooking_lvl, int) or not (1 <= cooking_lvl <= 5):
            raise ValueError("The level must be an integer between 1 and 5.")
        return cooking_lvl
    

    def checkTime(self, cooking_time):
        if not isinstance(cooking_time, int) or cooking_time < 0:
            raise ValueError("Cooking time must be a non-negative integer.")
        return cooking_time
    

    def checkIngredients(self, ingredients):
        if not isinstance(ingredients, list):
            raise ValueError("Ingredients must be a list of strings.")
        for i in ingredients:
            if not isinstance(i, str):
                raise ValueError("Ingredients must be a list of strings.")
        return ingredients
    

    def checkType(self, recipe_type):
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError('Course must be either "starter", "lunch", or "dessert".')
        return recipe_type
    

    def __str__(self):
        txt = "Recipe: "
        for i in range(len(self.ingredients)):
            if i < len(self.ingredients) - 1:
                txt += self.ingredients[i] + ", "
            else:
                txt += self.ingredients[i]
        return txt
    

# padthai = Recipe("padthai", 2, 25, ["noodle", "shrimp", "tofu"], "", "lunch")
# to_print = str(padthai)
# print(to_print)
