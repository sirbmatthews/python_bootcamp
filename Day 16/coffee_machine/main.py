from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money = MoneyMachine()
coffee_menu = Menu()

is_machine_on = True
while is_machine_on:
    choice = input(f'What would you like? ({coffee_menu.get_items()}): ').lower()

    if choice == 'report': 
        coffee_maker.report()
        money.report()
    elif choice == 'off': is_machine_on = False
    else:
        coffee = coffee_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(coffee) and money.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)