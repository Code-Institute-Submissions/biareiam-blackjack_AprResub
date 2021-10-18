# BlackJack/21 command-line application game

Welcome to my 3rd project.The aim of this project was to build a command-line game of 21 or BlackJack using Python.The goal of this game is to amount card values as near to 21 as possible without exceeding or 'busting' it. It is simple If the dealer gets closer to 21 points or 21 exactly, it wins the game. If the player is the one who gets closer to 21 or 21 exactly, they are the winner. This game will not be dealing with bets. 

Here is the live version of my project

 ![command-line game](https://game-21.herokuapp.com/)

## How to play

The game is played with a deck of 52 cards. In this version, the player will be only playing against the dealer and no bets will be placed. 
After shuffling the deck, the player and the dealer will get two cards each. The player will only be able to see his/her cards. Cards should be dealt one at a time. Throughout the game the player can choose to hit, which means get an extra card or stay, at this stage either the player or dealer receive another card and the results are printed. At this point, the player can then see the dealer’s cards, how much it was added to and who won the game. As previously mentioned, the winner is the one who got as close as possible to 21 without busting.

Card Values are as follows:
- Ace: It has a value of either 11 or 1 as needed to reach 21 without busting. 
- 2-10 -  the card  value is the same as the number printed in the cards, example. 2 is 2, 3 is 3 and so on. 
- Jacks, Queens, and Kings each have a value of 10.

The rules of the original game can be found here : [Wikipedia](https://en.wikipedia.org/wiki/Blackjack) 

## Features

* Welcoming
    * The player will be asked to enter his/her name and a welcome message will be printed along with a brief explanation of the rules of the game.

     ![welcome](https://user-images.githubusercontent.com/65717229/137708506-54297d8f-0dc9-415a-a942-ca2e5a2cccc1.PNG) 

     ![rules](https://user-images.githubusercontent.com/65717229/137708727-b5602601-c924-4172-844b-e6edccf40f6f.PNG)

* Random card generation
    * As mentioned previously, the dealer and the player will get two random cards in the beginning of the game.
    * The player will have the ability to see one of the dealer’s cards at the start of the game. 

     ![deck](https://user-images.githubusercontent.com/65717229/137708802-cfacb2b3-8def-49f0-9caf-7d5d2931564f.PNG)

* Accepts user input
    * Once the cards are displayed, the player can choose to hit or stay
    * The player is able to hit as many times as they want as long it does not go over 21. Once it happens, the game is over and the results are printed. 

     ![stay or hit](https://user-images.githubusercontent.com/65717229/137708897-175c13bd-00d3-4533-950e-664459095a47.PNG)

* Results
    * Once the game is over, the results board is printed. The player will then be able to see the dealer’s cards and how much the cards add up to.

     ![result 1](https://user-images.githubusercontent.com/65717229/137708956-e1ce7235-9793-4569-8c74-2294f6afb20c.PNG)
     ![result 2](https://user-images.githubusercontent.com/65717229/137709053-3c8aac14-abf8-4b0e-abba-145c65ad1dc1.PNG)

## Future Features

 * Make the cards being printed as “actual” cards.
 * More than one player. 

## Testing

I have manually tested this project by doing the following:

- Starting and playing the game several times. 
- Given invalid inputs.
- Tested in my local terminal and the Code Institute Heroku terminal.

## Deployment 

This project was deployed using Code Institute’s mock terminal for Heroku.
    - Steps for deployment were: 
    - Fork or clone this repository
    - Create a new Heroku app
    - Set the builtbacks to Python and NodeJS in that order
    - Link Heroku app to the repository
    - Clicking on Deploy


## Credits

* Code Institute for the deployment terminal
* [Bicyclecards](https://bicyclecards.com/how-to-play/blackjack/) for the rules of the blackjack/21 game.
* [Brilliant](https://brilliant.org/wiki/programming-blackjack/) - Helped to have a better understading of the logic of the game.


## Acknowledgements

I appreciate the support, feedback and guidance of the following people throughout this project: my mentor Victor Miclovich, the tutors and the community on slack.
This is for educational use.







