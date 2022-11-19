import datetime
from recipe import Recipe

class BookException(Exception):
    """"Class exception of Recipe's Class"""
    def __init__(self, mesg):
        super().__init__(mesg)

class Book:
    """Class of Book containing Recipes"""
    def __init__(self, name):
        if len(name.strip()) ==0:
            raise BookException("The name of the Book not be empty !")
        self.name = name
        self.creation_date = datetime.datetime.today()
        self.last_update = self.creation_date
        self.recipes_list = {"starter":[], "lunch":[], "dessert":[]}
    
    def add_recipe(self, recipe):
        """add a recipe in the book and update last_update"""
        if type(recipe) is not Recipe:
            raise BookException("recipe must be a Recipe's Object !")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.datetime.today()

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name {name} and returns the instance"""

        if len(name.strip()) > 0:
            for type, recipeList in self.recipes_list.items():
                for recipe in recipeList:
                    if recipe.name == name:
                        print(recipe)
                        return recipe
            print(f"[{name}] not found!")
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""

        return_list = []
        if len(recipe_type.strip()) == 0 or not any(recipe_type in str for str in ['starter','lunch','dessert']):
            print(f"The recipe_type must be 'starter', 'lunch' or 'dessert' \n")
            return None
        else:
            recipeList = self.recipes_list[recipe_type]
            for recipe in recipeList:
                return_list.append(recipe.name)
            return return_list
        

    def __str__(self):
        txt ="\n******* B O O K *******\n"
        txt += "Name : " + self.name + "\n"
        txt += "created : " + str(self.creation_date) + "\n"
        txt += "updated : " + str(self.last_update) + "\n\n"
        for type,recipeList in self.recipes_list.items():
            txt += "=== " + type + " ===\n"
            for recipe in recipeList:
                txt += "\t" + str(recipe) + "\n\n"
        return txt