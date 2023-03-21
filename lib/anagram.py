
class Anagram:

    def __init__(self, word) -> None:
        self.word = word

    def match(self, list):
        match_list = []
        for word in list:
            word_deconstructed = [letter for letter in word]
            search_word_deconst = [letter for letter in self.word]

            if sorted(word_deconstructed) == sorted(search_word_deconst):
                match_list.append(word)

        return match_list