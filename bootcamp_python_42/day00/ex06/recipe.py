def dictionaries(select_dict):
    if select_dict == 1:
        cookbook = {
                'sandwich': {
                    'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                    'meal': 'lunch', 'prep_time': '10'},
                'cake': {
                    'ingredients': ['flour', 'sugar', 'eggs'],
                    'meal': 'dessert', 'prep_time': '60'},
                'salad': {
                    'ingredients': [
                        'avocado', 'arugula', 'tomatoes', 'spinach'],
                    'meal': 'lunch', 'prep_time': '15'}}
        return cookbook
    elif select_dict == 2:
        menu = {1: 'Add a recipe', 2: 'Delete a recipe', 3: 'Print a recipe',
                4: 'Print the cookbook', 5: 'Cookbook closed.'}
        return menu


def recipe(name, dic=None):
    if dic is None:
        cookbook = dictionaries(1)
    else:
        cookbook = dic
    print(f'\nRecipe for {name}:'
          f'\nIngredients list: {cookbook[name].get("ingredients")}'
          f'\nTo be eaten for {cookbook[name].get("meal")}.'
          f'\nTakes {cookbook[name].get("prep_time")} minutes of cooking.')


def delete_recipe(name):
    del cookbook[name]
    print(f'The recipe {name} has been deleted.')


def new_recipe(name, ingredients, meal, prep_time):
    cookbook = dictionaries(1)
    cookbook[name] = {}
    cookbook[name]['ingredients'] = ingredients
    cookbook[name]['meal'] = meal
    cookbook[name]['prep_time'] = prep_time
    return (cookbook)


def add_recipe():
    name = input(f'Enter the recipe\'s name: ')
    n = input(f'Enter the number of ingredients: ')
    ingredients = []
    for i in range(int(n)):
        i = input(f'Enter the ingredients: ')
        ingredients.append(i)
    meal = input(f'Enter the type of meal: ')
    prep_time = input(f'Enter the preparation time in minutes: ')
    cookbook = new_recipe(name, ingredients, meal, prep_time)
    print(f'\nNew recipe successfully added!')
    recipe(name, cookbook)


def all_recipe(cookbook):
    for recipe in cookbook:
        print(f'Recipe:\t{recipe.upper()}')
        print(f'{recipe.capitalize()}\'s ingredients are ', end='')
        for k, v in cookbook[recipe].items():
            if k is "ingredients":
                for i in v[:-1]:
                    print(i, end=', ')
                print(f'and {v[-1]}. ', end='')
            if k is "meal":
                print(f'It is a {v} ', end='')
            if k is "prep_time":
                print(f'and it takes {v} minutes of preparation.')
        print()


def options(choice):
    option = int(choice)
    if option == 1:
        add_recipe()
    elif option == 2:
        name = input(f'Please enter the recipe\'s name to delete\n')
        delete_recipe(name)
    elif option == 3:
        name = input(f'Please enter the recipe\'s name to get its details:\n')
        cookbook = dictionaries(1)
        recipe(name)
    elif option == 4:
        all_recipe()


def main():
    cookbook = dictionaries(1)
    menu = dictionaries(2)
    choice = input(f'Please select an option '
                   f'by typing the corresponding number:'
                   f'\n1: Add a recipe'
                   f'\n2: Delete a recipe'
                   f'\n3: Print a recipe'
                   f'\n4: Print the cookbook'
                   f'\n5: Quit'
                   f'\n')
    i = 0
    while i == 0:
        if not choice.isdigit() or int(choice) > 5:
            print(f'\nThis option does not exist, '
                  f'please type the corresponding number.'
                  f'\nTo exit, enter 5.')
            choice = input()
        else:
            print(menu[int(choice)])
            i = 1
    options(choice)


if __name__ == '__main__':
    main()
