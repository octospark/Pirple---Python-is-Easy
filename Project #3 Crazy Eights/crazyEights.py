information = """
How to play Crazy Eights.

Each player is dealt seven cards.
The remaining cards are placed face down in the center of the table,
forming a draw pile.
The top card of the draw pile is turned face up to start the discard
pile next to it.
First player adds to the discard pile by playing one card that matches the top
card on the discard pile either by suit or by rank (i.e. 6, jack, ace, etc.).
A player who cannot match the top card on the discard pile by suit or rank must
draw cards until he can play one.
When the draw pile is empty, a player who cannot add to the discard pile passes
his turn.
All eights are wild and can be played on any card during a player's turn.
When a player discards an eight, he chooses which suit is now in play.
The next player must play either a card of that suit or another eight.
The first player to discard all of his cards wins.
If no player has discarded all their cards and cannot play the top card of the
discarded pile, the winner is the one with less cards in their hand.
When this number is equal it is a draw.
Press --resume to resume the game: 
"""

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return str(self.rank) + " of " + self.suit

    def legalMove(self, other):
        if self.rank == other.rank or self.suit == other.suit or self.rank == "8":
            return True
        return False

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand # This is a list

    def win(self):
        if len(self.hand) == 0:
            return True
        return False
    
    def getName(self):
        return self.name

    def getHand(self):
        return self.hand

    def printHand(self):
        print()
        print(self.name + "'s hand.")
        for i in range(len(self.hand)):
            print(i, ":", self.hand[i])

def winner(hand1, hand2, discard_pile):
    """Determine the winner of the game if the deck is empty and
    the hands of the players do not contain any cards that can be played
    with the given discard pile"""
    for card in hand1:
        if card.legalMove(discard_pile):
            return False
    for card in hand2:
        if card.legalMove(discard_pile):
            return False
    return True

def crazyEight(card):
    if card.rank == "8":
        print("Choose suit for the next player. Enter a number to match the suit: ")
        print("    0. Hearts")
        print("    1. Clubs")
        print("    2. Diamonds")
        print("    3. Spades")
        choose_suit = input("Your choice: ")
        if choose_suit == "0":
            card.suit = "Hearts"
        elif choose_suit == "1":
            card.suit = "Clubs"
        elif choose_suit == "2":
            card.suit = "Diamonds"
        elif choose_suit == "3":
            card.suit = "Spades"
    return card

def getHelp(value):
    if value == "--help":
        print(information)
        value = input()
        while value != "--resume":
            value = input()
        return True
    return False
    
    
    
    
        
            
#Initialize the deck and shuffle it
suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
         "Queen", "King"]
deck = []

for rank in ranks:
    for suit in suits:
        deck.append(Card(rank, suit))

random.shuffle(deck)

# Ask for the players names and initialize their decks
print("""Welcome to Crazy Eights.After the players enter their names,
they can at any time press --help to get help and --resume to resume the game.
""")
name1 = input("Enter the name of player 1: ")
name2 = input("Enter the name of player 2: ")

hand1 = [deck.pop() for card in range(7)]
hand2 = [deck.pop() for card in range(7)]

player1 = Player(name1, hand1)
player2 = Player(name2, hand2)

# Create the discard pile (which will be implemented as a simple variable
# containing the card at the top of the deck.
discard_pile = deck.pop()

# Players take turns to play
while len(player1.hand) != 0 and len(player2.hand) != 0:
    player1_turn = True
    player2_turn = True
    print()
    print("---------------------------------")
    print(f"It is {player1.getName()}'s turn.", end = "")
    player1.printHand()
    print("Discard pile: ", discard_pile)

    choice_player1 = input("Enter number to select card: ")
    if getHelp(choice_player1):
        choice_player1 = input("Enter number to select card: ")
    card_player1 = crazyEight(player1.hand[int(choice_player1)])
    while not card_player1.legalMove(discard_pile) and player1_turn:
        another_card_player1 = input("""This is your hand. Choose another card from your
your hand (h) or from the pile (p): """)
        if getHelp(another_card_player1):
            another_card_player1 = input("""This is your hand. Choose another card from your
your hand (h) or from the pile (p): """)
            
        if another_card_player1 == 'h':
            choice_player1 = input("Enter number to select card: ")
            if getHelp(choice_player1):
                choice_player1 = input("Enter number to select card: ")
            card_player1 = crazyEight(player1.hand[int(choice_player1)])
        elif another_card_player1 == 'p':
            if len(deck) != 0:
                player1.hand.append(deck.pop())
                player1.printHand()
                print("Discard pile: ", discard_pile)
                
            else:
                print("Deck is empty")
                player1_turn = False
    if player1_turn and len(player1.hand)!= 0:
        discard_pile = player1.hand.pop(int(choice_player1))
        print("Discard pile: ", discard_pile)

    if len(player1.hand) == 0:
          print(player1.getName(), " has won!")
          break
    
    print()
    print("---------------------------------")
    print(f"It is {player2.getName()}'s turn.", end = "")
    player2.printHand()
    print("Discard pile: ", discard_pile)

    choice_player2 = input("Enter number to select card: ")
    if getHelp(choice_player2):
        choice_player2 = input("Enter number to select card: ")
    card_player2 = crazyEight(player2.hand[int(choice_player2)])
    while not card_player2.legalMove(discard_pile) and player2_turn:
        another_card_player2 = input("""This is your hand. Choose another card from your
your hand (h) or from the pile (p): """)
        if getHelp(another_card_player2):
            another_card_player2 = input("""This is your hand. Choose another card from your
your hand (h) or from the pile (p): """)
        if another_card_player2 == 'h':
            choice_player2 = input("Enter number to select card: ")
            if getHelp(choice_player2):
                choice_player2 = input("Enter number to select card: ")
            card_player2 = crazyEight(player2.hand[int(choice_player2)])
        elif another_card_player2 == 'p':
            if len(deck) != 0:
                player2.hand.append(deck.pop())
                player2.printHand()
                print("Discard pile: ", discard_pile)
            else:
                player2_turn = False
    if player2_turn and len(player2.hand) != 0:
        discard_pile = player2.hand.pop(int(choice_player2))
        print("Discard pile: ", discard_pile)

    if len(player2.hand) == 0:
          print(player2.getName(), "has won!")
          break

    # If both players can not get new cards from the pile and cannot play
    # the card at the top of the discard pile, determine winner from the
    # function defined above.
    if len(deck) == 0 and winner(player1.hand, player2.hand, discard_pile):
        if len(player1.hand) > len(player2.hand):
            print(player2.getName(), " has won.")
        elif len(player1.hand) < len(player2.hand):
            print(player1.getName(), " has won.")
        else:
            print("It is a draw.")


