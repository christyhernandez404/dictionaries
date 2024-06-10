restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {
    "Soda": 2.50,
    "Coffee": 3,
    "Tea": 2.75
}

restaurant_menu["Main Course"]["Steak"] = 17.99
print(restaurant_menu)

del restaurant_menu["Starters"]['Bruschetta']
print(restaurant_menu)



