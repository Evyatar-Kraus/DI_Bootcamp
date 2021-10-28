#Instructions below ↓↓↓

# example for user input ↓↓↓
# user_input = "without,hello,bag,world"

get_user_input = lambda:input("Please enter a comma separated sequence of words:\n")
sort_words_sequence = lambda seq: ','.join([ y for y  in sorted(seq.split(","))])

def main():
    user_input_words = get_user_input()
    sorted_user_input = sort_words_sequence(user_input_words)
    print(sorted_user_input)

if __name__ == '__main__':
    main()

# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints
# the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Suppose the following input is supplied to the program:
# without,hello,bag,world

# Then, the output should be:
# bag,hello,without,world
