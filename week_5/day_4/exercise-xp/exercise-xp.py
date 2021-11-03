# What You Will Learn
# Working with files

# Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

from os import path, getcwd, sep
import random

print("\n\nExercise 1")

FILE_NAME ='wordlist.txt'
FILE_PATH = path.normpath(getcwd()+sep+FILE_NAME)

# Create a function called get_words_from_file. This function should read the file’s content
#  and return the words as a collection. What is the correct data type to store the words?

word_list = []

def get_words_from_file(path):
    try:
        print(path)
        with open(path, 'r') as file:
            for line in file:
                word_list.append(line.rstrip())
        return word_list
    except FileNotFoundError:
        print("bad file path")
        raise SystemExit

# Create another function called get_random_sentence which takes a single parameter called length.
#  The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.
def get_random_sentence(length):
    """
    returns a list of words
    Parameters:
    length - used to determine how many words the sentence should have.
    """
    word_list_len = len(word_list)
    random_lines_nums = [random.randint(0,word_list_len-1) for x in range(0,length)]
    sentence_word_list = [word_list[i] for i in random_lines_nums]
    return sentence_word_list

# Take the random words and create a sentence (using a python method), the sentence should be lower case.
def create_sentence(word_list):
    return ' '.join([word.lower() for word in word_list])

# Create a function called main which will:
# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are:
#  an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

def main():
    print("This program generates a random sentence")
    try:
        length = int(input("How long do your want your sentence to be?"))
        if not (2 <= length <= 20):
            raise ValueError
        words = get_words_from_file(FILE_PATH)
        sentence_words = get_random_sentence(length)
        sentence = create_sentence(sentence_words)
        print("We have a sentence for you:",end="\n")
        print(sentence)
    except ValueError:
        print("You entered incorrect data. This program will terminate itslef")


if __name__ == "__main__":
    # main()
    pass



# Exercise 2: Working With JSON
# Instructions
import json
sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

print("\n\nExercise 2")
json_dict = json.loads(sampleJson)
# Access the nested “salary” key from the JSON-string above.
salary =  json_dict['company']['employee']['payable']['salary']
print(salary)
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
json_dict['company']['employee']['birth_date'] = '10/10/1995'
print(json_dict)

new_json_string = json.dumps(json_dict)
# Save the dictionary as JSON to a file.

file_path = 'workfile.txt'

#1st way
# with open(file_path, "w") as work_file:
#     work_file.write(new_json_string)

#2nd way
f = open(file_path, "w")
new_json_string = json.dump(json_dict,open(file_path, "w"))
f.close()
