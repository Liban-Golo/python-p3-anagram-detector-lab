# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        matches = []
        sorted_original = sorted(self.word)

        for w in word_list:
        
            if w.lower() != self.word:
                if sorted(w.lower()) == sorted_original:
                    matches.append(w)

        return matches
