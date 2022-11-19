class RecipeException(Exception):
    """"Class exception of Recipe's Class"""
    def __init__(self, mesg):
        super().__init__(mesg)

class Recipe:
    """Object Recipe"""

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        """init class Recipe"""
        if len(name.strip()) == 0:
            raise RecipeException("The name must not be empty !")
        try:
            if cooking_lvl != int(cooking_lvl):
                raise RecipeException("["+name+"] :cooking lvl must be an int !")
            cooking_lvl = int(cooking_lvl)
            if cooking_lvl not in range(1,6):
                raise RecipeException("["+name+"] :cooking lvl must be in range from 1 to 5 !")
        except ValueError:
            raise RecipeException("["+name+"] :cooking lvl must be an int !")
        try:
            cooking_time = int(cooking_time)
            if cooking_time < 0:
                raise RecipeException("["+name+"] :cooking time must be positive int !")
        except ValueError:
            raise RecipeException("["+name+"] :cooking level must be an int !")
        if type(ingredients) is not list:
            raise RecipeException("["+name+"] :ingredients must be a list of string !")
        if len(ingredients) == 0:
            raise RecipeException("["+name+"] :The list of ingredients must not be empty !")
        if len(recipe_type.strip()) == 0 or not any(recipe_type in str for str in ['starter','lunch','dessert']):
            raise RecipeException("["+name+"] :The recipe type must be 'starter', 'lunch' or 'dessert' !")
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = str(description)
        self.recipe_type = recipe_type
    
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt = self.name + "\n("
        txt += self.description + ")\n"
        txt += "Level: "+str(self.cooking_lvl) + "\n"
        txt += "Duration: "+str(self.cooking_time) + " minute(s)\n"
        txt += "Type: "+self.recipe_type + "\n"
        txt += "Ingrédients: "+str(self.ingredients)
        return txt
