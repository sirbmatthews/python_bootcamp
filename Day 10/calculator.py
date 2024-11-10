from os import system

art = '''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''

def add(num1, num2):
    '''
        Takes to numbers, adds num1 and num2 together and returns the sum. 
    '''
    return num1 + num2

def subtract(num1, num2):
    '''
        Takes to numbers, subtracts num2 from num1 and returns the minuend.
    '''
    return num1 - num2

def divide(num1, num2):
    '''
        Takes to numbers, divides num1 by num2 and returns the quotient. 
    '''
    return num1 / num2

def multiply(num1, num2):
    '''
        Takes to numbers, multiplies num1 with num2 and returns the product. 
    '''
    return num1 * num2

# Request number
def get_number(position):
    '''
        Prompts a user for a number and returns the value.
    '''
    got_number = False
    while not got_number:
        try:
            num = float(input(f'What is the {position} number?: '))
            got_number = True
        except:
            print('Invalid input: Please enter a number!')
            pass
    return num

# Request operator
def get_operator():
    '''
        Prompts a user for an mathemaical operation and returns the operator.
    '''
    for operator in operations:
        print(operator)    
    
    got_operator = False
    while not got_operator:
        try:
            operator = input('Pick an operation: ')
            if operator not in operations:
                raise
            else:
                got_operator = True
        except:
            print('Invalid input: Please enter \'+\' for addition, \'-\' for subtraction, \'/\' for division or \'*\' for multiplication.')
            pass
    return operator

# Prompt user if they want to perform more calculations with the answer or not, or if they're done  
def should_accumulate(answer):
    '''
        Prompts the user if they want to continue calculating usign the previous answer or start a new calculation, or if they want to exit the calculator.
    '''
    accumulate = ''
    while accumulate != 'y' and accumulate != 'n':
        try:
            accumulate = input(f'Type \'y\' to continue calculating with {answer}, \'n\' to start a new calculation or \'d\' if you are done: ')
            if accumulate != 'y' and accumulate != 'n' and accumulate != 'd': 
                raise
        except:
            print('Invalid option, please try again.') 
        if accumulate == 'd': 
            print('Shutting down!')
            exit()
    
    if accumulate == 'y': return True
    else: return False

operations = {
    '+': add, 
    '-': subtract,
    '/': divide,
    '*': multiply
}

def calculator():
    accumulate = True
    system('clear')
    print(art)
    num1 = get_number('first')
    
    # sort outwhen answer is being used 
    while accumulate:
        
        operator = get_operator()
        num2 = get_number('second')

        answer = operations[operator](num1, num2)
        print(f'{num1} {operator} {num2} = {answer}')
        
        accumulate = should_accumulate(answer)
        if accumulate:
            num1 = answer
        else:
            calculator()

print(art) 
calculator()