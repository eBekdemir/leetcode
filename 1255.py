from itertools import combinations

class Solution(object):
    def allIndexSubsets(self, n):
        indices = list(range(n))
        result = []
        for r in range(n + 1):
            result.extend(combinations(indices, r))
        return [list(subset) for subset in result]

    def calculateScore(self, word, score):
        scr = 0
        for letter in word:
            scr += score[ord(letter)-97]
        return scr

    def validIndicies(self, words, indicies, letters):
        valid_indicies = []
        for inds in indicies:
            dct = dict(**letters)
            check = False
            for i in inds:
                for char in words[i]:
                    if char in dct and dct[char] != 0:
                        dct[char] -= 1
                    else: 
                        check = True
                        break
                if check:
                    break
            if check: continue
            valid_indicies.append(inds)

        return valid_indicies


    def maxScoreWords(self, words, letters, score):
        scores_of_words = [self.calculateScore(word, score) for word in words]
        count_of_letters = dict()
        for letter in set(letters):
            count_of_letters[letter] = letters.count(letter)

        indicies = self.validIndicies(words, self.allIndexSubsets(len(words)), count_of_letters)

        return max([sum([scores_of_words[i] for i in inds]) for inds in indicies])