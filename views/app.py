# Score rules - Face cards each count as 10, Aces count as 1 or 11, all others count at face value. 
# An Ace with any 10, Jack, Queen, or King is a “Blackjack.


#### Game #####

# Create a deck of cards and a player dealer hand
# Create a function which deals the cards
# Take each players hand (players and dealer) and calculate the total on each hand
# check for the winner of the game
# Game loop -  to start the game










# to make sure each time the cards a dealt is it random 
import random 

playerIn = True
dealerIn = True 

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

def total (turn):
    total = 0
    face = ["J",'K','Q']

    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total +=1
            else:
                total += 11   
    return total             
# check for the winner of the game

def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0],dealerHand[1]    

# Game loop -  to start the game

for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)
#print(dealerHand)
#print (playerHand)  
while playerIn or dealerIn:
    print(f"Dealer had {revealDealerHand()} and X")  
    print(f"You have {playerHand} for a total of {total(playerHand)}") 

    if playerIn:
        stayOrHit = input ("1: Stay\n2: Hit\n")
        if total(dealerHand)>16:
            dealerIn = False
        else:
            dealCard(dealerHand)
        if stayOrHit == '1':
            playerIn = False
        else :
            dealCard(playerHand)
        if total(playerHand) >= 21:
            break
        elif total(dealerHand) >= 21:
            break

if total(playerHand) == 21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")                         
    print("Blackjack! You win!")
elif total(dealerHand) == 21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")  
    print("Blackjack! Dealer wins!")     
elif total(playerHand) > 21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("You bust! Dealer win!")
elif total(dealerHand) > 21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Dealer busts, you win!")
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")  
    print("Dealer wins!")  
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("You win!")    




