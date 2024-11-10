'''
This is how you work out whether if a particular year is a leap year. 
- on every year that is divisible by 4 with no remainder
- except every year that is evenly divisible by 100 with no remainder 
- unless the year is also divisible by 400 with no remainder   
'''

def is_leap_year(year):
    '''
        Takes a year value and returns a statement of whether it is a leap year or not.
    '''
    if year % 4 != 0:
        return 'Not Leap Year'
    else:
        if year % 100 != 0:
            return 'Leap Year'
        else: 
            if year % 400 != 0:
                return 'Not Leap Year'
            else:
                return 'Leap Year'

def get_year():
    '''
        Prompts a user for a year they want to check whether it is a leap year or not.
    '''
    year = 0
    while year < 1:
        try:
            year = int(input('Enter the year you want check if it\'s a leap year of not: '))
        except:
            print('Invalid input: Please enter a positive number as a year!')
            pass
    return year

year = get_year() 
print(is_leap_year(year))