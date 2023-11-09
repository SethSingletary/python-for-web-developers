recipe_list = []
ingredients_list = []

def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = input("Enter the cooking time of the recipe: ")
    ingredients = input("Enter the ingredients: ").split()
    ingredients.sort()
    recipe = {'name': name, "cooking_time": cooking_time, 'ingredients': ingredients}
    return recipe

number_recipes = input("How many recipes would you like to enter?: ")
num = int(number_recipes)
n = 0
while n < num:
    n = n + 1
    recipe = take_recipe()
    for i in (recipe.get('ingredients')):
        if i in ingredients_list:
            continue
        else:
            ingredients_list.append(i)
    recipe_list.append(recipe)

for x in recipe_list:
    if int(x.get('cooking_time')) < 10 and len(x.get('ingredients')) < 4:
        x['difficulty'] = 'Easy'
    elif int(x.get('cooking_time')) < 10 and len(x.get('ingredients')) >= 4:
        x['difficulty'] = 'Medium'
    elif int(x.get('cooking_time')) >= 10 and len(x.get('ingredients')) < 4:
        x['difficulty'] = 'Intermediate'
    elif int(x.get('cooking_time')) >= 10 and len(x.get('ingredients')) >= 4:
        x['difficulty'] = 'Hard'

for x in recipe_list:
    print("Recipe: " + x.get('name'))
    print("Cooking Time (min):" + x.get('cooking_time'))
    print("Ingredients: ")
    for i in x.get('ingredients'):
        print(str(i) + " ", end="")
    print('')
    print("Difficulty: " + x.get('difficulty'))
print('')
print("Ingredients avaliable across all recipes")
print("----------------------------------------")

ingredients_list.sort()
for i in ingredients_list:
    print(str(i) + " ", end="")