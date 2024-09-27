MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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


def user_selection():
    """Finds out what the user selects and returns it. It also discards the invalid inputs and asks
     the user to guess again."""
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'espresso':
        return 'espresso'
    elif choice == 'latte':
        return 'latte'
    elif choice == 'cappuccino':
        return 'cappuccino'
    elif choice == 'report':
        return 'report'
    elif choice == 'off':
        return 'off'
    else:
        print("Please enter valid inputs!")
        return user_selection()


def resource_checker_message(coffee_menu, coffee_name):
    resources_available = True
    if resources['water'] < coffee_menu['water']:
        print("Sorry there is not enough water.")
        resources_available = False
    if resources['coffee'] < coffee_menu['coffee']:
        print("Sorry there is not enough coffee.")
        resources_available = False
    if 'milk' in coffee_menu:
        if resources['milk'] < coffee_menu['milk']:
            print("Sorry there is not enough milk.")
            resources_available = False
            return
    return resources_available


def insert_coins():
    print("Please insert coins")
    quarters_coins_input = int(input("How many quarters (quarters = $0.25) ?: "))
    dimes_coins_input = int(input("How many dimes (dimes = $0.10) ?: "))
    nickles_coins_input = int(input("How many nickles (nickles = $0.05) ?: "))
    pennies_coins_input = int(input("How many pennies (pennies = $0.01) ?: "))
    total_money_inserted = (quarters_coins_input * 0.25) + (dimes_coins_input * 0.1) + (nickles_coins_input * 0.05) + (pennies_coins_input * 0.01)
    print(f"You inserted ${total_money_inserted}")
    return total_money_inserted


def money_calculation(money_paid, coffee_name):
    coffee_cost = MENU[coffee_name]['cost']
    if money_paid < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_paid == coffee_cost:
        resources['money'] += coffee_cost
    else:
        change_amount = round(money_paid - coffee_cost, 2)
        resources['money'] += coffee_cost
        print(f"Here is ${change_amount} dollars in change.")
    return True


def resource_calculation(coffee_menu, coffee_name, money_calculated):
    if money_calculated:
        resources['water'] -= coffee_menu['water']
        resources['coffee'] -= coffee_menu['coffee']
        if 'milk' in coffee_menu:
            resources['milk'] -= coffee_menu['milk']


def coffee_message(money_calculated, coffee_name):
    if money_calculated:
        print(f"Here is your {coffee_name}. ☕️ Enjoy!")


def resource_checker(user_choice):
    if user_choice == 'espresso':
        espresso_menu = MENU['espresso']['ingredients']
        espresso_available = resource_checker_message(espresso_menu, 'Espresso')
        if espresso_available:
            money_paid = insert_coins()
            money_calculated = money_calculation(money_paid, 'espresso')
            resource_calculation(espresso_menu, 'espresso', money_calculated)

    elif user_choice == 'latte':
        latte_menu = MENU['latte']['ingredients']
        latte_available = resource_checker_message(latte_menu, 'Latte')
        if latte_available:
            money_paid = insert_coins()
            money_calculated = money_calculation(money_paid, 'latte')
            resource_calculation(latte_menu, 'latte', money_calculated)

    elif user_choice == 'cappuccino':
        cappuccino_menu = MENU['cappuccino']['ingredients']
        cappuccino_available = resource_checker_message(cappuccino_menu, 'Espresso')
        if cappuccino_available:
            money_paid = insert_coins()
            money_calculated = money_calculation(money_paid, 'cappuccino')
            resource_calculation(cappuccino_menu, 'cappuccino', money_calculated)


def coffee_machine():
    resources['money'] = 0
    machine_status = True
    while machine_status:
        user_choice = user_selection()
        if user_choice == 'report':
            print(f"""REPORT
        Water: {resources['water']}ml
        Milk: {resources['milk']}ml
        Coffee: {resources['coffee']}g
        Money: ${resources['money']}""")
        elif user_choice == 'off':
            print("Turning off the machine!")
            return
        else:
            resource_checker(user_choice)


coffee_machine()




