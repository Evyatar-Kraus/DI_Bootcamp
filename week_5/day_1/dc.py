# Daily Challenge: Old MacDonald’s Farm
# Last updated : May 2nd 2021


# What You Will Learn :
# Classes and Objects


# Instructions : Old MacDonald’s Farm
# Take a look at the following code and output!
# File: market.py

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


# Create the code that is needed to recreate the code provided above. Below are 
# a few questions to assist you with your code:
# 1. Create a class called Farm. How should this be implemented?


class Farm:
    def __init__(self,farm_name):
        self.name = farm_name
        self.animals_dict = {}
    
    def add_animal(self,animal, count = 1):
        if animal in self.animals_dict:
            self.animals_dict[animal] += count
        else:
            self.animals_dict[animal] = count

    def get_info(self):
        info = f"\n{self.name}'s Farm\n\n"
        for animal in self.animals_dict:
            info+=f"{animal} {self.animals_dict[animal]}\n"
        info+="\nE-I-E-I-0!\n"
        return info

    def get_animal_types(self):
        return sorted(self.animals_dict.keys())


    animal_plural_form_dict = {
        "sheep": "sheep",
        "ox": "oxen",
        "goose": "geese"

    }
    def get_animal_plural_form(self,animal_singular):
        if animal_singular in self.animal_plural_form_dict:
            return self.animal_plural_form_dict[animal_singular]
        else:
            return animal_singular+'s'

    def get_short_info(self):
        animals = self.get_animal_types()
        short_info = f"{self.name}'s farm has "
        for idx,animal in enumerate(animals):
            animal_count = self.animals_dict[animal]
            animal_name = animal if animal_count == 1 else self.get_animal_plural_form(animal)
            if len(animals) == 1:
                short_info+=f" {animal_name}s."
                break
            else: 
                if idx+1 == len(animals):
                    short_info+=f"{animal_name}"
                elif idx+2 == len(animals):
                    short_info+=f"{animal_name} and "
                else:
                    short_info+=f"{animal_name}, "
        return short_info

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('goose')
macdonald.add_animal('goose')

macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

# 2. Does the Farm class need an __init__ method? If so, what parameters should it take?
#it takes the parameter farm name - because of the -> macdonald = Farm("McDonald") 
# and later it outputs  McDonald's farm

# 3. How many methods does the Farm class need?
# at the minimum 3 -> init, add_animal, and get_info

# 4. Do you notice anything interesting about the way we are calling the add_animal method? 
# What parameters should this function have? How many…?
#it has one mandatory parameter - the animal name and it can have another parameter for count -
# how many of this animal are being added

# 5. Test your code and make sure you get the same results as the example above.

# 6. Bonus: nicely line the text in columns as seen in the example above. Use string formatting.

# Expand The Farm
# Add a method called get_animal_types to the Farm class. This method should return 
# a sorted list of all the animal types (names) in the farm. With the example above, 
# the list should be: ['cow', 'goat', 'sheep'].

# Add another method to the Farm class called get_short_info. This method 
# should return the following string: “McDonald’s farm has cows, goats and 
# sheep.”. The method should call the get_animal_types function to get a list of the animals.

print(macdonald.get_short_info())