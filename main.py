# Not At Home
# 3 CPU, 1 player

import random
import time

class opponent:
    def __init__(self, difficulty):
        self.d = difficulty


def rules():
    ruleStr = '''
    Not at home is a game for 3+ players. All cards are dealt out to all players.
    This game will be played with you, and 3 other computer opponents.
    The game is split into 2 rounds, and the aim of the game is to collect all of the cards by the end.

    Round 1:
    Player 1 must ask any another player for a specific card, for example the 2 of Clubs, in the format 2C.
    If the player who has been asked has that card, they must give it to the player who asked them.
    The player then keeps aasking for cards until the player they have asked does not have the requested card.
    Then, the turn passes on to the player who did not have the requested card. 

    N.B. A player can only ask for a card if they have at least one of the card number in their hand.
    For example, a player cannot ask for a 4 of diamonds if they do not have a 4 of any suit in their hand.

    This continues until all players have sets of 4 cards in their hands, 
    e.g. you may have 4 Queens, 4 Aces, 4 2s, etc.
    The game then progresses to round 2

    Round 2:
    Now, the player whose turn it is asks for sets of cards, instead of specific cards.
    For example, a player could ask for all of the 5s.
    Similar to above, this continues until the asked player does not have the requested set, and the turn passes to them.
    The game ends when one person has every single card in the deck.
    '''

    print(ruleStr)
    menu()


def decideDifficulty():
    print("Please decide the difficulty for the 3 opponents, from [1] - Easy, [2] - Medium, [3] - Hard")

    availableDiffs = ["1", "2", "3"]
    opponents = []
    for i in range(3):
        print(f"Enter difficulty for opponent {i+1}")
        diff = input()

        while diff not in availableDiffs:
            print("Please enter either [1] for Easy, [2] for Medium, or [3] for Hard difficulty")
            diff = input()

        opponents.append("op")
        opponents[-1] = opponent(diff)


def dealCards():
    pass


def startGame():
    dealCards()


def playGame():
    decideDifficulty()
    startGame()


def menu():
    option = "0"

    while option != "1" and option != "2" and option != "3":
        print("What would you like to do?")
        print("[1] Rules\n[2] Play\n[3] Exit")

        option = input()

    if option == "1":
        rules()

    elif option == "2":
        playGame()

    else:
        exit()


def intro():
    print("Welcome to the famous card game: \nNot At Home!")

    menu()


if __name__ == "__main__":
    intro()