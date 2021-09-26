# to make sure each time the cards a dealt is it random 

import random

cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
playercards = []

def getcard():
    """
    This function will get a random card each time
    """
    card = random.randrange(13) # 0 inded basis
    return cards[card]

def giveplayercard():
    card = getcard()
    playercards.append(card)

def playerturn():
    while True:
        answer = input("Will you hit or will you stay?")
        if answer.lower() == 'hit':
           giveplayercard()
           print(playercards)
        else:
           return 

def startgame():
    # it will print 2 random cards, and append them to the playercards hand each time. 
    for i in range(2):
        giveplayercard()
    print(playercards)

    playerturn ()
    print(playercards)    


startgame()


    