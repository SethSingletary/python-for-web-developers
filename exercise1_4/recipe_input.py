import pickle

def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = input("Enter the cooking time of the recipe: ")
    ingredients = input("Enter the ingredients: ").split()
    ingredients.sort()
    difficulty = calc_difficulty(cooking_time, ingredients)
    recipe = {'name': name, "cooking_time": cooking_time, 'ingredients': ingredients, 'difficulty': difficulty}
    return recipe


def calc_difficulty(cooking_time, ingredients):
    if int(cooking_time) < 10 and len(ingredients) < 4:
        return 'Easy'
    elif int(cooking_time) < 10 and len(ingredients) >= 4:
        return 'Medium'
    elif int(cooking_time) >= 10 and len(ingredients) < 4:
        return 'Intermediate'
    elif int(cooking_time) >= 10 and len(ingredients) >= 4:
        return 'Hard'

filename = input('Enter the path for your recipe file: ')
recipe_list = []
ingredient_list = []

try:
    with open(filename, 'rb') as recipe_file:
        data = pickle.load(recipe_file)
        recipe_list = data['recipe_list']
        ingredient_list = data['ingredient_list']

except FileNotFoundError:
    with open(filename, 'wb') as recipe_file:
        print('file not found')
        data = {"recipe_list": [], "ingredient_list": []}
        pickle.dump(data, recipe_file)
except:
    with open(filename, 'wb') as recipe_file:
        data = {"recipe_list": {}, "ingredient_list": []}
        pickle.dump(data, recipe_file)
finally: 
    recipe_list = data.get('recipe_list')
    ingredient_list = data.get('ingredient_list')

number_recipes = input("How many recipes would you like to enter?: ")
num = int(number_recipes)
n = 0
while n < num:
    n = n + 1
    recipe = take_recipe()
    for i in (recipe.get('ingredients')):
        if i in ingredient_list:
            continue
        else:
            ingredient_list.append(i)
    recipe_list.append(recipe)
    

data = {"recipe_list": recipe_list, "ingredient_list": ingredient_list}
with open(filename, 'wb') as recipe_file:
    pickle.dump(data, recipe_file)