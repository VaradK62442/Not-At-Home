# Not At Home
# 3 CPU, 1 player

import random, time, itertools

class opponent:
    def __init__(self, difficulty, hand):
        self.d = difficulty
        self.h = hand


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
        opponents[-1] = opponent(diff, [])

    return opponents


def dealCards(opponents):
    # create list of cards using itertools
    deck = list(itertools.product(['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k'], ['spade', 'heart', 'diamond', 'club']))
    # shuffle guess
    random.shuffle(deck)

    playerHand = []

    # deal out cards
    for i in range(len(deck)):
        if i%4 == 0:
            playerHand.append(deck[i])
        elif i%4 == 1:
            opponents[0].h.append(deck[i])
        elif i%4 == 2:
            opponents[1].h.append(deck[i])
        else:
            opponents[2].h.append(deck[i])

    #for i in range(0,3):
    #    print(f"comp {i+1}:\n{opponents[i].h}\n")

    #print(playerHand)

    return opponents, playerHand


def easyGuess(opponents, playerHand):
    pass


def medGuess(opponents, playerHand):
    pass


def hardGuess(opponents, playerHand):
    pass


def startRound1(opponents, playerHand):
    turn = 1

    suits = ["spades", "diamonds", "clubs", "hearts"]
    cards = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']
    names = ["player", "cpu 1", "cpu 2", "cpu 3"]

    match turn:
        case 1:
            print("Your hand: ")
            print(playerHand)

            suitGuess = ""
            print("Please enter which suit you would like to guess: ")
            print("- Spades\n- Diamonds\n- Clubs\n- Hearts\n")
            while suitGuess.lower() not in suits:
                suitGuess = input()

            cardGuess = ""
            print("Please enter which card you would like to guess: ")
            print("- A\n- 2\n- 3\n- 4\n- 5\n- 6\n- 7\n- 8\n- 9\n- 10\n- J\n- Q\n- K\n")
            while cardGuess.lower() not in cards:
                cardGuess = input()

            target = ""
            print("Please enter who you would like to ask: ")
            print("- CPU 1\n- CPU 2\n- CPU 3\n")
            while target.lower() not in names:
                target = input()

            if target.lower() == "cpu 1":
                target = 0
            elif target.lower() == "cpu 2":
                target = 1
            else:
                target = 2

            if [cardGuess, suitGuess] in opponents[target].h:
                print(f"The chosen card - the {cardGuess} of {suitGuess} -  was in the chosen opponent's hand.")
                playerHand.append([cardGuess, suitGuess])
                opponents[target].h.remove([cardGuess, suitGuess])
            else:
                print(f"Not at home! The chosen card - the {cardGuess} of {suitGuess} -  was not in the chosen opponent's hand.")

            turn = turn + 1 + target
        case 2: # cpu 1
            if opponents[0].diff == "1":
                easyGuess(opponents, playerHand)
            elif opponents[0].diff == "2":
                medGuess(opponents, playerHand)
            else:
                hardGuess(opponents, playerHand)
        case 3: # cpu 2
            if opponents[1].diff == "1":
                easyGuess(opponents, playerHand)
            elif opponents[1].diff == "2":
                medGuess(opponents, playerHand)
            else:
                hardGuess(opponents, playerHand)
        case 4: # cpu 3
            if opponents[2].diff == "1":
                easyGuess(opponents, playerHand)
            elif opponents[2].diff == "2":
                medGuess(opponents, playerHand)
            else:
                hardGuess(opponents, playerHand)


def startRound2(opponenets, playerHand):
    pass


def declareWinner(opponenets, playerHand):
    pass


def playGame():
    opponents = decideDifficulty()
    opponents, playerHand = dealCards(opponents)
    opponents, playerHand = startRound1(opponents, playerHand)
    opponents, playerHand = startRound2(opponents, playerHand)
    opponents, playerHand = declareWinner(opponents, playerHand)


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

if __name__ == "__main__":
    menu()