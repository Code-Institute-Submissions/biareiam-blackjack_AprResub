# to make sure each time the cards a dealt is it random 
import random 
# Create a deck of cards and a player dealer hand
deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
'J', 'Q','K','A','J', 'Q','K','A','J', 'Q','K','A','J', 'Q','K','A']
playerHand = []
dealerHand = []

# Create a function which deals the cards

def dealCard(turn):
    """
    This function will deal the cards randomly
    """
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)


# Take each players hand (players and dealer) and calculate the total on each hand
# check for the winner of the game
# Game loop -  to start the game

