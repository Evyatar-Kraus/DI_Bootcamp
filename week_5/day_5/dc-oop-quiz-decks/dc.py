
# Instructions
# Part 1 : Quizz :
# Answer the following questions

# What is a class?

# A class is a blueprint to create objects; it defines what properties(attributes) and behaviors(methods) the object created from it will have
# Classes are used to model real world objects and to organize related code - data and functions into a single and coherent place in the code
# Classes are an integral key in the OOP method of programming

# What is an instance?
# An instance is the result of a call to a Class - like ClassName() - you then instantiate the class and receive an object with the attrs and methods
# defined by the blueprint - the class. there can be many instances of one class. each can have different properties/attributes - with similar methods
# that can do different things because they can act based on different attributes

# What is encapsulation?
# encapsulation is a concept in oop, it comes from 'capsule' its means "encapsulating" everything that is related in the code -
# data (as attributes) and functions behaviors (as methods) #and putting it all together and not let it wander around the code,
# by that you also increase readability and coherency

# What is abstraction?
# Abstraction is a concept in oop, is one of the pillars of oop, it means abstractify and making the access to an
# object simpler and hiding the unnecessary details#from the "code users", they dont need to know Dog().talk() works,
#  they only need to have the class and the  method talk exposed (to have the interface with the class)
# and to receive the result "promised" by the class methods

# What is inheritance?
# inheritance is a concept in oop, it lets a class receive the properties and behaviors in a parent class,
# for example a Truck class can inherit from a parent class Vehicle - since a truck is a vehicle (but not every vehicle is a truck),
#  and the Truck then can use the Vehicle class Drive() method by that we can reduce code and organize classes more logically,
# since drive method isnt needed to be declared twice, #  it can work also on the truck=Truck(Vehicle) and truck.Drive() will
# activate its parent class Drive method  but will be based on the truck props like truck.speed(self.speed inside the Truck class)

# What is multiple inheritance?
# multiple inheritance is a feature available in Python (and not in some other langs because it can make the code tricky),
#  it lets a class inherit from more than one class.
# the class will receive the props and the methods from the multiple parent classes and not only one

# What is polymorphism?
# polymorphism means in many shapes, in practice its a concept in oop, it let's the user call a method, this method can be implemented differently
# - overrided - in different subclasses, but it is still available in all of them all the same
# for example Animal can have Talk method, Bear and Dog will be subclasses of Animal and they can both implement a Talk method of their own
# and you can call Bear().talk() and Dog.talk() and the first one can return 'ahhhhh' and the second can return 'woof
# And a Cat might not implement its own method of Talk and if you call Cat().Talk() it can use it's parent (Animal) Talk() method
# in TLDR; it can be said polymorphism is about  different implementation
# of a parent(/base) class's function (method) in a subclass(/child class that inherits from it),

# What is method resolution order or MRO?
# Mro is a method of ordering what class a subclass will inherit from first in a case of multiple inheritance,
# it is need to figure out what method or attribute to use
# like if class D(B,C) the mro can be [class D, class B, class C] so if you call D.some_method() it will
# first look if D has some_method if it does it wil call it
# if not it will search on B then on C (same for looking for  attributes)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should inherit from a Card class.

# The requirements are as follows:
import random
from constants import RANKS, SUITS


# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
class Card:
    def __init__(self, suit, value) -> None:
        self.__suit = suit
        self.__value = value

    @property
    def suit(self):
        return self.__suit

    @property
    def value(self):
        return self.__value

    def __str__(self) -> str:
        tuple_string = str((self.value, self.suit))
        return tuple_string

    def __iter__(self):
        for val in (self.value, self.suit):
            yield val

    #for the equality purposes - so we can use set on a list of Cards
    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    #for comparison purposes (here set on list of Cards);
    #it computes a hash value for an object, since equal objects must have equal hashes
    def __hash__(self) -> int:
        return hash(('suit', self.value,
                     'value', self.suit))




# The Deck class :

class Deck(Card):

    @staticmethod
    def fix_deck(cards):
        return list(set(cards))

    def __init__(self, cards) -> None:
        self.__cards = self.fix_deck(cards)

    @property
    def cards(self):
        return self.__cards

    def get_card_tuple_list(self):
        card_list = [(card.value, card.suit) for card in self.cards]
        return card_list

    @cards.setter
    def cards(self,new_cards):
        self.__cards = self.fix_deck(new_cards)

    def check_deck(self):
        cards = self.cards
        if len(set(cards)) != 52:
            raise ValueError

    # should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
    def shuffle(self):
        try:
            self.check_deck()
            random.shuffle(self.__cards)
        except ValueError:
            print("bad deck, i cant shuffle this!")

    # should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
    def deal(self):
        cards_in_deck_count = len(self.cards)
        if cards_in_deck_count:
            random_card = random.choice(self.cards)
            res = self.cards.remove(random_card)
            print(f"dealing card {random_card}")
            return random_card
        else:
            print("deck is empty, can't deal anymore cards")
            return None

    def __str__(self) -> str:
        return '[' + ','.join([str(card) for card in self.cards]) + ']'

    def __len__(self):
        return len(self.__cards)

    def __iter__(self):
        for card in self.cards:
            yield (card.value, card.suit)



h5 = Card('5', 'Hearts')
h4 = Card('4', 'Hearts')
h5_2 = Card('5', 'Hearts')
unique_cards = set([h4, h5, h5_2])
unique_suits = set([h4.suit, h5.suit, h5_2.suit])

cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
cards.append(Card('5', 'Hearts'))
print("length of cards list after appending a 53th card before using it in Deck Class")
print(len(cards))

deck = Deck(cards)
print(deck.cards)
print("Deck","\n",deck)
print('\n\nlen of the Deck class after instantiating it with cards list - it has 53 cards','\n',
    'but it will make sure it will be valid using set so it will have 52')
print(len(deck))
print('first card in deck:',deck.cards[0])

print("\nafter shuffle")
deck.shuffle()
print('first card in deck:',deck.cards[0])
print(len(deck))

print(deck)
print(len(deck.cards))

print("\ncard tuple list")
print(deck.get_card_tuple_list())

print("\ndealing cards")
# deck.deal()
for card in range(0,len(deck)):
    print(len(deck.cards))
    deck.deal()

print("\nlen of deck:",len(deck))
deck.deal()
print("\nlen of deck:",len(deck))
deck.deal()
