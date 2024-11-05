print('Welcome to Python Pizza Deliveries')

size = input('What size pizza do you want? S, M or L: ')
pepperoni = input('Do you want pepperoni on your pizza? Y or N: ')
extra_cheese = input('Do you want extra cheese? Y or N: ')

if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
elif size == 'L':
    bill = 25
else:
    print('You\'ve typed the wrong inputs.')
    exit()

if pepperoni == 'Y' and size == 'S':
    bill += 2
elif pepperoni == 'Y' and (size == 'M' or 'L'):
    bill += 3
elif pepperoni == 'N':
    bill += 0
else:
    print('You\'ve typed the wrong inputs.')
    exit()

if extra_cheese == 'Y':
    bill += 1
elif extra_cheese == 'N':
    bill += 0
else:
    print('You\'ve typed the wrong inputs.')
    exit()

print(f'Your total bill is ${bill}')