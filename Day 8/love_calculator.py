'''
Love Calculator

Take two people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number and print it out. 

'''

def calculate_love_score(name1, name2):
    name = (name1 + name2).upper()
    
    true_score = name.count('T') + name.count('R') + name.count('U') + name.count('E')
    love_score = name.count('L') + name.count('O') + name.count('V') + name.count('E')

    print(str(true_score) + str(love_score))

print('Welcome to the Love Calculator.')
name1 = input('Enter the first name: ')
name2 = input('Enter the second name: ')

calculate_love_score(name1, name2)