from string import ascii_letters, digits, punctuation
from random import choice, shuffle

print('Welcome to the PyPassowrd Generator')

letters = int(input('How many letters would you like in your password_list?\n'))
symbols = int(input('How many symbols would you like?\n'))
numbers = int(input('How many numbers would you like?\n'))

password_list = []

for letter in range(letters):
    password_list.append(choice(ascii_letters))
    
for symbol in range(symbols):
    password_list.append(choice(punctuation))
    
for number in range(numbers):
    password_list.append(choice(digits))

shuffle(password_list)
password = ''.join(str(passwrd) for passwrd in password_list)
print(f'Your password_list is {password}')