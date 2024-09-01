# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        # Normalize the word to lowercase for comparison
        sorted_word = ''.join(sorted(self.word.lower()))
        matches = []
        for candidate in words:
            # Normalize the candidate word to lowercase for comparison
            if ''.join(sorted(candidate.lower())) == sorted_word:
                matches.append(candidate)
        return matches
