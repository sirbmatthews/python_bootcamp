# Check if a customer's height is greater than 120cm and if they're over 18 or below
print('Welcome to the rollercoaster!')

height = int(input('What is your height in cm? '))
bill = 0

if height >= 120:
    print('You can ride the rollercoaster.')
    age = int(input('What is your age? '))
    if  45 <= age <= 55: 
        print('Have a free ride on us.')
    elif age > 18:
        print('Adult tickets are $12')
        bill += 12
    elif 12 < age <= 18:
        print('Youth tickets are $7')
        bill += 7
    else:
        print('Child tickets are $5')
        bill += 5

    take_picture = input('Do you want a picture taken? Please type y for Yes or n for No ')
    if take_picture == 'y':
        bill += 3
        print(f'Your total bill is ${bill}')
    else:
        print(f'Your total bill is ${bill}')
else:
    print('Sorry you have to grow taller before you can ride the rollercoaster.')