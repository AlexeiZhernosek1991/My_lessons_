"""Game BLACK JACK"""


class Player:  # New class to implement the players
    it_card = ''  # Variable for iteration set with card
    set_card = {
        '2 Spades', '3 Spades', '4 Spades', '5 Spades', '6 Spades', '7 Spades', '8 Spades', '9 Spades', '10 Spades',
        'J Spades', 'Q Spades', 'K Spades', 'A Spades', '2 Clubs', '3 Clubs', '4 Clubs', '5 Clubs', '6 Clubs',
        '7 Clubs', '8 Clubs', '9 Clubs', '10 Clubs', 'J Clubs', 'Q Clubs', 'K Clubs', 'A Clubs',
        '2 Hearts', '3 Hearts', '4 Hearts', '5 Hearts', '6 Hearts', '7 Hearts', '8 Hearts', '9 Hearts', '10 Hearts',
        'J Hearts', 'Q Hearts', 'K Hearts', 'A Hearts', '2 Diamonds', '3 Diamonds', '4 Diamonds', '5 Diamonds',
        '6 Diamonds', '7 Diamonds', '8 Diamonds', '9 Diamonds', '10 Diamonds', 'J Diamonds', 'Q Diamonds', 'K Diamonds',
        'A Diamonds'
    }  # Set with cards for generation list cards
    dict_card = {
        '2 Spades': 2, '3 Spades': 3, '4 Spades': 4, '5 Spades': 5, '6 Spades': 6, '7 Spades': 7, '8 Spades': 8,
        '9 Spades': 9, '10 Spades': 10, 'J Spades': 10, 'Q Spades': 10, 'K Spades': 10, 'A Spades': 11, '2 Clubs': 2,
        '3 Clubs': 3, '4 Clubs': 4, '5 Clubs': 5, '6 Clubs': 6, '7 Clubs': 7, '8 Clubs': 8, '9 Clubs': 9,
        '10 Clubs': 10, 'J Clubs': 10, 'Q Clubs': 10, 'K Clubs': 10, 'A Clubs': 11, '2 Hearts': 2, '3 Hearts': 3,
        '4 Hearts': 4, '5 Hearts': 5, '6 Hearts': 6, '7 Hearts': 7, '8 Hearts': 8, '9 Hearts': 9, '10 Hearts': 10,
        'J Hearts': 10, 'Q Hearts': 10, 'K Hearts': 10, 'A Hearts': 11, '2 Diamonds': 2, '3 Diamonds': 3,
        '4 Diamonds': 4, '5 Diamonds': 5, '6 Diamonds': 6, '7 Diamonds': 7, '8 Diamonds': 8, '9 Diamonds': 9,
        '10 Diamonds': 10, 'J Diamonds': 10, 'Q Diamonds': 10, 'K Diamonds': 10, 'A Diamonds': 11
    }  # Dict for counting card combinations

    @classmethod
    def __iter__(cls):  # Method for iteration set with card
        cls.it_card = iter(Player.set_card)

    def __init__(self, name):  # Method for variable definitions name and result
        self.name = name  # Variable name class object
        self.result = 0  # Variable the result of a combination of cards

    def dealing(self):  # Method for passing values from a list one by one
        try:
            card = next(self.it_card)  # The function returns the cards from the list one by one
            self.result += Player.dict_card[card]  # Adds the values of the cards in accordance with
            # the dictionary dict_card
            print(card)  # Print card
        except StopIteration:  # Exception handling StopIteration
            print('The deck of cards is over')
            Player.__iter__()  # Method for iteration set with card when # Method for iteration set with card


def playing(player1: Player, player2: Player):  # The method of determining victory
    if 22 > player1.result > player2.result or player2.result > 21 and player1.result < 22:
        print(f'{player1.name} is WINNER!!!!')  # Victory condition player1
    elif 22 > player2.result > player1.result or player1.result > 21 and player2.result < 22:
        print(f'{player2.name} is WINNER!!!!')  # Victory condition player2
    elif player1.result > 21 and player2.result > 21:  # The condition for going beyond the maximum value
        print('too mach')
    elif player1.result == player2.result:  # Draw condition
        print('Draw')


def play_computer(player2: Player):  # Function for computer logic
    player2.dealing()  # Calling a function that returns a single card
    player2.dealing()  # Calling a function that returns a single card
    while player2.result <= 16:  # If the variable values result are less than 16 calls the function dealing
        player2.dealing()


def play_user(player1: Player):  # Function for user logic
    player1.dealing()  # Calling a function that returns a single card
    player1.dealing()  # Calling a function that returns a single card
    print(player1.result)  # Output of the result of a combination of cards
    while True:  # Cycle for the opportunity to take another card
        play = input('Do you want another one card print "y" - yes or "n" - not >>> ')
        if play == 'n':  # Exit condition of the cycle
            break
        elif play == 'y':
            player1.dealing()  # Calling a function that returns a single card
            print(player1.result)  # Output of the result of a combination of cards
            if player1.result >= 21:  # If the card combination has a value above 21 exit the cycle
                break
            else:
                pass
        else:  # Incorrect value entered
            print('you entered the wrong value')


def main():  # The main function of the game
    print('Greetings my Friend!!!')
    player_1 = Player(input('What is you name >>>'))  # Creates a class object Player for the player
    player_2 = Player('Computer')  # Creates a class object Player for the computer
    print(f"Hellow {player_1.name}! We are glad to see you. Let's start the game")
    Player.__iter__()  # Method for iteration set with card (desk card)
    while True:  # Cycle for gameplay
        play = input("let's play? print 'y' - yes or 'n' if not >>>  ")  # Enter a value for the gameplay
        if play == 'n':  # Condition for exiting the cycle
            break
        elif play == 'y':
            play_computer(player_2)  # The computer is playing
            play_user(player_1)  # The user is playing
            playing(player_1, player_2)  # Determining the winner
            player_1.result = 0  # Zeroing the game variable user
            player_2.result = 0  # Zeroing the game variable computer
        else:  # Condition for entering an invalid variable
            print('you entered the wrong value')
    print(f'Thank you {player_1.name} for game!See you...')


"""Start Game"""
main()
