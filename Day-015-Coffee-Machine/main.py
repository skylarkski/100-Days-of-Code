from coffee import MENU
from coffee import resources

money = 0
drinkChoice = ""

print()


def get_drink(drk):
    if drk == "1":
        drk = "espresso"
        return drk
    elif drk == "2":
        drk = "latte"
        return drk
    elif drk == "3":
        drk = "cappuccino"
        return drk
    elif drk == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Water: {resources['coffee']}g")
        print(f"Money: ${money}\n")
        return "none"


def check_resources(drink_resource):

    if drink_resource == "espresso":

        if resources['water'] < MENU[drink_resource]['ingredients']['water']:
            print("Sorry, there is not enough water")
            return False
        elif resources['coffee'] < MENU[drink_resource]['ingredients']['coffee']:
            print("Sorry, there is not enough coffee")
            return False

        return True

    else:
        if resources['water'] < MENU[drink_resource]['ingredients']['water']:
            print("Sorry, there is not enough water")
            return False
        elif resources['milk'] < MENU[drink_resource]['ingredients']['milk']:
            print("Sorry, there is not enough milk")
            return False
        elif resources['coffee'] < MENU[drink_resource]['ingredients']['coffee']:
            print("Sorry, there is not enough coffee")
            return False

        return True

def check_coins(drink_coins):
    print("Please insert coins.")
    quart = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nick = int(input("How many nickles?: "))
    penn = int(input("How many pennies?: "))

    print(quart, dime, nick, penn)

    total = (quart * 0.25) + (dime * 0.10) + (nick * 0.05) + (penn * 0.01)

    print(total)
    change = round(total - MENU[drink_coins]['cost'], 2)

    return change


def update_resources(drink_sold):
    if drink_sold != "espresso":
        resources['water'] = resources['water'] - MENU[drink_sold]['ingredients']['water']
        resources['milk'] = resources['milk'] - MENU[drink_sold]['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - MENU[drink_sold]['ingredients']['coffee']
    else:
        resources['water'] = resources['water'] - MENU[drink_sold]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU[drink_sold]['ingredients']['coffee']

    return resources


while drinkChoice != "off":

    print("What would you like? (espresso/latte/cappuccino): ")
    print("1. espresso")
    print("2. latte")
    print("3. cappuccino")

    drinkChoice = str(input())
    drink = get_drink(drinkChoice)

    if drink == "espresso" or drink == "latte" or drink == "cappuccino":

        if check_resources(drink):
            change_due = check_coins(drink)
            if change_due >= 0:
                print(f"Here is your ${change_due} in change.")
                print(f"Here is your {drink}. Enjoy!")
                money += MENU[drink]['cost']
                resources = update_resources(drink)
            else:
                print("Sorry, that's not enough money. Money refunded.")

