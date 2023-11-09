import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')

cursor = conn.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS task_database')
cursor.execute('USE task_database')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS recipes(
               id INT PRIMARY KEY AUTO_INCREMENT,
               name VARCHAR(50),
               ingredients TEXT,
               cooking_time INT,
               difficulty VARCHAR(20)           
    )''')
               

def create_recipe(conn, cursor):
    name = input("Enter the name: ")
    cooking_time = int(input("Enter the cooking time in mins: "))
    ingredients = input("Enter the ingredients: ").split()
    difficulty = calc_difficulty(cooking_time, ingredients)
    recipe_ingredients = ", ".join(ingredients)
    sql = 'INSERT INTO recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
    recipe = (name, recipe_ingredients, cooking_time, difficulty)
    
    cursor.execute(sql, recipe)

def delete_recipe(conn, cursor):
    cursor.execute("SELECT * FROM recipes")
    result = cursor.fetchall()
    for row in result:
        print("\n")
        print("ID: " + str(row[0]))
        print("Name: " + str(row[1]))
        print("Cooking Time: " + str(row[3]))
        print("Ingredients: " + str(row[2]))
        print("Difficulty: " + str(row[4]))
    choice = input("Select a recipe by the ID to delete: ")
    cursor.execute("DELETE FROM recipes WHERE id = (%s)", (choice, ))

def search_recipe(conn, cursor):
    all_ingredients = []
    cursor.execute("SELECT ingredients FROM recipes")
    result = cursor.fetchall()
    for ingredients in result:
        for ingredient in ingredients:
            ingredient_split = ingredient.split(", ")
            all_ingredients.extend(ingredient_split)
    all_ingredients = list(dict.fromkeys(all_ingredients))
    all_ingredients_list = list(enumerate(all_ingredients))
    print("\n Ingredients: ")
    print("----------------------")

    for index, tup in enumerate(all_ingredients_list):
        print(str(tup[0] + 1) + ". " + tup[1])

    search_ingredient = int(input("Enter the ingredient number you would like to search: "))
    search_ingredient_index = int(search_ingredient) - 1
    searched_ingredient = all_ingredients_list[search_ingredient_index][1]

    cursor.execute("SELECT * FROM recipes WHERE ingredients LIKE %s", ('%' + searched_ingredient + '%',))
    result = cursor.fetchall()
    for row in result:
        print("\n")
        print("Name: " + str(row[1]))
        print("Cooking Time: " + str(row[3]))
        print("Ingredients: " + str(row[2]))
        print("Difficulty: " + str(row[4]))

def update_recipe(conn, cursor):
    cursor.execute("SELECT * FROM recipes")
    result = cursor.fetchall()
    for row in result:
        print("\n")
        print("ID: " + str(row[0]))
        print("Name: " + str(row[1]))
        print("Cooking Time: " + str(row[3]))
        print("Ingredients: " + str(row[2]))
        print("Difficulty: " + str(row[4]))
    choice = int(input("Select a recipe by the ID: "))
    id = choice

    choice = int(input("Choose the number of what you would like to update: "))
    if choice == 1:
        print(1)
        change = input("What would you like to change the name too: ")
        cursor.execute("UPDATE recipes SET name = %s WHERE id LIKE %s", (str(change), '%' + str(id) + '%'))
        conn.commit
    elif choice == 2:
        print(2)
        change = int(input("What would you like to change the cooking time too: "))
        cursor.execute("UPDATE recipes SET name = %s WHERE id LIKE %s", ('%' + str(change) + '%', '%' + str(id) + '%'))
        conn.commit
    elif choice == 3:
        change = int(input("What would you like to change the ingredients too: "))
        recipe_ingredients = ", ".join(change)
        cursor.execute("UPDATE recipes SET name = %s WHERE id LIKE %s", ('%' + str(recipe_ingredients) + '%', '%' + str(id) + '%'))
        conn.commit

def calc_difficulty(cooking_time, ingredients):
        if int(cooking_time) < 10 and len(ingredients) < 4:
            return 'Easy'
        elif int(cooking_time) < 10 and len(ingredients) >= 4:
            return 'Medium'
        elif int(cooking_time) >= 10 and len(ingredients) < 4:
            return 'Intermediate'
        elif int(cooking_time) >= 10 and len(ingredients) >= 4:
            return 'Hard'

choice = ""

while(choice != "5"):
    print("Main Menu")
    print("==================")
    print("1. Create a recipe!")
    print("2. Search a recipe!")
    print("3. Update a recipe!")
    print("4. Delete a recipe!")
    print("5. Quit")
    choice = input("Pick a choice number: ")


    if choice == "1":
        create_recipe(conn, cursor)
    elif choice == "2":
        search_recipe(conn, cursor)
    elif choice == "3":
        update_recipe(conn, cursor)
    elif choice == "4":
        delete_recipe(conn, cursor)

conn.commit()
conn.close()