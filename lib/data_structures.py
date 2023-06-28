spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_names=[]
    for food in spicy_foods:
        spicy_names.append(food['name'])
    return spicy_names

def get_spiciest_foods(spicy_foods):
    new_list=[]
    for food in spicy_foods:
        if food['heat_level']>=5:
            new_list.append(food)
    return new_list
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine==food['cuisine']:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods= get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        heat_level = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    num_foods = len(spicy_foods)
    if num_foods == 0:
        return 0
    for food in spicy_foods:
        total_heat_level += food['heat_level']

    average = total_heat_level / num_foods
    return int(average)

def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods