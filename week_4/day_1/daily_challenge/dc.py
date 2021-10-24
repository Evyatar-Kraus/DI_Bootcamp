# What You Will Learn :
# Python Basics
# Conditionals
# Loops

#Instructions below ↓↓↓
from random import shuffle

user_string = input("please enter a 10 characters long string\n")
if len(user_string) < 10:
    print("string not long enough")
elif len(user_string) > 10:
    print ("string too long")
else:
    print("first char is :")
    print(user_string[0])

    print("\nlast char is :")
    print(user_string[len(user_string)-1]) #1 way
    # print(user_string[-1])

    # print the strings in steps
    print("\nprinting the string in 'steps':")
    print(user_string[:1])
    print(user_string[:2])
    print(user_string[:3])
    print(user_string[:4])
    print(user_string[:5])
    print(user_string[:6])
    print(user_string[:7])
    print(user_string[:8])
    print(user_string[:9])
    print(user_string[:10])

    # shuffle and return a jumbled string
    print('\n')
    user_string_as_list = list(user_string) # change to list as shuffle won't work on str
    shuffle(user_string_as_list)
    user_string = ''.join(user_string_as_list) # back to str
    print(user_string)




# Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

# Then, print the first and last characters of the given text.

# Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "Hello World"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# Hello World

# 4. Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:
# Hlrolelwod
