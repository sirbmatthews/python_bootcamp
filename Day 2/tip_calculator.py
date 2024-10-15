# Project that calculates a tip and split the bill

# Print the welcome message
print('Welcome to the tip calculator!')

# Prompt the bill amount
bill = float(input('What was the total bill? '))

# Prompt the tip percentage
tip = float(input('How much tip would you like to give? 10, 12 or 15 '))

# Ptompt the number of people spliting the bill
people = int(input('How many people to split the bill? '))

# Calculate the total bill, including tip
total_bill = bill + (bill * tip / 100)

# Calculate each person's damage
each_person_bill = round((total_bill / people), 2)

# Print the total paid by each person
print(f'Each person should pay ${each_person_bill}')