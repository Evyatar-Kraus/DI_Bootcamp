# Exercises XP
# Last updated : April 22nd 2021


# What We Will Learn:
# Dictionaries


# Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
from pprint import pprint


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
pprint("Exercise 1:")
my_dict = {}
for key, value in list(zip(keys, values)):
    my_dict[key] = value
pprint(my_dict)


# Exercise 2 : Cinemax #2
# Instructions
# “Continuation of Exercise Cinemax from Week4Day2 XP”

# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# How much does each family member have to pay ?

# print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the
#  provided family variable (Hint: ask the user for names and ages and add
# them into a family dictionary that is initially empty).
pprint("Exercise 2:")
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

###uncomment for bonus###
# family = {}
# while input("Please press enter to continue to fill a name and a price; to exit write 'quit': ") != 'quit':
#     person_name = input("Please enter a person name\n")
#     person_age = int(input("Please enter age - int:\n"))
#     family[person_name] = person_age
# pprint(family)

total_cost = 0
for person, age in family.items():
    person_price = 0
    if age > 3:
        if age > 12:
            person_price = 15
        else:
            person_price = 10
    total_cost += person_price
    pprint(f"{person} has to pay ${person_price}")

pprint(f'The family total cost is ${total_cost} \n')

# Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green


# 2. Create a dictionary called brand which value is
# the information from
#  part one (turn the info into keys and values).
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras
#  clients are.
# 5. Add a key called country_creation with a
#  value of Spain.
# 6. Check if the key international_competitors
#  is in the dictionary.
# If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie.
# length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara
#  with
# the following details:

# creation_date: 1975
# number_stores: 10 000


# 13. Use a method to add the information
#  from the dictionary more_on_zara to the
#  dictionary brand.
# 14. Print the value of the key number_stores.
#  What just happened ?
pprint("Exercise 3:")
#2
brand = {
    'name': 'zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': [
        {'country': 'France', 'colors': ['blue']},
        {'country': 'Spain', 'colors': ['red']},
        {'country': 'USA', 'colors': ['pink', 'green']}
    ]
}

brand['number_stores'] = 2 #3

print("Zara's clients are:") #4
client_groups = brand['type_of_clothes']

for idx, client_group in enumerate(client_groups):
    if idx == len(client_groups) - 1: #not printing last beacause home isn't a client group :)
        break
    if idx == len(client_groups) - 2: #last relevant item ends with a dot
        print(f"{client_group}.")
    elif  idx == len(client_groups) - 3: #one before last has and instead of ,
        print(f"{client_group} and ",end="")
    else:
        print(f"{client_group}, ",end="")


#5
brand['country_creation'] = 'Spain'

#6
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')
pprint(brand)

#7
# brand.pop('creation_date',None) #another way to remove
del brand['creation_date']
pprint(brand)

#8
print(brand['international_competitors'][-1:-2:-1])
#print from -1 (last) until -2 not inclusive -
# and go reverse 1 at a time


#9
print("Printing major clothes colors in the US with list comprehension:")
#1st way
usa_major_colors = [color for country in brand['major_color'] for color in country['colors'] if country['country'] == 'USA']
# same way but with enters and explanation
# usa_major_colors =  [color \ # #4-> give me the color
#                    for country in brand['major_color'] \ # #1-> for every country obj in brand['major_colors']
#                    for color in country['colors'] \ # #2 -> for the color in its colors prop
#                    if country['country'] == 'USA'] # #3 -> filter -> if the country obj's country prop is USA
#2nd way - different filter
# usa_major_colors = [color for country in brand['major_color'] for color in country['colors'] if country['country'] is 'USA']
#3rd way -> different filter - with is not spain or france (the other countries beside USA)
# usa_major_colors = [color for country in brand['major_color'] for color in country['colors'] if country['country'] is not 'France' and country['country'] != 'Spain']
pprint(usa_major_colors)

#10
print(f"dict length is {len(brand)}")

#11
print('brand keys: ',end="")
for key in brand.keys():
     print(key,end =" ")

#12
more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}
#13
brand = {**brand,**more_on_zara} #1st way
brand.update(more_on_zara) #2nd way
pprint(brand)

#14
# the key number_stores's value was overwritten
print(brand.get('number_stores'))


# Exercise 4 : Disney Characters
# Instructions
# Use this list :

# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# Analyse these results :

# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.
