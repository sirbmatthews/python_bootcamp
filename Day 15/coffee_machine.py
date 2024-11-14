resources = {
    'Water': 300,
    'Milk': 200,
    'Coffee': 100,
    'Money': 0
}

drinks_menu = {
    'Espresso': {
        'Ingredients': {
            'Water': 50,
            'Coffee': 18
        },
        'Cost': 1.5
    },
    'Latte': {
        'Ingredients': {
            'Water': 200,
            'Milk': 150,
            'Coffee': 24
        },
        'Cost': 2.5
    },
    'Cappuccino': {
        'Ingredients': {
            'Water': 250,
            'Milk': 100,
            'Coffee': 24
        },
        'Cost':3
    }
}

def print_report():
    '''
        Print a Report
    '''
    print(f'Water: {resources['Water']}ml')
    print(f'Milk: {resources['Milk']}ml')
    print(f'Coffee: {resources['Coffee']}g')
    print(f'Money: ${resources['Money']}')

def is_resource_sufficient(option):
    '''
        Return true for sufficient resources and false for insufficient resources
    '''
    drink = drinks_menu[option]['Ingredients']
    insufficient_resources = []
    for resource in drink:
        if resources[resource] < drink[resource]: insufficient_resources.append(resource)

    if insufficient_resources:
        list_of_resources = ', '.join(insufficient_resources)
        print(f'Sorry there is not enough {list_of_resources}.')
        return False
    return True

def get_coin(coin):
    '''
        Return coins inserted
    '''
    correct_option = False
    while not correct_option:
        try:
            coins = int(input(f'How many {coin}?: '))
            correct_option = True
        except: print('Invalid option, please enter whole number: ')
    return coins

def process_coins():
    '''
        Process coins inserted
    '''
    print('Please insert coins.')
    quarters = round(get_coin('quarters') * 0.25, 2)
    dimes = round(get_coin('dimes') * 0.1, 2)
    nickles = round(get_coin('nickles') * 0.05, 2)
    pennies = round(get_coin('pennies') * 0.01, 2)
    
    return quarters + dimes + nickles + pennies
    
def review_transaction(option, total):
    '''
        Return true is transaction is successful and false if there's insufficient funds
    '''
    if total < drinks_menu[option]['Cost']:
        print('Sorry that\'s not enough money. Money refunded.')
        return False
    else:
        resources['Money'] += drinks_menu[option]['Cost']
        change = total - drinks_menu[option]['Cost']
        if change > 0: print(f'Here is ${change} in change.')
        return True

def make_coffee(option):
    '''
        Update the resources by deducting 
    '''
    drink = drinks_menu[option]['Ingredients']
    for resource in drink:
        resources[resource] -= drink[resource]

def user_option():
    '''
        Return user option from prompt
    '''
    correct_option = False
    while not correct_option:
        try:
            option = input('What would you like? (espresso/latte/cappuccino): ').capitalize()
            if option != 'Espresso' and option != 'Latte' and option != 'Cappuccino' and option != 'Report' and option != 'Off': raise
            else: return option
        except: print('Invalid option, try again!')

while True:
    option = user_option()
    if option == 'Off': exit()
    elif option == 'Report': print_report()
    else: 
        if is_resource_sufficient(option):
            total = process_coins()
            transact = review_transaction(option, total)
            if transact: 
                make_coffee(option)
                print(f'Here is your {option}. Enjoy')