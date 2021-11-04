
# Instructions
# Part 1 : Quizz :
# Answer the following questions

# What is a class?

#A class is a blueprint to create objects; it defines what properties(attributes) and behaviors(methods) the object created from it will have
#Classes are used to model real world objects and to organize related code - data and functions into a single and coherent place in the code
#Classes are an integral key in the OOP method of programming

# What is an instance?
#An instance is the result of a call to a Class - like ClassName() - you then instantiate the class and receive an object with the attrs and methods
#defined by the blueprint - the class. there can be many instances of one class. each can have different properties/attributes - with similar methods
#that can do different things because they can act based on different attributes

# What is encapsulation?
#encapsulation is a concept in oop, it comes from 'capsule' its means "encapsulating" everything that is related in the code -
# data (as attributes) and functions behaviors (as methods) #and putting it all together and not let it wander around the code,
# by that you also increase readability and coherency

# What is abstraction?
#Abstraction is a concept in oop, is one of the pillars of oop, it means abstractify and making the access to an
#object simpler and hiding the unnecessary details#from the "code users", they dont need to know Dog().talk() works,
#  they only need to have the class and the  method talk exposed (to have the interface with the class)
#and to receive the result "promised" by the class methods

# What is inheritance?
#inheritance is a concept in oop, it lets a class receive the properties and behaviors in a parent class,
#for example a Truck class can inherit from a parent class Vehicle - since a truck is a vehicle (but not every vehicle is a truck),
#  and the Truck then can use the Vehicle class Drive() method by that we can reduce code and organize classes more logically,
# since drive method isnt needed to be declared twice, #  it can work also on the truck=Truck(Vehicle) and truck.Drive() will
# activate its parent class Drive method  but will be based on the truck props like truck.speed(self.speed inside the Truck class)

# What is multiple inheritance?
#multiple inheritance is a feature available in Python (and not in some other langs because it can make the code tricky),
#  it lets a class inherit from more than one class.
#the class will receive the props and the methods from the multiple parent classes and not only one

# What is polymorphism?
#polymorphism means in many shapes, in practice its a concept in oop, it let's the user call a method, this method can be implemented differently
# - overrided - in different subclasses, but it is still available in all of them all the same
#for example Animal can have Talk method, Bear and Dog will be subclasses of Animal and they can both implement a Talk method of their own
#and you can call Bear().talk() and Dog.talk() and the first one can return 'ahhhhh' and the second can return 'woof
#And a Cat might not implement its own method of Talk and if you call Cat().Talk() it can use it's parent (Animal) Talk() method
#in TLDR; it can be said polymorphism is about  different implementation
# of a parent(/base) class's function (method) in a subclass(/child class that inherits from it),

# What is method resolution order or MRO?
#Mro is a method of ordering what class a subclass will inherit from first in a case of multiple inheritance,
# it is need to figure out what method or attribute to use
#like if class D(B,C) the mro can be [class D, class B, class C] so if you call D.some_method() it will
# first look if D has some_method if it does it wil call it
#if not it will search on B then on C (same for looking for  attributes)



# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.