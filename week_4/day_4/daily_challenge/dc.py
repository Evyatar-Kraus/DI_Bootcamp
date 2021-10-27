# Daily Challenge: Solve The Matrix
# Last updated : April 22nd 2021

#the matrix given
mat = [
    ['7','i','3'],
    ['T','s','i'],
    ['h','%','x'],
    ['i',' ','#'],
    ['s','M',' '],
    ['$','a',' '],
    ['#','t','%'],
    ['^','r','!']
]

relevant_chars = ''
#rotating the mat around 180 deg for  it to be easier to work with
# print(*mat)
rotated_mat = list(zip(*mat)) #-> the * unpacking gives you all the items inside mat - now its 8 rows each with 3 elements
# zip -> the zip takes the unpacked and makes of them new lists with the list of the first elements of the previous mat rows and etc...
# list -> turn it back to a list - now it's a list of 3 tuples each one  8 elements long
# print(rotated_mat)

for row in rotated_mat:
    relevant_chars = relevant_chars + ''.join(map(lambda col: col if col.isalpha() else '' if col.isnumeric() else ' ' ,row))
    #go over each row in the rotated_mat and leave only alphabetical chars intact, numbers will be empty string and
    #symbols will become space

decrypted_string = ' '.join(relevant_chars.split()) #to remove extra spacing
print(decrypted_string)


# What You Will Learn :
# Python Basics
# Conditionals
# Loops
# Functions


# Instructions
# Hint: Look at the remote learning “Matrix” videos

# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost
#  column, select only the alpha characters and connect them, then he replaces every group of
# symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix:

#     7i3
#     Tsi
#     h%x
#     i #
#     sM
#     $a
#     #t%
#     ^r!

# utility funcs - not used
# get_mat_rows_num = lambda mat: len(mat)
# get_mat_col_num = lambda mat: len(mat[0]) #for mat with the same number of elements in every row


