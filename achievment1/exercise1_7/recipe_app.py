from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String


engine = create_engine("mysql://cf-python:password@localhost/task_database")
Session = sessionmaker(bind=engine)
Base = declarative_base()

session = Session()

class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + "Difficulty: " + self.difficulty + ">"
    def __str__(self):
        return "Recipe Name: " + self.name + "\n" + "Recipe Difficulty: " + self.difficulty + "\n" + "Cooking Time:" + str(self.cooking_time) + "\n" + "Ingredients: " + str(self.ingredients)
    def return_ingredients_as_list(self):
         if self.ingredients == "":
              ingredient_list = []
              return ingredient_list
         else:
              ingredient_list = self.ingredients.split(",")
              return ingredient_list
    def calc_difficulty(self):
        if int(self.cooking_time) < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif int(self.cooking_time) < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif int(self.cooking_time) >= 10 and len(self.ingredients) < 4:
            self.difficulty = "intermediate"
        elif int(self.cooking_time) >= 10 and len(self.ingredients) >= 4:
            self.difficulty = "Hard"

def create_recipe():
    name = input("Enter Recipe Name: ")
    if len(name) < 51:
        print("Name accepted: ")
    else:
        print("That name is too long!")
        
    
    cooking_time = input("Enter the cooking time: ")
    if cooking_time.isnumeric():
        print("Time accepted")
    else:
        print("That cooking time is not only numbers!")
        
    
    count = input("How many ingredients would you like to add: ")
    ingredients_list = []
    i = 0
    while i < int(count):
        i = i + 1
        ingredient = input("Enter the ingredient: ")
        ingredients_list.append(ingredient)
    ingredients = ",".join(ingredients_list)

    recipe = Recipe(
        name = name,
        cooking_time = cooking_time,
        ingredients = ingredients,
        difficulty = ""
    )
    recipe.calc_difficulty()
    session.add(recipe)
    session.commit()

def view_all_recipes():
    recipes_list = session.query(Recipe).all()
    for recipe in recipes_list:
        print("Recipe ID: ", recipe.id)
        print("Recipe Name: ", recipe.name)
        print("Ingredients: ", recipe.ingredients)
        print("Cooking Time: ", recipe.cooking_time)

def search_by_ingredients():
    count = session.query(Recipe).count()
    if count == 0:
        print("There are no entries!")
        return None
    else:
        results = session.query(Recipe.ingredients).all()
        all_ingredients = []

        for ingredients in results:
            for ingredient in ingredients:
                ingredient_split = ingredient.split(",")
                all_ingredients.extend(ingredient_split)
        all_ingredients = list(dict.fromkeys(all_ingredients))
        all_ingredients = list(enumerate(all_ingredients))

        for index, tup in enumerate(all_ingredients):
            print(str(tup[0] + 1) + ". " + tup[1])
        
        choice = int(input("Select the ingredient number you would like to search: "))
        search_ingredient = choice - 1
        result = all_ingredients[search_ingredient][1]
        recipes = session.query(Recipe).filter(Recipe.ingredients.like("%" + result + "%")).all()
        for recipe in recipes:
            print("Recipe ID: ", recipe.id)
            print("Recipe Name: ", recipe.name)
            print("Ingredients: ", recipe.ingredients)
            print("Cooking Time: ", recipe.cooking_time)

def edit_recipe():
    recipes_list = session.query(Recipe).all()
    for recipe in recipes_list:
        print("Recipe ID: ", recipe.id)
        print("Recipe Name: ", recipe.name)
    choice = int(input("Select the id of the recipe you would like to change: "))
    id = choice
    selected_recipe = session.query(Recipe).filter(Recipe.id == id).one()
    print("This is the recipe selected")
    print(selected_recipe)
    print("1. Name")
    print("2. Cooking Time")
    print("3. Ingredients")
    choice = int(input("Select the number of which you would like to edit: "))

    if choice == 1:
        print("hi")
        choice = input("Enter a new name for the recipe: ")
        session.query(Recipe).filter(Recipe.id == id).update({Recipe.name: choice})
        session.commit()
    elif choice == 2:
        choice = input("Enter a new cooking time: ")
        session.query(Recipe).filter(Recipe.id == id).update({Recipe.cooking_time: int(choice)})
        session.commit()
    elif choice == 3:
        count = input("How many ingredients would you like to add: ")
        ingredients_list = []
        i = 0
        while i < int(count):
            i = i + 1
            ingredient = input("Enter the ingredient: ")
            ingredients_list.append(ingredient)
        ingredients = ",".join(ingredients_list)
        session.query(Recipe).filter(Recipe.id == id).update({Recipe.ingredients: ingredients})
        session.commit()
    else:
        print("Not a valid choice")

def delete_recipe():
    recipes_list = session.query(Recipe).all()
    for recipe in recipes_list:
        print("Recipe ID: ", recipe.id)
        print("Recipe Name: ", recipe.name)
    choice = int(input("Select the id of the recipe you would like to delete: "))
    id = choice
    selected_recipe = session.query(Recipe).filter(Recipe.id == id).one()
    print("This is the recipe selected for deletion")
    print(selected_recipe)
    choice = int(input("Select 1 for yes, 2 for no: "))
    if choice == 1:
        print("Choice deleted")
        session.delete(selected_recipe)
        session.commit()
    else:
        print("Choice not deleted")
    

mainchoice = ""

while(mainchoice != "5"):
    print("Main Menu")
    print("==================")
    print("1. Create a recipe!")
    print("2. Search a recipe!")
    print("3. Update a recipe!")
    print("4. Delete a recipe!")
    print("5. Quit")
    mainchoice = input("Pick a choice number: ")


    if mainchoice == "1":
        create_recipe()
    elif mainchoice == "2":
        search_by_ingredients()
    elif mainchoice == "3":
        edit_recipe()
    elif mainchoice == "4":
        delete_recipe()

Base.metadata.create_all(engine)
