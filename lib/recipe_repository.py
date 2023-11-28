from lib.recipe import Recipe

class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM recipes")
        recipes = []
        for row in rows:
            recipes.append(Recipe(row['id'], row['name'], row['cooking_time'], row['rating']))
        return recipes

    def find(self, name):
        rows = self._connection.execute(
            "SELECT * FROM recipes WHERE name=%s", [name]
            )
        if rows:
            row = rows[0]
            return Recipe(row['id'], row['name'], row['cooking_time'], row['rating'])
        
        