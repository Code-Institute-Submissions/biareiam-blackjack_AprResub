import random
import time

#Defining Variables 
card_suits = ('♥', '♦', '♠', '♣')
card_ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
card_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10,
         'Q':10, 'K':10, 'A':1}
playing = True

#Creating Card Class
class Card():
    def __init__(self,suit,rank):
        self.suit = suit 
        self.rank = rank 
        self.value = card_values[rank]
    
    #returns rank of suit if printed 
    def __str__(self):
        return self.rank +" "+ self.suit

class Deck():

    def __init__(self):
        self.all_cards = []
      
        for suit in card_suits:
            for rank in card_ranks :
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def __str__(self):
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += '\n' + card.__str__()
        return "The deck has:  " + deck_comp
            
    def shuffle(self):
        random.shuffle(self.all_cards)
   
    def deal(self):
        single_card = self.all_cards.pop()
        return single_card 

#Creating Hand Class that refers to the cards in Player and Dealer's Hand
class Hand():
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0    
    
    def add_card(self,card):
        self.cards.append(card)
        self.value = self.value + card.value
        
        if card.rank == 'Ace':
            self.aces += 1
            
    def value_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10 
            self.aces -= 1 


def hit(deck,hand):
    """
      This function will draw cards to the player or dealers hand, while adjusting the value of ace.
    """
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.value_ace()


def hit_or_stand(deck,hand):
    """
      This function asks the player if he.she wants to keep playing and get an extra card (hit) or end the game (stay)
    """
    global playing  
    
    while True:
        print()
        x = input("Do you want to hit or stay? Enter 'h' or 's' :")
        
        if x[0].lower() =='h':
            hit(deck,hand)
            print("\nPlayer Hits !")
            
        elif x[0].lower() == 's':
            print("\nPlayer Stands, Dealer's Turn")
            playing = False
            
        else:
            print("\nSorry, I did not understand that, please enter h or s")
            continue

        break


def show_some(player,dealer):
    """
    This funstion will display the player's cards and one of the dealer's card.
    """
    print("\nCurrent cards in hand:")
    print("\nDealer's Hand: ")
    print("  <Hidden Card!>")
    print(f"  {dealer.cards[1]}")
    
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(f"  {card}")


def show_all(player,dealer):
    """
    This function will show all the cards on the player's and dealer's hand.
    """
    print("/---------------------------------------------------------/")
    print("\n                   Final Result:")
    print("\nDealer's Hand: ")
    for card in dealer.cards:
        print(f"  {card}")
    print()
    print(f"  The total value of Dealer's hand is {dealer.value}")
    time.sleep(1)

    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(f"  {card}")
    print()    
    print(f"  The total value of Player's hand is {player.value}")
    



def player_busts(player,dealer):
    """
     This function will display a message if the player busted.
    """
    print("\nOh,Player busted! The dealer won the game! 😒")
    
 

def player_wins(player,dealer):
    """
    This function will display a message if the player wins the game.
    """
    print("\nUhu! The player won the game!! 😁")

    


def dealer_busts(player,dealer):
    """
     This function will display a message if the player wins the game and the dealer busted.
    """
    print("\nThe dealer busted! Congrats, the player won the game !! 👏😁")
   
  


def dealer_wins(player,dealer):
    """
     This function will display a message if the dealer wins the game.
    """
    print("\nOh no!The dealer won! 😒")
   


def create_player():
    """
    This funtion to asks the user to choose a username.
    """
    global player
    
    while True:
        name = input("Please enter a username: ")
        print()
        print("⭐ ⭐ Welcome to the BlackJack game", name + " !⭐ ⭐")
        print()
        if name != ' ':
            break
        else:
            print("Enter a valid name.\n")



def push():
    """
    This function will display a message was the game was a tie.
    """
    print("\nDealer and Player tie! 😅")

while True:
    
    create_player()
    print('The rules are:')
    print('- The objective is to get a hand total of closer to 21 than the dealer without going over 21.')
    print('- At the start of the game, the player and the dealer receive two cards each.')
    print('- Kings, Queens, and Jacks are worth 10 points.')
    print('- Aces are worth 1 or 11 points.')
    print('- Cards 2 through 10 are worth their face value.')
    print('- Hit to take another card.\n- Stay to stop taking cards.')
    print()
    print('Good luck and enjoy it!😏')
    time.sleep(1)
    
    
    # Create and shuffle the deck
    New_Deck = Deck()
    New_Deck.shuffle()

    # Dealing two cards to each player
    Dealer_hand = Hand()
    Player_hand = Hand()
        
    Player_hand.add_card(New_Deck.deal())
    Dealer_hand.add_card(New_Deck.deal())
    Player_hand.add_card(New_Deck.deal())
    Dealer_hand.add_card(New_Deck.deal())
    time.sleep(2)
    

    # Shoing the player's hand and displaying only one of the dealer's cards
    show_some(Player_hand,Dealer_hand)
    time.sleep(1)
    
    while playing:  
        
        hit_or_stand(New_Deck,Player_hand)
        show_some(Player_hand,Dealer_hand)
        time.sleep(1)
        # If player's hand goes over 21, run player_busts() and break out of loop
        if Player_hand.value > 21:
            show_all(Player_hand,Dealer_hand)
            player_busts(Player_hand,Dealer_hand) 
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if Player_hand.value <= 21:
        
        while Dealer_hand.value < 17:
            hit(New_Deck,Dealer_hand)
            continue
            
        
        # Different winning scenarios
        if Dealer_hand.value > 21:
            dealer_busts(Player_hand,Dealer_hand)
        
        elif Dealer_hand.value > Player_hand.value:
            dealer_wins(Player_hand,Dealer_hand)

        elif Dealer_hand.value < Player_hand.value:
            player_wins(Player_hand,Dealer_hand)

        else:
            push()
    
    
        show_all(Player_hand,Dealer_hand)
        

    
    # Ask player, if he/she wants to continue playing the game
   
    play_again = input("\nWould you like to play again ? Enter y for yes and n for no: ")
    
    if play_again[0].lower() == 'y':
        playing = True 
        continue 
    elif play_again[0].lower() == 'n':
        playing = False 
        print("\nThank You for Playing Blackjack, hope you had fun !!")
        print()
        break
    else:
        print("You have not entered a valid Input, the game will end!")
        print("Thanks for playing, until next time! o/")
        print()
        break
