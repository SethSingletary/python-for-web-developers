class recipe(object):
    all_ingredients = []
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = ""
    
    def set_name(self):
        self.name = input("Enter the recipe name: ")
    def get_name(self):
        return self.name
    
    def set_cooking_time(self, time):
        self.cooking_time = time
        recipe.calculate_difficulty(self, self.ingredients, self.cooking_time)
    def get_cooking_time(self):
        return self.cooking_time
    
    def add_ingredients(self, *ingredients):
        for ingredient in ingredients:
            self.ingredients.append(ingredient)
            recipe.update_all_ingredients(self)
    def get_ingredients(self):
        return self.ingredients
    def search_ingredients(self, ingredient):
        if ingredient in self.ingredients:
            return True
        else:
            return False
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient in recipe.all_ingredients:
                continue
            else:
                recipe.all_ingredients.append(ingredient)
        
    def get_difficulty(self):
        self.difficulty = recipe.calculate_difficulty(self, self.ingredients, self.cooking_time)
        return self.difficulty
    def calculate_difficulty(self, ingredients, cooking_time):
        if int(cooking_time) < 10 and len(ingredients) < 4:
            self.difficulty = 'Easy'
        elif int(cooking_time) < 10 and len(ingredients) >= 4:
            self.difficulty = 'Medium'
        elif int(cooking_time) >= 10 and len(ingredients) < 4:
            self.difficulty = 'Intermediate'
        elif int(cooking_time) >= 10 and len(ingredients) >= 4:
            self.difficulty = 'Hard'
    
    def __str__(self):
        output = \
            "\nName: " + self.name + \
            "\nCooking Time: " + str(self.cooking_time) + \
            "\nIngredients: " + str(self.ingredients) + \
            "\nDifficulty: " + self.difficulty
        return output

def recipe_search(data, search_term):
    for recipe in data:
        if recipe.search_ingredients(search_term):
            print(recipe)

tea = recipe('Tea')
tea.add_ingredients('Tea Leaves', 'Sugar', 'Water')
tea.set_cooking_time(5)
#print(tea)

cake = recipe('Cake')
tea.add_ingredients('Sugar', 'Butter', 'Eggs', 'Vanilla Essence', 'Flour', 'Baking Powder', 'Milk')
tea.set_cooking_time(50)
#print(cake)

coffee = recipe('Coffee')
coffee.add_ingredients('Coffee Powder', 'Sugar', 'Water')
coffee.set_cooking_time(5)
#print(coffee)

bananaSmoothie = recipe('Banana Smoothie')
bananaSmoothie.add_ingredients('Bananas', 'Milk', 'Peanut Butter', 'Sugar', 'Ice Cubes')
bananaSmoothie.set_cooking_time(5)
#print(bananaSmoothie)

recipes_list = [tea, cake, coffee, bananaSmoothie]
recipe_search(recipes_list, 'Water')
recipe_search(recipes_list, 'Sugar')
recipe_search(recipes_list, 'Bananas')

