# Exercise 1 : Pets
# Instructions
# Using this code:
print("\n\nExercise 1")

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sphinx(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# bengal_cat = Bengal('mia-a-hu')
# chartreux_cat = Chartreux('mwuuuu')
# sphinx_cat = Sphinx('muusususus')

bengal_cat = Bengal('bengie',3)
chartreux_cat = Chartreux('chichi',4)
sphinx_cat = Sphinx('sifu',5)

my_cats = [bengal_cat,chartreux_cat,sphinx_cat]
my_pets = Pets(my_cats)
my_pets.walk()

# Create another cat bread. In order to do so, create a class which inherits from the Cat class.
# Create a few cat instances.
# Create a list called my_cats, which will hold all the created cat instances.
# Create a variable called my_pets. It’s value is an instance of the Pet class.
# Hint : Use the my_cats variable to create the instance.
# Take all the cats for a walk, use the walk method.


# Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value should be another dog called other_dog,
#  returns a string stating which dog won the fight. 
# The winner should be the dog with the higher run_speed x weight.
# Create 3 dogs and run them through your class.
print("\n\nExercise 2")

class Dog():
    def __init__(self,name,age,weight):
        self.name, self.age, self.weight = name,age,weight

    def bark(self):
        return f"{self.name} is barking!"

    def run_speed(self):
        return (self.weight / (self.age * 10))

    def fight(self, other_dog):
        return \
            self.name \
            if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight\
            else other_dog.name
    
dog1 = Dog("Sunny",3,11)
dog2 = Dog("Moony",4,10)
dog3 = Dog("Snowy",1,15)

my_dogs = [dog1,dog2,dog3]
[print(dog.bark()) for dog in my_dogs]
[print(f"{dog.name}'s running speed is {dog.run_speed()}") for dog in my_dogs]

#this makes zip on the my_dogs and the my_dogs without the first element
#so after they become tuples in zip its : [(1stDog,2ndDog),(2ndDog,3rdDog)]
#and then you can use fight in list comprehension
print("\n")
list_of_tuples_1st2nd_dogs_and_2nd3rd_dogs = list(zip(my_dogs,my_dogs[1:])) 
print('\n'.join([f"In the fight between {dog[0].name} and {dog[1].name} - the winner is {dog[0].fight(dog[1])}" for dog in list_of_tuples_1st2nd_dogs_and_2nd3rd_dogs]))


# Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean
#and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True
print("\n\nExercise 3")

import dog as ImportedDogFile
import random 

class PetDog(ImportedDogFile.Dog):

    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *args):
        print(self.name+',', ', '.join([*args]), 'all play together')

    def do_a_trick(self):
        if self.trained:
            trick = random.choice([
            f"{self.name} does a barrel roll",
            f"{self.name} stands on his back legs",
            f"{self.name} shakes your hand",
            f"{self.name} plays dead"
            ])

            print(trick)
            return trick


# play: takes a parameter which value is a few names of
#  other dogs (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.


johnny = PetDog('Johny',2,10,False)
print(johnny.trained)
johnny.play("Rex",'Simor','Jendny')
johnny.train()
print(johnny.trained)
johnny.do_a_trick()
johnny.do_a_trick()
johnny.do_a_trick()


