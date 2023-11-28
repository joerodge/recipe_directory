from lib.database_connection import DatabaseConnection
from lib.recipe_repository import RecipeRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/recipes.sql")

# Retrieve all recipes
recipe_repository = RecipeRepository(connection)
for recipe in recipe_repository.all():
    print(f"{recipe.name} - Cooking time: {recipe.cooking_time} mins, Rating: {recipe.rating}/5")



