from random import choice
from game_data import data
from os import system

higher_lower_art = '''
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/
'''

vs_art = '''
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
'''

correct_answer = True
account_a = choice(data)
account_b = {}
score = -1

def choose_account():
    '''
        Returns account and ensures it's a diffent account compared to account A
    '''
    account_b = choice(data)
    while account_a == account_b:
        account_b = choice(data)
    return account_b

def user_choice():
    '''
        Return a user prompted answer between A and B
    '''
    correct_option = False
    while not correct_option:
        try:
            option = input('WHo has more followers? Type \'A\' or \'B\': ').upper()
            if option != 'A' and option != 'B': raise
            else: return option
        except:
            print('Invalid option, try again!')
          
def check_answer(option):
    '''
        Return true if the answer is correct and false if incorrect
    '''
    if account_a['follower_count'] > account_b['follower_count'] and option == 'A': return True
    elif account_b['follower_count'] > account_a['follower_count'] and option == 'B': return True
    else: return False
    

while correct_answer:
    score += 1
    account_b = choose_account()
    system('clear')
    print(higher_lower_art)
    if score > 0: print(f'You\'re right! Current score: {score}')
    print(f'Compare A: {account_a['name']}, a {account_a['description']} from {account_a['country']}')
    print(vs_art)
    print(f'Agains B: {account_b['name']}, a {account_b['description']} from {account_b['country']}')
    option = user_choice()
    correct_answer = check_answer(option)
    account_a = account_b

system('clear')
print(higher_lower_art)
print(f'Sorry, that\'s wrong. Final score: {score}')