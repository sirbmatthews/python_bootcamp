from random import randint
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
          
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

game_images = [rock, paper, scissors]

def print_game_images(user, computer):
    print(game_images[user])
    print('Computer chose:')
    print(game_images[computer])

def check_winner(user, computer):
    if user == computer:
        print('It\'s a draw')
    elif user == 0 and computer == 2:
        print('You win.')
    elif user == 2 and computer == 0:
        print('You lose.')
    elif user < computer:
        print('You lose.')
    elif user > computer:
        print('You win.')

user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n'))
computer = randint(0, 2)

if user > 2:
    print('You selected an invalid option, you lose')
    exit()
  
print_game_images(user, computer)
check_winner(user, computer)