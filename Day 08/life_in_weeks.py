'''
Life in Weeks

Take your current age as the input and output a message with your time left in weeks until age 90.
'''

def life_in_weeks(age):
    return (90 - age) * 52

age = int(input('How old are  you? '))
    
print(f'You have {life_in_weeks(age)} weeks left.')