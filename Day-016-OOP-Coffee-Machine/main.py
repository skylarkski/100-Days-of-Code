from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinkChoice = ""
isOn = True

maker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

while isOn:

    print(f"What would you like? {menu.get_items()}: ")

    drinkChoice = str(input())

    if drinkChoice == "report":
        maker.report()
        money.report()
    elif drinkChoice == "off":
        isOn = False
    else:
        coffee = menu.find_drink(drinkChoice)
        if maker.is_resource_sufficient(coffee):
            if money.make_payment(coffee.cost):
                maker.make_coffee(coffee)
