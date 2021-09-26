# to make sure each time the cards a dealt is it random 

import random
import time # give it some time

cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
specialcards = ['J','Q','K']
playercards = []
dealercards = []

def getcard():
    """
    This function will get a random card each time
    """
    card = random.randrange(13) # 0 inded basis
    return cards[card]

def givecard(cards):
    card = getcard()
    cards.append(card)


# the player will get 2 cards
#def giveplayercard():
#    card = getcard()
#    playercards.append(card)


# the dealer will get 2 cards
# def givedealercard():
#     card = getcard()
#     dealercards.append(card)


# it will increment 1 if it is an Aces and if it an special card it will increment 10
# if it is none of it, it will increment the value of the card itself. 
def gethandvalue(cards):
    counter = 0
    for card in cards:
        if card == 'A':
            counter +=1
        elif card in specialcards:
            counter += 10
        else:
            counter += int(card)    
    return counter

def printdealerhand(cards, firsttime = False):
    print(f'Dealer\'s deck: ',end='')
    for card in cards:
        print(f'[{card}]',end='')
        if firsttime:
           print(f'[?]',end='')
           break
    print()


def dealerturn():
    while True:
        if gethandvalue(dealercards) >= 17:
           return False
        else:
           givecard(dealercards)
           printdealerhand(dealercards)
           time.sleep(1)
           if gethandvalue(dealercards) > 21:
               return True



def printplayerhand(cards):
    print(f'Your deck: ', end='')
    for card in cards:
        print(f'[{card}]',end='')
    print()    


# while playing the user can decide to hit or stay
def playerturn():
    while True:
        answer = input("Will you hit or will you stay?")
        if answer.lower() == 'hit':
           givecard(playercards)
           printplayerhand(playercards)
           time.sleep(1)
           value = gethandvalue(playercards)
           if value > 21:
               return True
           elif value == 21:
                return True 
        else:
           return False


# once the player goes over 21, the game is over.
def gameover():
    if gethandvalue(playercards) == 21:
        print('You win! Congrats')
    else:
        print ('Oh! you lose it')    
       

def startgame():
    for i in range(2):
        givecard(playercards)
        givecard(dealercards)

    printplayerhand(playercards)
    time.sleep(1)
    printdealerhand(dealercards, True)
    time.sleep(1)
  
    if playerturn():
        gameover()
        return

    if dealerturn():
        print('uhu! You win!')

    playervalue =  gethandvalue(playercards)
    dealervalue = gethandvalue(dealercards)   

    if playervalue < dealervalue:
        print('oh!You lose')
    elif playervalue == dealervalue:
        print('You draw!')
    else:
        print('You win the game! Congrats!')    

    printplayerhand(playercards)
    print(gethandvalue(playercards))    


startgame()


    