import sys

class bcolor:
    C_GREEN = "\033[92m"
    C_RED = "\033[91m"
    C_YELLOW = "\033[93m"
    C_CYAN = "\033[94m"
    C_RESET = "\033[0m"

cookbook = {
    'Sandwich': {
        'ingredients': ['ham','bread','cheese','tomatoes'],
        'meal': 'lunch',
        'prep_time': 10,
    },
    'Cake': {
        'ingredients': ['flour','sugar','eggs'],
        'meal': 'dessert',
        'prep_time': 60,
    },
    'Salad': {
        'ingredients': ['avocado','arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15,
    },
}

def ft_input_int(prompt, min = 0, max = 100):
    ok = False
    while not ok:
        try:
            choice = input(prompt)
            ret = int(choice)
            if ret >= min and ret <= max:
                ok = True
            else:
                raise Exception(f"{bcolor.C_RED}Error: The value is not in range ({min}, {max}).{bcolor.C_RESET}") 
        except ValueError:
            print(f"{bcolor.C_RED}Bad value.{bcolor.C_RESET}")
        except Exception as error:
            print(error)

    return ret

def print_recipe(search):
    if search == '':
        print(f'{bcolor.C_RED}Error:{bcolor.C_RESET} empty name.')
    elif search in cookbook:
        recipe = cookbook[search]
        ingredients = recipe['ingredients']
        if len(ingredients) == 0:
            ingredients = "[empty]"
        meal=recipe['meal']
        time=recipe['prep_time']
        print(f"\nRecipe for {bcolor.C_GREEN}{search}{bcolor.C_RESET} :")
        print(f"Ingredients list: {bcolor.C_CYAN}{ingredients}{bcolor.C_RESET}")
        print(f"To be eating for {bcolor.C_CYAN}{meal}{bcolor.C_RESET}.")
        print(f"Takes {bcolor.C_CYAN}{time}{bcolor.C_RESET} minutes of cooking.\n")
    else:
        print(f"{bcolor.C_GREEN}{search}{bcolor.C_RED} does not exist in CookBook.{bcolor.C_RESET}")

def print_cookBook():
    print("\n********************************")
    print("*        C O O K B O O K       *")
    print("********************************")
    print(f"{len(cookbook)} recipe(s)")
    for recipe_name in cookbook:
        print_recipe(recipe_name)
        print("--------------------------------")

def del_recipe(recipe_to_del):
    if recipe_to_del == '':
        print(f'{bcolor.C_RED}Error:{bcolor.C_RESET} empty name.')
    elif recipe_to_del  in cookbook:
        del cookbook[recipe_to_del]
        print(f"\n\t -----------------> {recipe_to_del} {bcolor.C_RED}deleted.{bcolor.C_RESET}")
    else:
        print(f"{bcolor.C_GREEN}{recipe_to_del} {bcolor.C_RED}does not exist in CookBook.{bcolor.C_RESET}")

def add_recipe(name_recipe, ingredients, meal, time):
    if name_recipe == '':
        print(f"{bcolor.C_RED}Error:{bcolor.C_RESET} the recipe cannot have empty name.")
        return
    modif = False
    new_recipe = {}
    new_recipe['ingredients'] = ingredients
    new_recipe['meal'] = meal
    new_recipe['prep_time'] = time
    if name_recipe in cookbook:
        modif = True
    cookbook[name_recipe] = new_recipe
    if modif:
        print(f"\n\t ----------------->{bcolor.C_GREEN} {name_recipe} {bcolor.C_RESET} has just been {bcolor.C_CYAN} modified.{bcolor.C_RESET}")
    else:
        print(f"\n\t ----------------->{bcolor.C_GREEN} {name_recipe} {bcolor.C_RESET}{bcolor.C_YELLOW} has just been added to CookBook.{bcolor.C_RESET}")

def menu():
    print ("Please select an option by typing the corresponding number:")
    print ("1: Add a recipe")
    print ("2: Delete a recipe")
    print ("3: Print a recipe")
    print ("4: Print the Cookbook")
    print ("5: Quit")
    choice = '0'
    while choice not in ['1','2','3','4','5']:
        choice = input(">> ")
        if choice not in ['1','2','3','4','5']:
            print(f"\n{bcolor.C_RED}This option does not exist,{bcolor.C_RESET} please type the corresponding number.")
            print("To exit, enter 5.")
    return choice           

def main():
    choice = '0'
    while choice != '5':
        choice = menu()
        if choice == '1':
            print("Adding a Recipe ...")
            name_recipe = input("\tName of the recipe ? : ")
            ingredients = []
            while 42:
                ingredient = input("\tName of a ingredient (empty to quit) ? : ")
                if ingredient == '':
                    break
                ingredients.append(ingredient)
            meal = input("\tType of meal (lunch, dessert, etc... ? :")
            # prep_time = input ("\tTime to prepare the recipe (in minutes) ? : ")
            prep_time = ft_input_int("\tTime to prepare the recipe (in minutes) ? : ")
            add_recipe(name_recipe, ingredients, meal, prep_time)
        elif choice == '2':
            print("\nPlease enter the recipe's name to delete:")
            to_delete = input(">> ")
            del_recipe(to_delete)
        elif choice == '3':
            print("\nPlease enter the recipe's name to get details:")
            recipe = input (">> ")
            print_recipe(recipe)
        elif choice == '4':
            print_cookBook()
    print("\nCookBook ... closed.\n    By !!")

if __name__ == "__main__":

    main()
    sys.exit(1)