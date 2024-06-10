cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}


def print_recipes(cookbook):
    print("Recipe names:")
    for name in cookbook.keys():
        print(name)


def print_details(cookbook, name):
    if name in cookbook:
        print(f"Details of {name}:")
        for key, value in cookbook[name].items():
            print(f"{key}: {value}")
    else:
        print(f"Recipe '{name}' is not in cookbook.")


def delete_recipe(cookbook, name):
    if name in cookbook:
        del cookbook[name]
        print(f"Recipe '{name}' deleted successfully.")
    else:
        print(f"Recipe '{name}' is not in cookbook.")


def add_recipe(cookbook):
    name = input("Enter a name: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(',')
    meal = input("Enter a meal type: ")
    prep_time = int(input("Enter preparation time: "))

    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }
    print(f"Recipe '{name}' added successfully.")


def main():
    print("Welcome to the Python Cookbook!")

    while True:
        print("\nList of available options:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit\n")

        choice = input("Please select an option: ")

        if choice == "1":
            add_recipe(cookbook)
        elif choice == "2":
            recipe_name = input("Please enter a recipe name to delete: ")
            delete_recipe(cookbook, recipe_name)
        elif choice == "3":
            recipe_name = input("Please enter a recipe name to print its details: ")
            print_details(cookbook, recipe_name)
        elif choice == "4":
            print_recipes(cookbook)
        elif choice == "5":
            print("Cookbook closed. Goodbye!")
            break
        else:
            print("Sorry, this option does not exist.")


if __name__ == "__main__":
    main()
