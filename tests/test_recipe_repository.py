from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

def test_all_returns_list_of_all_recipes(db_connection):
    db_connection.seed("seeds/recipes.sql")
    recipe_rep = RecipeRepository(db_connection)
    assert recipe_rep.all() == [
        Recipe(1,'Lasagna', 120, 4),
        Recipe(2,'Roast Vegtables', 45, 3),
        Recipe(3,'Lamb stew', 120, 5),
        Recipe(4,'Chicken Salad', 15, 3),
        Recipe(5,'Beef Stirfry', 20, 4),
    ]


def test_find_by_name_of_recipe_returns_correct_entry(db_connection):
    db_connection.seed("seeds/recipes.sql")
    recipe_rep = RecipeRepository(db_connection)
    assert recipe_rep.find('Lamb stew') == Recipe(3,'Lamb stew', 120, 5)

def test_find_by_name_not_in_db_returns_none(db_connection):
    db_connection.seed("seeds/recipes.sql")
    recipe_rep = RecipeRepository(db_connection)
    assert recipe_rep.find('Fish and Chips') == None
