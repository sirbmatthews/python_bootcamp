import random
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************      
''')

print('''
Welcome to Treasure Island
Your mission is to find the treasure
''')

direction = input('You are at a cross road. Where do you want to go? '
                  'Type "left" or "right"\n').lower()

method = int(random.randrange(1, 3))

def if_statements(direction):
      if direction == 'left':
            action = input(   'You\'ve come to a lake. There is an island in the middle of the lake. '
                              'Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
            if action == 'wait':
                  colour = input(   'You\'ve arrived on the island unharmed. There is a house with three doors. '
                                    'One red, one yellow and one blue. Which colour do you choose?\n').lower()
                  
                  if colour == 'red':
                        print('It\'s a room full of fire. Game Over.')
                  elif colour =='yellow':
                        print('You found the treasure. You Win!')
                  elif colour =='blue':
                        print('You enter a room of beasts. Game Over!')
                  else:
                        print('You chose a door that does not exits. Game Over.')
                        
            else:
                  print('You get attacked by an angry trout. Game Over.')

      else:
            print('You fell into a hole. Game Over.')

def case_statements(direction):
      match direction: 
            case 'left':
                  action = input(   'You\'ve come to a lake. There is an island in the middle of the lake. '
                                    'Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()

                  match action: 
                        case 'wait':
                              colour = input(   'You\'ve arrived on the island unharmed. There is a house with three doors. '
                                                'One red, one yellow and one blue. Which colour do you choose?\n').lower()

                              match colour:
                                    case 'red':
                                          print('It\'s a room full of fire. Game Over.')
                                    case 'yellow':
                                          print('You found the treasure. You Win!')
                                    case 'blue':
                                          print('You enter a room of beasts. Game Over!')
                                    case _:
                                          print('You chose a door that does not exits. Game Over.')


                        case _:
                              print('You get attacked by an angry trout. Game Over.')
            
            case _:
                  print('You fell into a hole. Game Over.')


if method == 1:
      case_statements(direction)
else:
      if_statements(direction)