from math import ceil

def is_prime(num):
    '''
        Returns true for a prime number and false for a non-prime number
    '''
    if num > 1:
        for i in range(2, (num//2)+1):
            if num % i == 0:
                return False  
        else: return True
    else: return False

def get_number():
    '''
        Return a number from a user prompt.
    '''
    not_valid = True
    while not_valid:
        try: 
            num = int(input('Enter a number you want to check if it is a prime number: '))
            not_valid = False
        except: 
            print('Invalid input: try again.')
    
    return num

print(is_prime(get_number()))