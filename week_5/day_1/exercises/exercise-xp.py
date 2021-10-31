
# What You Will Learn
# Classes and Objects


# Exercise 1: Cats
# Instructions
# Using this class

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
from pprint import pprint
pprint("Exercise 1")
class Cat:
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Hello I am {self.name} and I'm {self.age} years old."

# cat1 = Cat("Michi" ,1)
# cat2 = Cat("Spin",4)
# cat3 = Cat("Shusi", 5)
# cats = [cat1,cat2,cat3]

cat_data_list = [("Michi" ,1),("Spin",6),("Shusi", 5)]
cats = [Cat(*data) for data in cat_data_list] # instantiate multiple objs with this list comprehension expressions
get_oldest_cat = lambda cat_list : sorted(cats,key = lambda cat: cat.age, reverse=True)[0]

oldest_cat = get_oldest_cat(cats)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old")

# Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This
#  function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
pprint("Exercise 2")


class Dog:
    def __init__(self,name,height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

    def __str__(self):
        return f"I am a dog named {self.name} and I am {self.height} cms tall!"

davids_dog = Dog("Rex",50)
print(davids_dog.name)
print(davids_dog.height)
print(davids_dog)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog(name="Teacup",height=20)
print(sarahs_dog.name)
print(sarahs_dog.height)
print(sarahs_dog)
sarahs_dog.bark()
sarahs_dog.jump()

print(sarahs_dog.name if sarahs_dog.height > davids_dog.height else davids_dog.name)

# Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# Then, call the sing_me_a_song method. The output should be:
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven
pprint("Exercise 3")

class Song:
    def __init__(self,lyrics = []):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line, end = "\n")

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds 
# the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method 
# removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups
#  them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)
print("Exercise 4", end="\n\n\n")

class Zoo:
    def __init__(self, zoo_name) -> None:
        self.animals = []
        self.name= zoo_name

    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("These are the animals currently at the zoo:", end ='\n')
        animal_list = ''
        for animal in self.animals:
            animal_list =  animal_list + animal + '\n'
        return animal_list
        
    def sell_animal(self, sold_animal):
        if sold_animal in self.animals:
            self.animals.remove(sold_animal)
    
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        if len(sorted_animals):
            animal_dict = {}
            current_key = 1
            last_letter = 'A'
            for animal in sorted_animals:
                current_letter = animal[0]
                if last_letter < current_letter:
                    last_letter = current_letter
                    if current_key in animal_dict:
                        current_key += 1
                if current_key in animal_dict:
                    if type(animal_dict[current_key]) == list:
                        animal_dict[current_key].append(animal)
                    else:
                        animal_dict[current_key] = [animal_dict[current_key]]
                        animal_dict[current_key].append(animal)
                else:
                    animal_dict[current_key] = animal

            return animal_dict

        else:
            return "no animals to sort!"

    def get_groups(self):
            print("These are the zoo's animals groupd alphabetically:")
            animal_dict = self.sort_animals()
            for letter_idx in animal_dict:
                item = animal_dict[letter_idx]
                if type(item) == list:
                    letter = item[0][0]
                else:
                    letter = item[0]
                print(letter+': ', end='')
                print(animal_dict[letter_idx])

    def __repr__(self) -> str:
        return f"This is the {self.name} and we currently have these animals:\n{self.get_animals()}"

ramat_gan_safari = Zoo("Ramat Gan Safari")
# ramat_gan_safari.add_animal("Girrafe")
# ramat_gan_safari.add_animal("Elephant")
# ramat_gan_safari.add_animal("Emu")
# ramat_gan_safari.add_animal("Dingo Dog")
# ramat_gan_safari.add_animal("Desert Cat")
# ramat_gan_safari.add_animal("Dinosaur")

animals_to_add_to_zoo = ['Girrafe','Elephant','Emu','Dingo Dog','Desert Cat','Dinosaur']
for animal in animals_to_add_to_zoo:
    ramat_gan_safari.add_animal(animal)


print(ramat_gan_safari.get_animals())
pprint(ramat_gan_safari)
ramat_gan_safari.sell_animal("Dingo Dog")
pprint(ramat_gan_safari)

ramat_gan_safari.get_groups()
ramat_gan_safari.add_animal('Ganu')
ramat_gan_safari.get_groups()
ramat_gan_safari.sell_animal('Elephant')
ramat_gan_safari.get_groups()
