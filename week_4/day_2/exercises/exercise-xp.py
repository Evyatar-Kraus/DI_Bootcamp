# What We Will Learn:
# Sequence
# List
# Set
# Tuple


# Exercise 1 : Favorite Numbers
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

print('Exercise 1:')
my_fav_numbers = set()
my_fav_numbers.add(2)
my_fav_numbers.add(3)
my_fav_numbers.remove(3)
print(my_fav_numbers)

friend_fav_numbers = set([4,7,3])
print(friend_fav_numbers)
# our_fav_numbers = list(my_fav_numbers) + list(friend_fav_numbers) #another way
our_fav_numbers = set.union(my_fav_numbers, friend_fav_numbers) #2nd way
print(our_fav_numbers)

# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
print('Exercise 2:')
new_tuple = tuple([11,12,13])
#Answer you cant add anymore elements to a tuple, since tuples tuple in Python are immutable sequences.


# Exercise 3: Print A Range Of Numbers
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
print('Exercise 3:')
num_range = range(1,21)
for num in num_range:
    print(num)


# Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
print('Exercise 4:')
print("Float has a decimal point and can represent rational numbers")
print("You can do so by dividing integers")
float_list = []
start_num = 1.5
change = 0.5
for num in range(1,9):
    float_list.append(max(int(start_num),start_num))
    start_num +=change
print(float_list)

# Exercise 5: Shopping List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

print('Exercise 5:')
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)

print("After removing Banana")
basket.remove('Banana')
print(basket)

print("After removing Blueberries")
basket.remove('Blueberries')
print(basket)

print("After inserting kiwis")
basket.append('kiwi')
print(basket)

print("After inserting apples")
basket.insert(0,'Apples')
print(basket)

print("Apples inside the basket")
print(basket.count('Apples'))

basket.clear()
print("basket after removing everything")
print(basket)

# Exercise 6 : Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
print('Exercise 6:')
name = 'john'
while name != input("Please Enter name\n"):
    pass

# Exercise 7
# Instructions
# Given a list, use a loop to print out every element which has an even index.
print('Exercise 7:')
list = [1,4,'agg', 'rr' , 5]
for idx, item in enumerate(list,0):
    if idx % 2 == 0:
        print(item)

# Exercise 8
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
print('Exercise 8: output is too long so uncomment lines below')

# for num in range (1500,2501):
    # if num % 5 == 0 or num % 7 == 0:
        # print(num)

# Exercise 9: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
print('Exercise 9:')
# fav_fruits = []
fav_fruits =  list(input('please enter fruits, separated by a single space:\n').strip().split(' '))
print(fav_fruits)
fruit_choice = input('please enter a fruit:\n')
if fruit_choice in fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

# Exercise 10: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
print('Exercise 10:')
pizza_toppings = []
while True:
    pizza_topping = input("please enter a pizza topping; to quit enter 'quit':\n")
    if pizza_topping == 'quit':
        break
    elif pizza_topping == '':
        continue
    else:
        pizza_toppings.append(pizza_topping)
        print(f"I will be adding {pizza_topping} to your pizza")
print("These are your pizza toppings", pizza_toppings)

# Exercise 11: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie
# that is restricted for people between the ages of 16 and 21.
# Write a program that asks every user for their age, and prints a list of the teens who are permitted to watch the movie.
print('Exercise 11 part 1:')
family_members = ['John','Dana','Sarah']
ticket_total_cost = 0
for member in family_members:
    age = int(input(f"what is your age, {member}?\n"))
    if age > 12:
        ticket_total_cost +=15
    else:
        if age > 3:
            ticket_total_cost +=10
print(f"The family total ticket cost is:{ticket_total_cost} \n")


print('Exercise 11 part 2:')
teenagers = ['Danny','Shimson','Eli']
permitted_teenagers = []

for teenager in teenagers:
    age = int(input(f"what is your age, {teenager}?\n"))
    if age >= 16 and age <=21:
        permitted_teenagers.append(teenager)

print("The permitted teenagers are:\n",permitted_teenagers)

# Exercise 12 : Who Is Under 16?
# Instructions
# Given a list of names, write a program that asks every user for their age,
#  if they are less than 16 years old remove them from the list.
# At the end, print the final list.
print('Exercise 12:')
names = ['John','Moshe','David']
names_over_16 = []
for i in range(0,len(names)):
    user_age = int(input(f"what is your age, {names[i]}?\n"))
    if user_age >= 16:
        names_over_16.append(names[i])
names = names_over_16
print("The people that are over 16 are:\n")
print(names)
print('\n')

# Exercise 13
# Instructions
# Make a list called sandwich_orders and fill it with the names of various sandwiches .
# Then make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.
print('Exercise 13:')
sandwich_orders = ['salami','tuna','avocado']
finished_sandwiches = []

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)

for finished_sandwich in finished_sandwiches:
    print(f'I made your {finished_sandwich} sandwich')


# Exercise 14
# Instructions
# Using the list sandwich_orders from Exercise 13, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message
# saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.
print('Exercise 14:')

# print( list(['pastrami']) + list(['pastrami']) + list(['pastrami']) ) # adding/concat three lists - test it
# print((list(['pastrami'])*3)) #concat the lists by multiplying

sandwich_orders.extend(list(['pastrami'])*3) # list with a pastrami item * multiply by three for three lists and insert them with extend
print(sandwich_orders)
print("The deli has run out of pastrami\n")
print("Running a While loop to remove pastrami\n")
sandwich_orders_len = len(sandwich_orders)
# print( sandwich_orders_len)
i = 1
while i < len(sandwich_orders):
    # print(f'current index is {i}')
    # print(f'current sandwich is {sandwich_orders[i]}')
    if sandwich_orders[i] == 'pastrami':
        sandwich_orders.pop(i)
    else:
        i = i +1

# print(sandwich_orders)
finished_sandwiches = []

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)

for finished_sandwich in finished_sandwiches:
    print(f'I made your {finished_sandwich} sandwich')
