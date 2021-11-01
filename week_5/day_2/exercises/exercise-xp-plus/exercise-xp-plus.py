# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]
# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# a method that prints all the members of the family.

print("\n\nExercise 1")

class Family:
    def __init__(self, last_name, members = []):
        self.last_name = last_name
        self.members = members

    def born(self, **baby):
        new_baby = {}
        for key in baby.keys():
            new_baby[key] = baby[key]
        new_baby.update({'is_child': True})
        new_baby.update({'age': 0})
        self.members.append(new_baby)
        print(f"Congratulations for the birth of {baby.get('name')}")

    def is_18(self,name):
        # person = list(filter (lambda person: person['name'] == name  , self.members))[0] #1st way
        person = next((member for member in self.members if member["name"] == name), None) #2nd way - generator expr
        if not person:
            raise Exception('This family member does not exist!')
        return person['age'] >= 18

    def show_members(self):
        print(f"Welcome! We are the {self.last_name} family!")
        print("Our names are: ")
        for member in self.members:
            print(member['name'])

    def __repr__(self) -> str:
        self.show_members()
        return ''


family_members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]

smith_family = Family("Smith", family_members)
smith_family.show_members()
print(smith_family.is_18('Sarah'))
# print(smith_family.is_18('Sara'))
print(smith_family)
smith_family.born(name='John', gender="Male")
print('\n')
smith_family.show_members() 


# Exercise 2 : The Incredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore we need
#  to add the following keys to our dictionaries: power and incredible_name.

# Add a method called use_power, this method should print the power of a member
#  if they are over 18 years old. If not raise an exception (look up exceptions) which stated
#  they are not over 18 years old.


family_members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False, 'power':'Super Strength', 'incredible_name':'SuperMike'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False, 'power': 'Invisibility', 'incredible_name': 'Amazing Who'}
]

print("\n\nExercise 2")
class TheIncredibles(Family):
    def __init__(self, last_name, members=[]):
        super().__init__(last_name, members=members)

    def use_power(self, name):
        person = next((member for member in self.members if member["name"] == name), None)
        if person:
            if person.get('age') >= 18:
                print(f"{person.get('name')} uses the power of {person.get('power')} ")
            else:
                raise Exception(f"{person.get('name')} is not over 18 years old yet!")
        else:
            raise Exception('This family member does not exist!')

    def incredible_presentation(self):
        self.show_members()
        print("and our powers are:\n")
        for member in self.members:
            self.use_power(member.get('name'))

inc_fam =TheIncredibles("Johnson", family_members)

inc_fam.incredible_presentation()
inc_fam.born(name='John', gender="Male", power="Unknown Power")
inc_fam.incredible_presentation()


# Add a method called incredible_presentation which presents the family
#  members with their incredible names and powers.

# Look up the names of The Incredibles characters on Google and build the family
# (if you can’t find the correct information just improvise).
# Print their normal presentation and their incredible presentation.
# Use the born method inherited from the Family class to add Baby
#  Jack with the following power: “Unknown Power”.
# Print both presentations again. Check that Baby Jack is born
#  and that his power is showing when using the incredible representation.