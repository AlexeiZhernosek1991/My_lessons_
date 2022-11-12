"""Game BLACK JACK"""


class Player:
    it_card = []
    set_card = {
        '2 Spades', '3 Spades', '4 Spades', '5 Spades', '6 Spades', '7 Spades', '8 Spades', '9 Spades', '10 Spades',
        'J Spades', 'Q Spades', 'K Spades', 'A Spades', '2 Clubs', '3 Clubs', '4 Clubs', '5 Clubs', '6 Clubs',
        '7 Clubs', '8 Clubs', '9 Clubs', '10 Clubs', 'J Clubs', 'Q Clubs', 'K Clubs', 'A Clubs',
        '2 Hearts', '3 Hearts', '4 Hearts', '5 Hearts', '6 Hearts', '7 Hearts', '8 Hearts', '9 Hearts', '10 Hearts',
        'J Hearts', 'Q Hearts', 'K Hearts', 'A Hearts', '2 Diamonds', '3 Diamonds', '4 Diamonds', '5 Diamonds',
        '6 Diamonds', '7 Diamonds', '8 Diamonds', '9 Diamonds', '10 Diamonds', 'J Diamonds', 'Q Diamonds', 'K Diamonds',
        'A Diamonds'
    }
    dict_card = {
        '2 Spades': 2, '3 Spades': 3, '4 Spades': 4, '5 Spades': 5, '6 Spades': 6, '7 Spades': 7, '8 Spades': 8,
        '9 Spades': 9, '10 Spades': 10, 'J Spades': 10, 'Q Spades': 10, 'K Spades': 10, 'A Spades': 11, '2 Clubs': 2,
        '3 Clubs': 3, '4 Clubs': 4, '5 Clubs': 5, '6 Clubs': 6, '7 Clubs': 7, '8 Clubs': 8, '9 Clubs': 9,
        '10 Clubs': 10, 'J Clubs': 10, 'Q Clubs': 10, 'K Clubs': 10, 'A Clubs': 11, '2 Hearts': 2, '3 Hearts': 3,
        '4 Hearts': 4, '5 Hearts': 5, '6 Hearts': 6, '7 Hearts': 7, '8 Hearts': 8, '9 Hearts': 9, '10 Hearts': 10,
        'J Hearts': 10, 'Q Hearts': 10, 'K Hearts': 10, 'A Hearts': 11, '2 Diamonds': 2, '3 Diamonds': 3,
        '4 Diamonds': 4, '5 Diamonds': 5, '6 Diamonds': 6, '7 Diamonds': 7, '8 Diamonds': 8, '9 Diamonds': 9,
        '10 Diamonds': 10, 'J Diamonds': 10, 'Q Diamonds': 10, 'K Diamonds': 10, 'A Diamonds': 11
    }

    @classmethod
    def __iter__(cls):
        cls.it_card = iter(Player.set_card)

    def __init__(self, name):
        self.name = name
        self.result = 0

    def dealing(self):
        try:
            card = next(self.it_card)
            self.result += Player.dict_card[card]
            print(card)
        except StopIteration:
            print('The deck of cards is over')
            Player.__iter__()


def playing(player1: Player, player2: Player):
    if 22 > player1.result > player2.result or player2.result > 21 and player1.result < 22:
        print(f'{player1.name} is WINNER!!!!')
    elif 22 > player2.result > player1.result or player1.result > 21 and player2.result < 22:
        print(f'{player2.name} is WINNER!!!!')
    elif player1.result > 21 and player2.result > 21:
        print('too mach')
    elif player1.result == player2.result:
        print('Draw')


def play_computer(player2: Player):
    player2.dealing()
    player2.dealing()
    while player2.result <= 16:
        player2.dealing()


def play_user(player1: Player):
    player1.dealing()
    player1.dealing()
    print(player1.result)
    while True:
        play = input('Do you want another one card print "y" - yes or "n" - not >>> ')
        if play == 'n':
            break
        elif play == 'y':
            player1.dealing()
            print(player1.result)
            if player1.result >= 21:
                break
            else:
                pass
        else:
            print('you entered the wrong value')


def main():
    print('Greetings my Friend!!!')
    player_1 = Player(input('What is you name >>>'))
    player_2 = Player('Computer')
    print(f"Hellow {player_1.name}! We are glad to see you. Let's start the game")
    Player.__iter__()
    while True:
        play = input("let's play? print 'y' - yes or 'n' if not >>>  ")
        if play == 'n':
            break
        elif play == 'y':
            play_computer(player_2)
            play_user(player_1)
            playing(player_1, player_2)
            player_1.result = 0
            player_2.result = 0
        else:
            print('you entered the wrong value')
    print(f'Thank you {player_1.name} for game!See you...')


"""Start Game"""
main()
