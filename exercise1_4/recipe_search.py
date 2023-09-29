import pickle

def display_recipe(data):
    print(data.get('name'))
    print(data.get('difficulty'))
    print(data.get('cooking_time'))
    print(data.get('ingredients'))

def search_ingredient(data):
    all_ingredients = enumerate(data['ingredient_list'])
    numbered_list = list(all_ingredients)
    print("Ingredients List:")

    for i in numbered_list:
        print(i[0], i[1])
    try:
        choice = int(input("Enter a number for the ingredient you would like to search: "))
        ingredient_searched = numbered_list[choice][1]
        print("Searching")
    except ValueError:
        print("Only numbers are allowed")
    except:
        print("Oops! Your input isn't an ingredient")
    else:
        for i in data["recipe_list"]:
            if ingredient_searched in i["ingredients"]:
                print(i)




filename = input('Enter the path for your recipe file: ')

try:
    with open(filename, 'rb') as recipe_file:
        data = pickle.load(recipe_file)
except:
    print("There was an error opening your file!")
else:
    search_ingredient(data)