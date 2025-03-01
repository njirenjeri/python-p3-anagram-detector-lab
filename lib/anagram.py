# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, words):
        return [myword for myword in words if sorted(myword.lower()) == sorted(self.word) and myword.lower() != self.word]
        
