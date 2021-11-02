
# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

# Write a program which prints the results of the following python built-in functions: 
# abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the
#  execution of your code. Take a look at the doc method on google for help.

print('\n\nExercise 1')

# print(abs(-4))
# print(int('1'))
# print(input("Please enter input"))

from abc import get_cache_token
import math

class Absolutizer():
    """
    This is a class for returning the Absolute Value of a number
    ...

    Attributes
    ----------
    number : int
        a number inputted by the user


    Methods
    -------
    __abs__()
        Returns the absolute value of the number attr
    """

    def __init__(self):
        while True:
            user_num_input = input("Please enter a number: ")
            try:
                user_num = int(user_num_input)
                break
            except:
                print("Please enter a number")
        self.number = user_num
        print("user num is ", self.number)


    def __abs__(self):
        """Returns the absolute value of the number attr"""
        num = self.number
        return num if num >=0 else num * -1

    __abs__.__doc__ = "A really cool method - Returns the absolute value of the number attr"

    def new_input(self):
        """Asks the user to input another number - overwrites current number attr"""
        while True:
            print(f"You entered {(user_num_input := input('Please enter another number: '))}")
            try:
                user_num = int(user_num_input)
                self.number = user_num
                break
            except:
                print("Bad input, try again...")

# absolutizer_1 = Absolutizer()
# print(abs(absolutizer_1))
# absolutizer_1.new_input()

print(Absolutizer.__doc__)
print(Absolutizer.__abs__.__doc__)
print(Absolutizer.new_input.__doc__)


Absolutizer.__abs__.__doc__= "A really very cool method"
print(Absolutizer.__abs__.__doc__)



# Exercise 2: Currencies
# Instructions
# Create the code which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c3 = Currency('shekel', 1)
# >>> c4 = Currency('shekel', 10)
print('\n\nExercise 2')


class CurrencyMixError(TypeError):
    '''Raise when my operation is made on Currencies with different Labels'''

class Currency:
    """
    A class to represent a currency
    """

    def __init__(self, label, amount) -> None:
        self.label = label
        self.amount = amount

    @staticmethod
    def get_currency_amount(other):
            if type(other) is int:
                return other
            if type(other) is Currency:
                return other.amount

    @classmethod
    def get_add_allowed_types(cls):
        allowed_types = [int,Currency]
        return allowed_types


    def __add__(self,other):
        try:
            if not type(other) in self.get_add_allowed_types():
                raise TypeError(f"Type not supported for add")
            elif type(other) == Currency and other.label != self.label:
                raise CurrencyMixError(f"Cannot add between Currency type <{self.label}> and <{other.label}>")
            else:
                other_amount = self.get_currency_amount(other)
                return self.amount + other_amount
        except CurrencyMixError:
            print("Error! You entered Currencies of different labels")
            return self.amount
        except TypeError:
            print(f"Error! Please enter correct types: {''.join( str(self.get_add_allowed_types()) ) }")
            return self.amount

    def __iadd__(self,other):
        self.amount  = self+other
        return self

    def __str__(self) -> str:
        return self.__repr__()
        
    def __repr__(self) -> str:
        return f"{self.amount} {self.label+'s' if self.amount != 1 else self.label}"

    def __int__(self) -> int:
        return self.amount


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
c1+=c3

c4 += c3
c3+= c4
print(c4)
print(c3)
c5 = c1+c2
print(c5)
print(c1)
print(c3)
print(int(c3))
print(repr(c1))
c1+5

c7= c2+c3
print(int(c1))
print(repr(c1))
