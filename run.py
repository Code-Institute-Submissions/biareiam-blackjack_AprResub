#Importing Random Library 
import random

#Defining Variables 
Suits = ('♥', '♦', '♠', '♣')
Ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
Values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10,
         'Q':10, 'K':10, 'A':1}
playing = True

#Creating Card Class
class Card():
    def __init__(self,suit,rank):
        # Suit 
        self.suit = suit 
        # Rank
        self.rank = rank 
        # Corresponding Value  by indexing
        self.value = Values[rank]
    
    #returns rank of suit if printed 
    def __str__(self):
        return self.rank +" "+ self.suit

class Deck():
    #Creates an empty list to which all cards are appended to
    def __init__(self):
        self.all_cards = []
        #The double for loop creates 13 ranks for each Suit
        for suit in Suits:
            for rank in Ranks:
                #Create the Card Object
                created_card = Card(suit,rank)
                #Appends the created cards one by one to the list.
                self.all_cards.append(created_card)
                
    def __str__(self):
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += '\n' + card.__str__()
        return "The deck has:  " + deck_comp
            
    def shuffle(self):
        #Shuffles the list containing the cards
        random.shuffle(self.all_cards)
   
    def deal(self):
        #pops the item of a list based on the index specified
        single_card = self.all_cards.pop()
        return single_card 

#Creating Hand Class that refers to the cards in Player and Dealer's Hand
class Hand():
    def __init__(self):
        self.cards = []  # starting with an empty list
        self.value = 0   # starting  with zero value
        self.aces = 0    # adding an attribute to keep track of aces
    
    def add_card(self,card):
        #After appending cards to Hand, Value of Hand is also modified.
        self.cards.append(card)
        self.value = self.value + card.value
        
        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_ace(self):
        #If the value of hand exceeds 21 because ace value is taken as 11, subtract 10 from the total value. 
        while self.value > 21 and self.aces:
            self.value -= 10 
            self.aces -= 1 


 


#Function that draws cards to hand of PLayer or Dealer while adusting for ace value
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

#Asks user if he is going to stand or hit 
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop, global variable can be changed.
    
    while True:
        print('\n')
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

#Function that shows some of the cards in hand 
def show_some(player,dealer):
    print("\nCurrent cards in hand:")
    print("\nDealer's Hand: ")
    print("  <Hidden Card!>")
    print(f"  {dealer.cards[1]}")
    
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(f"  {card}")

#Function that shows all cards in hand 
def show_all(player,dealer):

    print("\nFINAL RESULT :")
    print("\nDealer's Hand: ")
    for card in dealer.cards:
        print(f"  {card}")
       
    print(f"  Value of Dealer's hand is {dealer.value}")
    
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(f"  {card}")
        
    print(f"  Value of Player's hand is {player.value}")

#Function for when Player is busted
def player_busts(player,dealer):
    print("\nPlayer busted! Sorry,the dealer won!! 😒")
 

#Function for when Player WINS 
def player_wins(player,dealer):
    print("\nPlayer won the game!! 😁")
    

#Function for when Player WINS cause Dealer is Busted 
def dealer_busts(player,dealer):
    print("\nThe dealer busted! Congrats the player won the game !!! 👏😁")
  

#Function for when Dealer WINS 
def dealer_wins(player,dealer):
    print("\nOh no!The dealer won! 😒")


def create_player():
    """
    Funtion to create a Player.
    """
    global player
    
    while True:
        name = input("Please enter a username: ")
        print()
        print("⭐ ⭐ Welcome to the BlackJack game", name + " !⭐ ⭐")
        print()
        if name != '':
            break
        else:
            print("Enter a valid name.\n")


#When it is a tie.
def push():
    print("\nDealer and Player tie! 😅")

while True:
    
    # Printing an opening statement
    create_player()
    print('The rules are:')
    print('The objective is to get a hand total of closer to 21 than the dealer without going over 21.')
    print('At the start of the game, the player and the dealer receive two cards each.')
    print('Kings, Queens, and Jacks are worth 10 points./nAces are worth 1 or 11 points.\nCards 2 through 10 are worth their face value.\nHit to take another card.\nStay to stop taking cards.')
    print()
    print('Good luck!😏')
    
    
    # Creating & shuffling the deck, dealing two cards to each player
    New_Deck = Deck()
    New_Deck.shuffle()
    
    Dealer_hand = Hand()
    Player_hand = Hand()
        
    Player_hand.add_card(New_Deck.deal())
    Dealer_hand.add_card(New_Deck.deal())
    Player_hand.add_card(New_Deck.deal())
    Dealer_hand.add_card(New_Deck.deal())
    
   

    # Shows cards (but keeps one dealer card hidden)
    show_some(Player_hand,Dealer_hand)
    
    while playing:  #variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(New_Deck,Player_hand)
        
        # Shows cards (but keeps one dealer card hidden)
        show_some(Player_hand,Dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if Player_hand.value > 21:
            show_all(Player_hand,Dealer_hand)
            player_busts(Player_hand,Dealer_hand) 
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if Player_hand.value <= 21:
        
        while Dealer_hand.value < 17:
            hit(New_Deck,Dealer_hand)
            continue
            
        
        # Test different winning scenarios
            # Run different winning scenarios
        if Dealer_hand.value > 21:
            dealer_busts(Player_hand,Dealer_hand)
        
        elif Dealer_hand.value > Player_hand.value:
            dealer_wins(Player_hand,Dealer_hand)

        elif Dealer_hand.value < Player_hand.value:
            player_wins(Player_hand,Dealer_hand)

        else:
            push()
    
        # Show all cards
        show_all(Player_hand,Dealer_hand)
        

    
    # Ask to play again
   
    play_again = input("\nWould you like to play again ? Enter y for yes and n for no: ")
    
    if play_again[0].lower() == 'y':
        playing = True 
        continue 
    elif play_again[0].lower() == 'n':
        playing = False 
        #End Message
        print("\nThank You for Playing Blackjack !!")
        break
    else:
        print("You have not entered a valid Input, Game Ends !")
        print("Until next time!")
        break
#End of Game Code 