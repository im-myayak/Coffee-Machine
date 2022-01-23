MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def collect_the_information(name):
    """ THis is a function which takes the name of a coffee and return its information"""
    if name == 'cappuccino':
        water = MENU['cappuccino']['ingredients']['water']
        milk = MENU['cappuccino']['ingredients']['milk']
        coffee = MENU['cappuccino']['ingredients']['coffee']
        cost_coffee = MENU['cappuccino']['cost']
        return [water, milk, coffee, cost_coffee]
    elif name == 'espresso':
        water = MENU['espresso']['ingredients']['water']
        milk = MENU['espresso']['ingredients']['milk']
        coffee = MENU['espresso']['ingredients']['coffee']
        cost_coffee = MENU['espresso']['cost']
        return [water, milk, coffee, cost_coffee]
    elif name == 'latte':
        water = MENU['latte']['ingredients']['water']
        milk = MENU['latte']['ingredients']['milk']
        coffee = MENU['latte']['ingredients']['coffee']
        cost_coffee = MENU['latte']['cost']
        return [water, milk, coffee, cost_coffee]
    elif name == 'resources':
        water = resources['water']
        milk = resources['milk']
        coffee = resources['coffee']
        return [water, milk, coffee]
    else:
        return "Error"


def check_money(penny, nickel, dine, quarter, coffee_cost):
    """function takes the type of money entered by user for a coffee and return if money is not sufficient or not """
    sum_of_money = penny*0.01 + nickel*0.05 + dine*0.1 + quarter*0.25
    if sum_of_money > coffee_cost:
        return f"Here is {round(sum_of_money-coffee_cost,2)} in change. "
    elif sum_of_money == coffee_cost:
        return f"There is no change"
    else:
        return False


def check_coffee_sufficient(coffee_name, current_resource_list):
    """ function  takes the name of a coffee and current resources and return if resources are not sufficient or not """
    the_coffee_information = collect_the_information(coffee_name)
    item_list = ['water','milk','coffee']
    for item in range(len(current_resource_list)):

        if current_resource_list[item] < the_coffee_information[item]:
            print(f' {item_list[item]} is not sufficient ')
            return False

    return True


