# A command-line blackjack game, a.k.a 21.

import itertools
import random
import time
import argparse

parser = argparse.ArgumentParser(description='Welcome to BlackJack')
parser.add_argument('stake', metavar='stake', type=int, help='Please enter the number of chips you want to buy!')
parser.add_argument('decks', metavar='decks', type=int, help='Provide the number of decks of cards.')
args =  parser.parse_args()
stake = args.stake
decks = args.decks


class Deck:
    """
    Clasa Spil definise karte. Mapira svaki znak sa brojem i stihom.
    Vraca broj karata na osnovu spil parametra u fill metodi. 
    Use case:
    - 6 decks imace 312 karata -> 13nums * 4 suits * [num of decks]
    Mesa ih i broji
    
    """
    suits = ["Diamonds", "Spades", "Clubs", "Hearts"] # definisemo znake
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"] # definisemo karte

    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)
    
    def fill(self, decks):
        for i in range(decks):
            for suit, value in itertools.product(self.suits, self.values):
                self.cards.append(Card(suit, value))

    def clear(self):
        self.cards = []

    def shuffle(self):
        random.shuffle(self.cards)

class Card:
    """
    Prikazuje izvucenu kartu i definise vrednosti poena svake karte.
    """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value 

    def __str__(self):
        return f'{self.value} of {self.suit}'
    
    @property
    def score(self):
        """
        U 21 - jacks, queens i kings vrede 10 poena. Cita vrednosti sa karte
        return: int values
        """
        if self.value in ["Jack", "Queen", "King"]:
            return 10
        if self.value == "Ace":
            return 1
        else:
            return int(self.value)
        
class Player:
    """
    Prikazuje vrednost karta igraca(krajnjeg usera). Broji keceve, sabira score na osnovu vrednosti karata.
    """
    def __init__(self):
        self.hand = []

    def getHand(self):
        print("\t\t\t The player's hand:")
        for card in self.hand:
            print(card)
            print("")
        print("")

    def resetHand(self):
        self.hand = []
    
    @property
    def aces(self):
        """
        broj asova po jednoj ruci (lenght)
        return: int
        """
        return len([card for card in self.hand if card.value == "Ace"])
    
    @property
    def score(self):
        """
        Transformisacemo metodu da bismo mogli da joj pristupamo kao atribut.
        sum hand pozivajuci score metodu iz card klase
        return: int
        """
        return sum([card.score for card in self.hand])
    
    @property
    def score_aces(self):
        """
        Jer, onoliko asova koliko korisnik dobije po jednoj ruci
        ako je taj rezultat (koji se izracunava rezultatom f-ja) manji od 12
        dodaj 10 na to
        Slučaj upotrebe: 
        - Imaš 1 asa. Od toga je duzina 1. Dodajte da je 1 na 10 = 11
        - Imaš 2 asa. Od toga je duzina 2. Dodajte to 2 na 10 = 12. 
        To znaci da jedan as vredi 1 poen, dok drugi vredi 11 poena.
        return: int
        """
        for ace in range(self.aces):
            if self.score < 12:
                self.score += 10
        return self.score
    @property
    def isBusted(self):
        """
        Cilj nije da se prebaci 21. To je ono sto se proverava
        return: bool
        """
        if self.score_aces > 21:
            return True
        return False


class Gambler(Player):
    """
    Svaki igrac je Kockar. Bilo da je user ili diler.
    Ova klasa definise visinu uloga koji je na raspolaganju od strane class object-a kjio ga inicijalizuje i 
    pita kranjeg usera sa koliko ulazi  u igru.
    """

    def __init__(self, chips):
        super().__init__()
        self.chips = chips

    def bet(self):
        """
        Oduzima chipove od ukupnog amounta
        
        """
        stake = input(f"Total chips: {self.chips}. Enter the stake amount:")
        try:
            if int(stake) > self.chips:
                print("You cannot bet that amount")
                self.bet()
            else:
                self.chips -= int(stake)
        except ValueError:
            print("Please enter a valid integer.")
            self.bet()

class Dealer(Player):
    """
    Pokazuje ruku racunara, pozivajuci sve metode (sum score) Player klase
    
    """

    def __init__(self):
        super().__init__()
        self.hand = []

    def show(self, all = False):
        print("\t\t\t The dealer has:")
        if all:
            for card in self.hand:
                print(card)
        else:
            print(self.hand[0])
            print("And God knows what else :)")

class BlackJack:

    """
    Definise:
    - dva igraca
    - broj spilova 
    - broj chipova na raspolaganju
    Proverava izbore, bustove. Definise izgubljene/dobijene i neresene partije.
    """
    
    def __init__(self):
        self.players = [] # namenjena da sadrži instancirane objekte tipa Player
        self.deck = []
        self.player_bet = 0
        self.player_turn =  True

    def deal(self):
        """
        Za use case da su ostala/definisana manje od 2 spila"""
        print(f"There are {len(self.deck)} cards are left in the deck.")
        if len(self.deck) < 104:
            print("Re-shuffling...")
            self.deck.clear()
            self.deck.fill(6)
            self.deck.shuffle()

        for i in range(2):
            for player in self.players:
                player.hand.append(self.deck.cards.pop()) # pristupamo hand listi po prosledjenoj player instanci

        
    def hit(self, player):
        player.hand.append(self.deck.cards.pop())
        if isinstance(player, Dealer):
            player.show(True) # uvek prikazi 1 kartu
        else:
            player.getHand()
        self.checkBust(player)
        print(f"Player score: {player.score_aces}")

    def player_choice(self, player):
        answer = input("You're gonna hit or stick? (H/S):")
        if answer.lower() == "h":
            self.hit(player) # dodaj novu kartu u ruku igraca
        elif answer.lower() == "s":
            print(f"You choose to stick with your {player.score_aces} ")
            self.player_turn = False


    def checkBust(self, player):
        """
        Proverava se koji je igrac u pitanju
        """
        if player.isBusted:
            if (isinstance(player, Gambler)):
                print("You've been busted! ")
                self.player_turn = False
                self.playerlost(player)
            if (isinstance(player, Dealer)):
                print("Dealer is busted. You won!")
    
    def playerlost(self, player):
        """
        Od chip amounta oduzmi ulog
        """
        print("You've lost!")
        player.chips -= self.player_bet

    def draw(self, player):
        """
        Vrati mu taj iznos uloga na racun koje si mu uzeo na pocetku
        """
        print(f"It is a draw. Please get your {self.player_bet} back")
        player.chips += self.player_bet

    def player_won(self, player):
        """ 
        Dupliraj mu ulog i dodaj na racun
        """
        reward = self.player_bet * 2
        print(f"You got this. Please get your {reward} as a reward")
        player.chips += self.player_bet * 2


    def compare(self, player, dealer):
        if player.score_aces > dealer.score_aces:
            self.player_won(player)
        elif player.score_aces == dealer.score_aces:
            self.draw(player)
        else:
            self.playerlost(player)
    
    def reset(self):
        for player in self.players:
            player.resetHand()
        self.player_bet = 0

    def replay(self, player):
        again = None
        while again != "y" or again != "n":
            again = input("Play again? Y/N: ")
            if again.__eq__("y"):
                return True
            elif again.__eq__("n"):
                print(f"You walk away with {player.chips} chips")
                return False
            else:
                print("Invalid input. Try again.")
    
    def play(self):
        print("This is BlackJack")
        self.deck =  Deck()
        player = Gambler(stake) # definisemo chipove na raspolaganju
        dealer = Dealer()
        self.players = [player, dealer] # objekti instance Gambler i Dealer klasa
        self.deck.fill(decks) # broj spilova
        self.deck.shuffle()
        running = True
        """
        Pokrece se igra. 
        Odigra Player i ponisti mu se sledeci potez, na redu je dealer. Dok god Igrac nije bust-ovan i nije on na potezu"""

        while running:
            if self.players[0].chips == 0:
                print("You're broke. Get out!")
                break
            self.player_bet = player.bet()
            self.deal()
            dealer.show()
            player.getHand()
            while self.player_turn:
                self.player_choice(player)
            if not player.isBusted:
                dealer.show()
                while not self.player_turn:
                    if dealer.score_aces < 17:
                        # Ako dilerov zbir karata (score) bude manji od 17, on mora uzeti jos jednu kartu (hit)
                        print("Dealer hits")
                        self.hit(dealer)
                        time.sleep(2)
                    elif dealer.score_aces >= 17 and not dealer.isBusted:
                        # A ako dilerov zbir karata bude 17 ili vise, on mora stati (stand), odnosno ne uzima vise karata.
                        print(f"Dealer stick with its hands of {dealer.score_aces}")
                        break
                    elif dealer.isBusted:
                        self.player_won(player)
                        break

                if not dealer.isBusted:
                    """Ako posle prve iteracije pitanja o S ili H ni Dealer ni player nisu bustovani, provera stanja i proglasi rezultat partije"""
                    self.compare(player=player, dealer=dealer)
            again = self.replay(player)
            if not again:
                running = False
            # ako se igra ponovo Player je prvi na potezu
            self.player_turn = True
            self.reset()


def main():
    bj = BlackJack()
    bj.play()

if __name__ == '__main__':
    main()


                        



        











