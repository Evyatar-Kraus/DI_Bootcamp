# What We Will Learn:
# Python Basics
# Python data types
# Comparaison


# Exercise 1 : Hello World
# Instructions
# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello world
print("Exercise 1:")
print("Hello world\n" * 4)

# Exercise 2 : Some Math
# Instructions
# Write code that calculates the result of: (99^3) * 8
print("Exercise 2:")
from math import pow
print("result of (99^3) * 8:")
# print((99*99*99)*8) #1st way
print(int(pow(99,3) * 8)) #2nd way

# Exercise 3 : What Is The Output ?
# Instructions
# Predict the output of the following code snippets:
# >>> 5 < 3 ->false
# >>> 3 == 3 -> true same type same value
# >>> 3 == "3" -> false - different type int and str
# >>> "3" > 3 -> TypeError checking > on str and int - not supported
# >>> "Hello" == "hello" -> False -> in first one first letter has capital letter and the second's first letter isn't a capital letter

print("\nExercise 3:")
print("boolean expressions outputs")
print("5 < 3 is ", 5<3)
print("3 == 3 is ", 3 == 3)
print("3 == \"3\" is ", 3 == "3")
# print("\"3\" > 3 is ", "3" > 3) #TypeError
print("\"Hello\" == \"hello\" is ","Hello" == "hello")
print("\n")

# Exercise 4 : Your Computer Brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

print("Exercise 4:")
computer_brand = 'Dell'
print(f"I have a {computer_brand} computer")


# Exercise 5 : Your Information
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself.
# The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

print("Exercise 5:")
name = 'Evyatar'
age = 24
shoe_size = 43
info = 'I am {0}, I am {1} years old , and my shoe size is {2}'.format(name,age,shoe_size)
print(info)
print('\n')

# Exercise 6 : A & B
# Instructions
# Create two variables, a and b.
# Each variables value should be a number.
# If a is bigger then b, have your code print Hello World.

print("Exercise 6:")
a = 5
b = 4
if a > b:
    print("Hello world\n")

# Exercise 7 : Odd Or Even
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.

print("Exercise 7:")
number = int(input("Please enter a number\n"))
if number % 2 == 0:
    print("The number is even\n")
else:
     print("The number is odd\n")

# Exercise 8 : What’s Your Name ?
# Instructions
# Write code that asks the user for their name and determines whether or not you have the same name,
# print out a funny message based on the outcome.


print("Exercise 8:")
user_name = input("please enter your name:\n")
if len(user_name) < 4:
    print("I asked for your name, not your nickname :P\n")
elif len(user_name) > 9:
    print("This will take too much memory :P\n")
else:
    print("Thank you, the name was registered.\n")

# Exercise 9 : Tall Enough To Ride A Roller Coaster
# Instructions
# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

print("Exercise 9:")
height = float(input("please enter your height in inches:\n"))
height_in_cm = height*2.54 # convert inches to cm by multiplying by 2.54
tall_enough = height_in_cm > 145
if tall_enough:
    print("Hurray, You are tall enough to ride.\n")
else:
    print("Sorry, but you are not tall enough to ride.\n")
