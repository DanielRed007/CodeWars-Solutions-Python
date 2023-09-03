import math

def cakes(recipe={}, available={}):
    avail = available.copy()
    totals = []

    not_ingredients = []

    for ingredient in avail:
        if ingredient not in recipe:
            not_ingredients.append(ingredient)

    for key in not_ingredients:
        del avail[key]

    for ingredient in recipe:
        if ingredient not in avail:
            return 0
    
    for ingredient in avail:
        total = math.floor(avail[ingredient] / recipe[ingredient])
        totals.append(total)

    return min(totals)

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

cakes(recipe, available)