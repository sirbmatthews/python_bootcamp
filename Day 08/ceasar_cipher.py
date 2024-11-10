import string
from more_itertools import locate

print('''
  ___ __ _  ___  ___  __ _ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|
| (_| (_| |  __/\__ \ (_| | |   
 \___\__,_|\___||___/\__,_|_|   
                                
      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|                          
      ''')

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

def encrypt(message, shift):
    encrypted_message = ''
    for char in list(message):
        if char.islower():
            encrypted_message += lowercase[(int(''.join([str(i) for i in list(locate(lowercase, lambda x: x == char))])) + shift) % len(lowercase)]
        elif char.isupper():
            encrypted_message += uppercase[(int(''.join([str(i) for i in list(locate(uppercase, lambda x: x == char))])) + shift) % len(uppercase)]
        elif char.isdigit():
            encrypted_message += numbers[(int(''.join([str(i) for i in list(locate(numbers, lambda x: x == char))])) + shift) % len(numbers)]
        elif char == ' ':
            encrypted_message += ' '
        elif char.isascii():
            encrypted_message += symbols[(int(''.join([str(i) for i in list(locate(symbols, lambda x: x == char))])) + shift) % len(symbols)]
        
    return encrypted_message
    
def decrypt(message, shift):
    decrypted_message = ''
    for char in list(message):
        if char.islower():
            decrypted_message += lowercase[(int(''.join([str(i) for i in list(locate(lowercase, lambda x: x == char))])) - shift) % len(lowercase)]
        elif char.isupper():
            decrypted_message += uppercase[(int(''.join([str(i) for i in list(locate(uppercase, lambda x: x == char))])) - shift) % len(uppercase)]
        elif char.isdigit():
            decrypted_message += numbers[(int(''.join([str(i) for i in list(locate(numbers, lambda x: x == char))])) - shift) % len(numbers)]
        elif char == ' ':
            decrypted_message += ' '
        elif char.isascii():
            decrypted_message += symbols[(int(''.join([str(i) for i in list(locate(symbols, lambda x: x == char))])) - shift) % len(symbols)]
        
    return decrypted_message


restart = True

while restart:
    cipher = input('Type \'encode\' to encrypt, type \'decode\' to decrypt: \n').lower()
    while cipher != 'encode' and  cipher != 'decode':
        cipher = input('Wrong input!! Type \'encode\' to encrypt, type \'decode\' to decrypt: \n').lower()
    message = input('Type your message: \n')
    shift = int(input('Type the shift number: \n'))

    if cipher == 'encode':
        print(f'Here\'s the encoded message: {encrypt(message, shift)}')
    elif cipher == 'decode':
        print(f'Here\'s the decoded message: {decrypt(message, shift)}')
    else:
        print('you chose a wrong input.')
    
    again  = ''
    while again != 'no' and again != 'yes':
        again = input('Type \'yes\' if  you  want to go again. Otherwise type \'no\': ')
    
    if again == 'no':
        restart = False
        print('Goodbye!')