

# Instructions :
# Download the_stranger.txt

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Implement the following methods:

from pathlib import Path
import string

class Text():
    def __init__(self, text_str):
        text_string= text_str.lower()
        text_string_list = text_string.split()
        self.text_str = " ".join(text_string_list)

    def get_word_list(self):
        return  self.text_str.lower().split()

# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message .
    def get_word_frequency(self, word):
        """return how many times a word appears in the text"""
        return self.get_word_list().count(word.lower())


# a method that returns the most common word in the text.
    def get_most_common_word(self):
        """return most common word in the text"""
        words = self.get_word_list()
        #use set
        words_set = set(words)
        most_common_word = max(words_set,key=words.count)
        return most_common_word

# a method that returns a list of all the unique words in the text.

    def get_unique_words(self):
        """returns a list of unique words (appear only once) in the text"""
        words =  self.get_word_list()
        unique_words = list(filter(lambda x: words.count(x) == 1,words))
        return unique_words

# a classmethod that returns a Text instance but with a text file: >>> Text.from_file('the_stranger.txt')
    @classmethod
    def createTextFromFile(cls,file_path):
        with open(file_path, 'r') as file:
            text = file.read()
        return cls(text)

# Create a class called TextModification that inherits from Text.
# Implement the following methods:

class TextModification(Text):
    def __init__(self,text):
        super().__init__(text)
        self.english_stop_word_list = []
        self.exclude_punc_list = set(string.punctuation)

# a method that returns the text without any punctuation.
    def get_text_without_punctuation(self):
        # print(self.text_str.count('.'))
        text = self.text_str.lower()
        text_without_punctuation = ''.join(ch for ch in text if ch not in self.exclude_punc_list)
        # print(text_without_punctuation.count('.'))
        return text_without_punctuation

# a method that returns the text without any english stop-words (check out what this is !!).
    def get_text_without_english_stop_words(self):
        # print(self.text_str.count('amongst'))
        text = self.text_str.lower()
        if not self.english_stop_word_list:
            with open('stopwords.txt', 'r') as file: #after first loading of the stopwords file we save it to the prop like cache
                    self.english_stop_word_list = file.read().split()
                    print("Saving file stopwords to obj prop")
        text_without_english_stop_words = ' '.join([ch for ch in text if ch not in self.english_stop_word_list])
        # print(text_without_english_stop_words.count('amongst'))
        return text_without_english_stop_words

# a method that returns the text without any special characters.
    def get_text_without_special_characters(self):
        # print(self.text_str.count('"'))
        text = self.text_str.lower()
        self.text_without_special_characters=  ' '.join([ch for ch in text if ch if ch.isalnum()]) #if not alpha numeric char its a special char
        # print(self.text_without_without_special_characters.count('"'))
        return self.text_without_special_characters
# Now, use the provided txt file and try using the class you created above.

file_path = "the_stranger.txt"

#1st way
# file_text = Path(file_path).read_text()

# 2nd way
with open(file_path, 'r') as file:
    file_text = file.read().replace('\n', ' ')

print(file_text.lower().count('stranger'))
# print(file_text)
textObj = Text.createTextFromFile(file_path)
print("Most common word")
print(textObj.get_most_common_word())
# print("\n\n\nUnique words\n")
# print(textObj.get_unique_words())
print('\n\n\nfrequency of the word the')
print(textObj.get_word_frequency('the'))
print('\n\n\nfrequency of the word man')
print(textObj.get_word_frequency('man'))
print('\n\n\nfrequency of the word instagram ')
print(textObj.get_word_frequency('instagram'))
print('\n\n\nfrequency of the word stanger')
print(textObj.get_word_frequency('stranger'))
print('\n\n\nfrequency of the word worth ')
print(textObj.get_word_frequency('worth'))
print('\n\n\nfrequency of the word and ')
print(textObj.get_word_frequency('and'))


file_path = 'the_stranger.txt'
textModObj = TextModification.createTextFromFile(file_path)
# print(textModObj.get_text_without_punctuation())
textModObj2 = TextModification(file_text)
print(file_text.lower().split().count('and'))
print(textModObj2.get_word_list().count('and'))
print(textModObj2.get_word_frequency('and'))
print("\n\ntextModobj")
print("\nHow many '.' inside text before and after without_punctuation")
print(textModObj.text_str.count('.'))
print(textModObj.get_text_without_punctuation().count('.'))
print("\nHow many 'and' inside text before and after without_english_stop_words")
print(textModObj.text_str.count('and'))
print(textModObj.get_text_without_english_stop_words().count('and'))
print("From here stop words arent loaded from file - but saved in the object instance prop")
print("\nHow many 'as' inside text before and after without_english_stop_words")
print(textModObj.text_str.count('as'))
print(textModObj.get_text_without_english_stop_words().count('as'))

print('\nHow many \'"\' inside text before and after without_special_characters')
print(textModObj.text_str.count('"'))
print(textModObj.get_text_without_special_characters().count('"'))
print('\nfrequency of the word and ')
print(textModObj.get_word_frequency('and'))


print("\n\ntextModObj2")
print("\nHow many '.' inside text before and after without_punctuation")
print(textModObj2.text_str.count('.'))
print(textModObj2.get_text_without_punctuation().count('.'))
print("\nHow many 'and' inside text before and after without_english_stop_words")
print(textModObj2.text_str.count('and'))
print(textModObj2.get_text_without_english_stop_words().count('and'))
print(textModObj2.get_text_without_english_stop_words().count('and'))
print('\nHow many \'"\' inside text before and after without_special_characters')
print(textModObj2.text_str.count('"'))
print(textModObj2.get_text_without_special_characters().count('"'))
print('\nfrequency of the word and ')
print(textModObj2.get_word_frequency('and'))

# # Note: Note: Feel free to implement/create any attribute,
# #  method or function needed to make this work, be creative :)
