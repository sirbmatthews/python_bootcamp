# Project that generates a band name using the name of your city and pet.

# Print the welcome message
print('Welcome to the Band Name Generator.')

#  Prompt for a city name
city_name = input('What is the name of the city you grew up in?\n')

#  Prompt for a pet name
pet_name = input('What\'s your pet\'s name?\n')

# Generate the band name
band_name = city_name + ' ' + pet_name

# Output the generated band name
print(f'Your band name could be {band_name}')