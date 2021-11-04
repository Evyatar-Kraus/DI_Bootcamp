class AnagramChecker:
    def __init__(self, file_name='sowpods.txt'):
        with open(file_name) as f:
            #all words without spaces in a list in uppercase
            self.words = [word.strip().upper() for word in f.readlines()]
            # self.words = list(map(lambda x:x.strip(), f.readlines()))
    #is the word in the list of words
    def is_valid_word(self, word):
        return word.upper() in self.words

    def get_anagrams(self, word):
        word = word.upper()
        #sort the word alphabetically
        word_sorted = sorted(list(word))

        anagrams = []
        for other_word in self.words:
            #if the word sorted alphabetically equals the current word in the list sorted alphabetically then they are anagrams
            if sorted(list(other_word)) == word_sorted:
                anagrams.append(other_word)
        #remove the original word from anagrams returned
        anagrams.remove(word)
        return anagrams
