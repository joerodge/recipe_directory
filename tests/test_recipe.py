from lib.recipe import Recipe

def test_recipe_object_created_correctly():
    recipe = Recipe(1, 'test recipe', 30, 4)
    assert recipe.id == 1
    assert recipe.name == 'test recipe'
    assert recipe.cooking_time == 30
    assert recipe.rating == 4

def test_equal_behaviour():
    recipe1 = Recipe(1, 'test recipe', 30, 4)
    recipe2 = Recipe(1, 'test recipe', 30, 4)
    assert recipe1 == recipe2

def test_repr():
    recipe = Recipe(1, 'test recipe', 30, 4)
    assert str(recipe) == "Recipe(1, test recipe, 30, 4)"