import random
import time
import re

# Defining Variables
card_suits = ('♥', '♦', '♠', '♣')
card_ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
card_values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 1
}
playing = True
# Creating Card Class


class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = card_values[rank]
# returns rank of suit if printed

    def __str__(self):
        return self.rank + " " + self.suit


class Deck():

    def __init__(self):
        self.all_cards = []
        for suit in card_suits:
            for rank in card_ranks:
                deck_card = Card(suit, rank)
                self.all_cards.append(deck_card)

    def __str__(self):
        deck_cards = ''
        for card in self.all_cards:
            deck_cards += '\n' + card.__str__()
        return "The deck has:  " + deck_cards

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        single_card = self.all_cards.pop()
        return single_card

# Creating Hand Class that refers to the cards in Player and Dealer's Hand


class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value = self.value + card.value
        if card.rank == 'Ace':
            self.aces += 1

    def ace_value(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


def hit(deck, hand):
    """ Draw cards, while adjusting the value of ace."""
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.ace_value()


def hit_or_stand(deck, hand):
    """This function asks the player if they want to keep playing and get an
    extra card (hit) or end the game (stay)"""

    global playing
    while True:
        print('\n')
        player_move = input("Do you want to hit or stay? Enter 'h' or 's' :")
        player_move = re.fullmatch(r'h|s', player_move)
        if player_move is None:
            print("Sorry, I did not understand that, enter h or s")
        elif player_move.group(0) == 'h':
            hit(deck, hand)
            print("Player Hits !")
        elif player_move.group(0) == 's':
            print("Player Stands, Dealer's Turn")
            playing = False
        else:
            print("\nInvalid input, please enter h or s")
            continue
        break


def show_some(player, dealer):
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


def show_all(player, dealer):
    """
    This function will show all the cards on the player's and dealer's hand.
    """
    print("\n")
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
    print(f"  The total value of Player's hand is {player.value}\n")


def player_busts(player, dealer):
    """ Function for when Player is busted """
    print("\nOh,Player busted! The dealer won the game! 😒\n")


def player_wins(player, dealer):
    """Function for when Player wins the game."""
    print("\nThe player wins the game!! 😁\n")


def dealer_busts(player, dealer):
    """Function for when Player WINS cause Dealer is Busted """
    print("\nThe dealer busted! Player wins!! 👏😁\n")


def dealer_wins(player, dealer):
    """Function for when Dealer wins the game"""
    print("\nOh no!The dealer won! 😒\n")


def push():
    """Function for when there is a tie"""
    print("\nDealer and Player tie !\n")


def create_player():
    """
    This funtion to asks the user to choose a username.
    """
    global player
    while True:
        name = input("Please enter a username:")
        print("\n")
        print("⭐ ⭐ Welcome to the BlackJack game", name + " !⭐ ⭐\n")
        name = re.fullmatch(r'(([a-z]|[A-Z]))+\d*', name)
        if name is None:
            print("Enter valid username. It must start with a letter.\n")
        else:
            name = name.group(0)
            break


while True:
    create_player()
    print('The rules are:')
    print('Get as close to 21 as you can without being busted.')
    print('At the start, the player and the dealer receive two cards each.')
    print('Notes:')
    print('- Kings, Queens, and Jacks are worth 10 points.')
    print('- Aces count as 1 or 11.')
    print('- Cards 2 through 10 are worth their face value.')
    print('- Hit to take another card.\n- Stay to stop taking cards.\n')
    print('Good luck and enjoy it!😏\n')
    print("/---------------------------------------------------------/")
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
    time.sleep(1)

# Showing the player's hand and displaying only one of the dealer's cards
    show_some(Player_hand, Dealer_hand)
    time.sleep(1)
    while playing:
        hit_or_stand(New_Deck, Player_hand)
        show_some(Player_hand, Dealer_hand)
        time.sleep(1)
        # If the hand goes over 21, run player_busts() and break out of loop
        if Player_hand.value > 21:
            show_all(Player_hand, Dealer_hand)
            player_busts(Player_hand, Dealer_hand)
            break
# If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if Player_hand.value <= 21:
        while Dealer_hand.value < 17:
            hit(New_Deck, Dealer_hand)
            continue
        # Different winning scenarios
        if Dealer_hand.value > 21:
            dealer_busts(Player_hand, Dealer_hand)
        elif Dealer_hand.value > Player_hand.value:
            dealer_wins(Player_hand, Dealer_hand)
        elif Dealer_hand.value < Player_hand.value:
            player_wins(Player_hand, Dealer_hand)
        else:
            push()
        show_all(Player_hand, Dealer_hand)

# Asks if the player  wants to play again
    play_again = input("\nWant to restart the game? y for yes and n for no:\n")
    if play_again[0].lower() == 'y':
        playing = True
        continue
    elif play_again[0].lower() == 'n':
        playing = False
        print("\nThank You for Playing Blackjack, hope you had fun !!\n")
        break
    else:
        print("You have not entered a valid Input, the game will end!\n")
        print("Thanks for playing, until next time! o/\n")
        break
