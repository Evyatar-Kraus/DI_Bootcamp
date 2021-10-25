# What You Will Learn :
# Python Basics
# Conditionals

# Instructions
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.
# Bonus : If they were born on a leap year, display two cakes !
from datetime import date

#getting user input
birthday_date = input("Please enter your birthday: DD/MM/YYYY form:\n")
print(birthday_date)
birth_day_in_month, birth_month, birth_year = tuple(map(lambda x: int(x), birthday_date.split('/')))

#getting current year
current_year = date.today().year
print(f"current year is {current_year}\n")

#calculating current age
age = current_year - birth_year
print(f"You are {age} years old")

#calculating number of candles
number_of_candles = age % 10
print(f"Your number of candles is {number_of_candles}")

#bonus
is_leap_year = False
birthday_year = int(birth_year)

#figuring out if it's a leap year
if birthday_year % 4 == 0:
    if birthday_year % 100 != 0:
        is_leap_year = True
    if birthday_year % 100 == 0 and birthday_year % 400 == 0:
       is_leap_year = True

print(f"This year is {'' if is_leap_year else 'not'} a leap year")
print("Printing cake:")

#constructing the happy and birthday string with the colon
happy_str = 'Happy'
happy_str = list(happy_str)
happy_loc = 0
while happy_loc < len(happy_str)+1:
  happy_str.insert ( happy_loc , ':' )
  happy_loc = happy_loc +2
happy_str = ''.join(happy_str)


birthday_str = 'Birthday'
birthday_str = list(birthday_str)
birth_day_loc = 0
while birth_day_loc < len(birthday_str)+1:
  birthday_str.insert ( birth_day_loc , ':' )
  birth_day_loc = birth_day_loc +2
birthday_str = ''.join(birthday_str)

# building the strings for printing the cake
line_num = 7
line_len = 19
line_dict = {}

small_row_inside_chars_num = 13
first_line_spaces = 8
first_line_underscores = small_row_inside_chars_num - number_of_candles
first_line = int(first_line_spaces/2) * ' ' + int(first_line_underscores/2) * '_' + number_of_candles*'i' \
    + int(first_line_underscores/2) * '_' \
    +int(first_line_spaces/2) * ' '

happy_line_spaces_inside = line_len - 8 - len(happy_str)
happy_line= ' '*3+'|' + ' ' +  happy_str + ' ' + '|' +' '*3

line_dict["line_1"] = first_line
line_dict["line_2"] = happy_line
line_dict["line_3"] = ' '*2+ '_|' + ' '* (line_len-6) + '|_'+ ' '*2
line_dict["line_4"] =  ' '*1 +'|' + '^'*(line_len-2) + '|'+ ' '*1
line_dict["line_5"] = ' |' + birthday_str + '|  '
line_dict["line_6"] = ' '*1+ '|' + ' '* (line_len-2) + '|'+ ''*2
line_dict["line_7"] = ' '*1 + '~' * line_len

#since its in a dict we can make a short loop and call the keys dynamically
for line_num in range(1, 8):
    print(line_dict['line_'+str(line_num)],end='\n')

#if its a leap year print once more
if is_leap_year:
    print("this is a leap year! get one more cake:\n")
    for line_num in range(1, 8):
        print(line_dict['line_'+str(line_num)],end='\n')
