from random import randint

art = '''
  .oooooo.                                                 ooooooooooooo oooo                       ooooo      ooo                                .o8                          
 d8P'  `Y8b                                                8'   888   `8 `888                       `888b.     `8'                               "888                          
888           oooo  oooo   .ooooo.   .oooo.o  .oooo.o           888       888 .oo.    .ooooo.        8 `88b.    8  oooo  oooo  ooo. .oo.  .oo.    888oooo.   .ooooo.  oooo d8b 
888           `888  `888  d88' `88b d88(  "8 d88(  "8           888       888P"Y88b  d88' `88b       8   `88b.  8  `888  `888  `888P"Y88bP"Y88b   d88' `88b d88' `88b `888""8P 
888     ooooo  888   888  888ooo888 `"Y88b.  `"Y88b.            888       888   888  888ooo888       8     `88b.8   888   888   888   888   888   888   888 888ooo888  888     
`88.    .88'   888   888  888    .o o.  )88b o.  )88b           888       888   888  888    .o       8       `888   888   888   888   888   888   888   888 888    .o  888     
 `Y8bood8P'    `V88V"V8P' `Y8bod8P' 8""888P' 8""888P'          o888o     o888o o888o `Y8bod8P'      o8o        `8   `V88V"V8P' o888o o888o o888o  `Y8bod8P' `Y8bod8P' d888b 
'''

def set_difficulty():
    '''
        Return difficulty from a user prompt.
    '''
    not_valid = True
    while not_valid:
        try: 
            difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
            if difficulty != 'easy' and difficulty != 'hard': raise
            not_valid = False
        except: 
            print('Invalid input: Try again!')

    if difficulty == 'easy': return 10
    elif difficulty == 'hard': return 5

def user_guess():
    '''
        Return a number from a user prompt.
    '''
    not_valid = True
    while not_valid:
        try: 
            guess = int(input('Make a guess: '))
            if 1 > guess > 100: raise
            not_valid = False
        except: 
            print('Invalid input: Try again with a number between 1 and 100.')
    
    return guess

def check_answer(guess):
    if guess > number: 
        print('Too high.')
        return 0
    elif guess < number: 
        print('Too low.')
        return 0
    else: 
        print(f'You got it! The answer {number}')
        return 1

def number_guess():
    '''
        Play number guess
    '''
    global attempts, number
    for attempt in range(attempts):
        print(f'You have {attempts - attempt} attempts remaining to guess the number')
        guess = user_guess()
        
        answer = check_answer(guess)
        if answer == 1:
            winner = True
            break
        elif attempts - attempt > 1: print('Guess again')
        winner = False
        
    if not winner:
        print('You\'ve run out of guesses. Try again!')       

print(art)
print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100.')
number = randint(1, 100)

attempts = set_difficulty()

number_guess()