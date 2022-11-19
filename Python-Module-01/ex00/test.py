from recipe import Recipe, RecipeException
from book import Book
try:
    sandwich = Recipe("Sandwich Jambon Beurre",1,3,["Pain","Beurre","Jambon"],"The Sandwich of the Sandwich","lunch")
    burger = Recipe("Burger", 3, 25, ["Pain","Steak","Tomatoes","cheese","burger sauce"],"","lunch")
    tarte = Recipe("Tarte aux fraises", 4, 30, ["Farine", "oeufs", "lait","fraises"],"Tarte de Mamie", "dessert")
    souffle = Recipe("Soufflé au fromage", 5, 25, ["farine","fromage rapé", "oeufs", "crème fraiche"], "Pas Facile !", "starter")
    
    livre = Book("Mes recettes")
    livre.add_recipe(sandwich)
    livre.add_recipe(tarte)
    livre.add_recipe(burger)
    livre.add_recipe(souffle)

    print(f"{livre}")
    
    recette_recherchee = "Tarte aux fraises"
    print(f"get_recipe_by_name('{recette_recherchee}')\n")
    recherche = livre.get_recipe_by_name(recette_recherchee)
    if recherche:
        print(f"\nI found {recherche.name} ({recherche.description})\n")

    type_recherche = "lunch"
    print(f"get_recipes_by_types('{type_recherche}'):\n")
    print(f"=>{livre.get_recipes_by_types(type_recherche)}")

except RecipeException as e:
    print(e)

