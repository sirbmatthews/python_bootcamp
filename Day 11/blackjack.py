from random import choice
from os import system

art = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      '------'                           |__/  
'''

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_game():
    '''
        Prompts a user if they want to play a game of Blackjack. Return True if yes and False if no.
    '''
    while True:
        try:
            play = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ')
            if play != 'y' and play != 'n': raise
            elif play == 'y': return True
            else: return False
        except: print('Invalid option, type \'y\' for yes or \'n\' for no.')

def deal_card():
    '''
        Return a random card from the deck
    '''
    global cards
    card = choice(cards)
    cards.pop(cards.index(card))
    return card

def add(cards):
    '''
        Return the sum of all cards values.
    '''
    return sum(cards)

def hit_or_stand():
    '''
        Prompts a user if they want another card. Return True if yes and False if no.
    '''
    while True:
        try:
            play = input('Type \'y\' to get another card, type \'n\' to pass: ')
            if play != 'y' and play != 'n': raise
            elif play == 'y': return True
            elif play == 'n': return False
        except: print('Invalid option, type \'y\' or \'n\'.')

def is_blackjack(user_cards):
    '''
        Return True if user hit a Blackjack, else False
    '''
    user_total = add(user_cards)
    
    if user_total == 21: return True
    else: return False
      
def print_game_scores(user_cards, computer_card):
    '''
        Prints the current score of the game
    '''
    print(f'Your cards: {user_cards}, current score: {add(user_cards)}')
    print(f'Computer\'s first card: {computer_card}')

def print_final_score(user_cards, computer_cards):
    '''
        Prints the final score of the game
    '''
    print(f'Your final hand: {user_cards}, final score: {add(user_cards)}')
    print(f'Computer\'s final hand: {computer_cards}, final score: {add(computer_cards)}')

def convert_eleven_to_one(cards):
    '''
        Return updated cards. If score is greater than 21, converts 11 into 1.
    '''
    total = add(cards)
    if total > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        total = add(cards)
    return cards
    
def check_score(user_cards, computer_cards):
    '''
        Return 0 if the user total is above 21, else it returns the total score.
    '''
    total = add(user_cards)
    if total > 21:
        print_final_score(user_cards, computer_cards)
        print('You went over. You lose.')
        return 0
    else: return add(user_cards)

def play_computer(cards):
    '''
        Returns Computer's cards once after it play's it's turn.
    '''
    total = add(cards)
    while total < 17:
        draw_card = deal_card()
        cards.append(draw_card)
        total += draw_card
        if total > 21: 
            cards = convert_eleven_to_one(cards)
            total = add(cards)
    return cards

def check_winner(user_cards, computer_cards):
    '''
        Checks who won and prints the results.
    '''
    user_score = add(user_cards)
    computer_score = add(computer_cards)
    
    if computer_score > 21:
        print('Opponent went over. You win.')
    elif computer_score == user_score:
        print('Draw')
    elif computer_score > user_score:
        print('You lose')
    elif computer_score < user_score:
        print('You win')
    
def blackjack():
    '''
        Game controller
    '''
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    print_game_scores(user_cards, computer_cards[0])
    
    is_winner = is_blackjack(user_cards)
    if is_winner:
        print('Win with a Blackjack')
        return
    
    while True:
        draw_card = hit_or_stand()
        if draw_card:
            user_cards.append(deal_card())
            user_cards = convert_eleven_to_one(user_cards)
            print_game_scores(user_cards, computer_cards[0])
            score = check_score(user_cards, computer_cards)
            if score == 0: return
        else: 
            if add(computer_cards) == 21:
                print_final_score(user_cards, computer_cards)
                print('Lose, opponent has a Blackjack')
                return
            else:
                computer_cards = play_computer(computer_cards)
                print_final_score(user_cards, computer_cards)
                check_winner(user_cards, computer_cards)
                return
    
while True:
    if play_game():
        system('clear')
        print(art)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        blackjack()
    else: exit()
