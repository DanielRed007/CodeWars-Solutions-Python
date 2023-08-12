def get_order(order = ""):
    menu = [
        "Burger",
        "Fries",
        "Chicken",
        "Pizza",
        "Sandwich",
        "Onionrings",
        "Milkshake",
        "Coke"
    ]

    result = []

    for i in range(len(menu)):
        item = menu[i]

        while item.lower() in order:
            getItem = order.find(item.lower())
            result.append(item)
            order = order[0:getItem] + order[getItem + len(item):]

    return " ".join(result)

get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza")
# "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke");
get_order("pizzachickenfriesburgercokemilkshakefriessandwich")
# "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke");