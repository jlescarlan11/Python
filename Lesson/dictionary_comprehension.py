"""
dictionary comprehension =  create dictioonaries using an expression
                            can replace for loops and certain lambda functions

dictionary = {key: expression for (key, value) in iterable}
dictionary = {key: expression for (key, value) in iterable if conditional}
dictionary = {key: (if/else) for (key, value) in iterable}
dictionary = {key: function(value) for (key, value) in iterable}
"""

# Dictionary comprehension is a concise way to create dictionaries using expressions.
# It can replace for loops and, in some cases, lambda functions.

# Example 1: Convert temperatures from Fahrenheit to Celsius
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value - 32) * (5 / 9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

# Example 2: Filter cities with sunny weather
weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles': 'sunny', 'Chicago': 'cloudy'}
sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}
print(sunny_weather)

# Example 3: Categorize cities as 'WARM' or 'COLD' based on temperature
cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: ('WARM') if value >= 40 else ('COLD') for (key, value) in cities.items()}
print(desc_cities)

# Example 4: Use a function in the expression for more complex operations
def check_temp(value):
    if value >= 40:
        return 'WARM'
    else:
        return 'COLD'

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities)
