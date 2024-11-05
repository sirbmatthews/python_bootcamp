# Check if a number is odd or even

check_number = int(input('What is the number you want to check?\n'))

if check_number % 2 == 0:
    print(f'{check_number} is an even number')
else:
    print(f'{check_number} is an odd number')