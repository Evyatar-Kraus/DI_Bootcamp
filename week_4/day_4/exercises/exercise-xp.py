# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what
# you are learning in this course.
# Call the function, and make sure the message displays correctly.
print("\nExercise 1:")
def display_message():
    """Prints a message that explains what I'm learning in the course"""
    print("Hi, I am learning python over here!")
display_message()

# Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
# Call the function, make sure to include a book title as an argument when calling the function.
print("\nExercise 2:")
def favorite_book(title):
    print(f'One of my favorite books is {title}.')
favorite_book('Alice in Wonderland')

# Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as “Reykjavik is in Iceland”.
# Give the country parameter a default value.
# Call your function.

print("\nExercise 3:")
def describe_city(city, country='Italy'):
    print(f'The {city} is in {country}')

describe_city('Reykjavik','Iceland')
describe_city('Reykjavik') #using default value
describe_city(country='Iceland', city='Reykjavik') #keyword arguments


# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates
# another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message,
#  otherwise show a fail message and display both numbers.
print("\nExercise 4:")

from random import randint
gen_rand = lambda: randint(1,100) #generate a random number
compare_2_nums = lambda num1, num2: True if num1 == num2 else False #return true if 2 nums are the some, otherwise false

def compare_number_to_rand(num):
    rand_num = gen_rand()
    if compare_2_nums(num, rand_num):
        print("success, the numbers are the same")
    else:
        print(f"failure, the numbers are {num} and {rand_num} ")
compare_number_to_rand(1)

# Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function make_shirt() using positional arguments to make a shirt.
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
# Bonus: Call the function make_shirt() using keyword arguments.
print("\nExercise 5:")
#with bonus

def make_shirt(size,print_msg):
    print(f"This is a shirt of size {size} and the print on it is {print_msg}")

make_shirt(print_msg='Tomorrow is now', size='medium')

def make_shirt(size='large',print_msg='I love Python'):
    print(f"This is a shirt of size {size} and the print on it is {print_msg}")
make_shirt()
make_shirt(size="large")
make_shirt(size="small",print_msg="I love NY")

# Exercise 6 : Magicians …
# Instructions
# Make a list of magician’s names.
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.
print("\nExercise 6:")

magicians = ['Harry Houdini','David Copperfield','Raymond Teller','Penn Jillette']
add_great = lambda name: f'{name} The Great' #returns the name with 'the great' suffix
get_with_greats = lambda  arr: list(map(add_great,arr))  #returns array of names with 'the great' suffix to each element

#1st way
# def make_great():
#     global magicians # refer to a magicians var outside - usually try not to use
#     magicians = get_with_greats(magicians)

#2nd way
def make_great():
    for idx,val in enumerate(magicians):
        magicians[idx] = add_great(val)

make_great()
print(magicians)
