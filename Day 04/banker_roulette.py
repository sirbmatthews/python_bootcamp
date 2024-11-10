from random import choice, randint

friends = ['Alice', 'Bob', 'Charlie', 'David', 'Emanuel']

# Option 1: choice
print(choice(friends))

# Option 2: index
index = randint(0, 4)
print(friends[index])
