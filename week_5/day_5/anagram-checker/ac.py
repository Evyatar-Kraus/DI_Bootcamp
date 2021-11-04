
from anagram_checker import AnagramChecker

def is_word_valid(word):
    #without spaces - so only letters in the word - and is only alphabet
    return len(word.split()) == 1 and word.isalpha()

while True:
    #show menu
    user_choice = input('A. Find a word\'s anagrams\nX. Exit\n')
    #exit the program - lowercase or uppercase x
    if user_choice in 'xX':
        print('Goodbye')
        break
    elif user_choice.upper() == 'A':
        selected_word = input('give us the word to check for anagrams\n')
        if is_word_valid(selected_word):
            #clean words from spaces
            clean_word = selected_word.strip()
            a = AnagramChecker('wordlist.txt')
            #get the anagrams to the word
            anagrams = a.get_anagrams(clean_word)
            msg = f'''YOUR WORD :"{clean_word}"
this is a valid English word.
Anagrams for your word:'''
            #print the message and the anagrams as *args
            print(msg, *anagrams)
        else:
            print('not a valid word')