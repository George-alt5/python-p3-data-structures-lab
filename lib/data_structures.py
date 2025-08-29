spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

def get_names(foods):
    """Return a list of names from spicy_foods."""
    return [food["name"] for food in foods]

def get_spiciest_foods(foods):
    """Return foods with heat_level > 5."""
    return [food for food in foods if food["heat_level"] > 5]

def print_spicy_foods(foods):
    """Print each food as: Name (Cuisine) | Heat Level: 🌶*level"""
    for food in foods:
        chilis = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {chilis}')

def get_spicy_food_by_cuisine(foods, cuisine):
    """Return the first food dict matching the given cuisine."""
    return next((food for food in foods if food["cuisine"] == cuisine), None)

def print_spiciest_foods(foods):
    """Print only foods with heat_level > 5, formatted like print_spicy_foods."""
    for food in get_spiciest_foods(foods):
        chilis = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {chilis}')

def get_average_heat_level(foods):
    """Return average heat level as integer (floor)."""
    if not foods:
        return 0
    total = sum(food["heat_level"] for food in foods)
    return total // len(foods)

def create_spicy_food(foods, new_food):
    """Append a new spicy food dict and return the updated list."""
    foods.append(new_food)
    return foods
