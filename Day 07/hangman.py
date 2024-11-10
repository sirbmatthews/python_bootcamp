from wonderwords import RandomWord
from more_itertools import locate
from hangman_art import hangman_logo, graphic

rand = RandomWord()
word = rand.word()

used_letters = [] # List of already guessed letters
life = 0


# Print the logo
print(hangman_logo)
    
def lost_life():
    global life
    life += 1
    print(graphic[life])
    print(f'*************************{life}/6 Lives Left*************************')

def is_winner():
    if word == placeholder:
        print(f'####################--You win--####################')
        print(f'The word is {word}')
        return True
    else:
        return False    

placeholder = ''

for position in range(len(word)):
    placeholder += '_'
    
print(f'Word to  guess: {placeholder}')


while word != placeholder and life != 6:
    
    letter = input('Guess a letter: ').lower()
    
    # Check if user has entered a single alphabet, if not they  should retry
    if not letter.islower() and len(letter) > 1 :
        print('Your guess should be a single alphabet. Try again!')
        continue
    
    # If the user chose the wrong letter deduct a life
    elif letter not in word:
        lost_life()
    
    # If user chose the correct letter update the placeholder
    else:
        indecies = list(locate(word, lambda x: x == letter))
        temp = list(placeholder)
        for index in indecies:
            temp[index] = letter
        placeholder = ''.join(temp)
        
        # If all letters have been guessed end the game
        if is_winner():
            exit()
        
        else:
            print(graphic[life])
            print(f'*************************{life}/6 Lives Left*************************')
    
    print(placeholder)
    used_letters.append(letter)

print('####################--You lose--####################')
print(f'The word is {word}')