import os

print('''
                         ___________
                                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'\''---------'' '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')


bids = {}
names = []

# Request bidder name, two bidders cannot have the same name.
def request_name():
    name = ''
    while name == '':
        name = input('What is your name?: ').capitalize()
        if name in names:
            print(f'{name} has already placed their bid.')
            name = ''
        else:
            names.append(name)
    return name

# Request a bidder's bid amount, ensure it is 0 or above
def request_bid():
    bid = -1
    while bid < 0:
        try:
            bid = int(input('What is your bid?: $'))
            if bid < 0 : raise
        except:
            print('Your bid should be a number equal to or greater than $0')
            pass
    return bid

# Check if there are more bidders
def check_more_bidders():
    bidder  = ''
    while bidder != 'yes' and bidder != 'no':
        bidder = input('Are there any other bids? Tpe \'yes\' or \'no\'. ')
    return bidder

# Check who is the highest bidder
def check_highest_bidder(bids):
    highest_bid = 0
    tie = []
    
    for name in bids:
        if bids[name] > highest_bid:
            highest_bid = bids[name]
            tie = [name]
        elif bids[name] == highest_bid:  
            tie.append(name)
    
    if len(tie) > 1:
        winner = ', '.join(tie)
        print(f'It is a tie between {winner} with a bid of ${highest_bid}') 
    else:
        print(f'The winner is {''.join(tie)} with a bid of ${highest_bid}')    
    

add_a_bidder = True
while add_a_bidder:
    
    name = request_name()
    bid = request_bid()
    bids[name] = bid   
    bidder = check_more_bidders()
        
    if bidder == 'no':
        check_highest_bidder(bids)
        add_a_bidder = False
    else:
        os.system('clear')