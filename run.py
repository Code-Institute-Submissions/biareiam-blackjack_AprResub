# to make sure each time the cards a dealt is it random 

import random

cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
specialcards = ['J','Q','K']
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


def playerturn():
    while True:
        answer = input("Will you hit or will you stay?")
        if answer.lower() == 'hit':
           giveplayercard()
           print(playercards)
           value = gethandvalue(playercards)
           if value > 21:
               return True   
        else:
           return False

def gameover():
    print ('Oh! you lost it')  
       

def startgame():
    # it will print 2 random cards, and append them to the playercards hand each time. 
    for i in range(2):
        giveplayercard()
    print(playercards)

    if playerturn():
        gameover()

    print(playercards)
    print(gethandvalue(playercards))    


startgame()


    