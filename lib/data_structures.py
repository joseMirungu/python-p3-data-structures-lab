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
    """Returns a list of names of spicy foods."""
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    """Returns a list of spicy foods with a heat level over 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    """Prints the spicy foods with their cuisine and heat level."""
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Returns the spicy food that matches the given cuisine."""
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None


def print_spiciest_foods(spicy_foods):
    """Prints the spicy foods with a heat level over 5."""
    for food in get_spiciest_foods(spicy_foods):
        heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")


def get_average_heat_level(spicy_foods):
    """Returns the average heat level of the spicy foods."""
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods) if spicy_foods else 0


def create_spicy_food(spicy_foods, new_spicy_food):
    """Adds a new spicy food to the list and returns the updated list."""
    spicy_foods.append(new_spicy_food)
    return spicy_foods
