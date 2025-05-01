class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]] 
        """
        theMap = dict()
        for s in strs:
            stred = ''.join(sorted(s))
            if stred in theMap:
                theMap[stred].append(s)
            else:
                theMap[stred] = [s]
        return list(theMap.values())


# -------------------------------------------------------
from collections import Counter
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicts = []
        anagrams = []
        for sentence in strs:
            theDict = Counter(sentence)
            if theDict in dicts:
                anagrams[dicts.index(theDict)].append(sentence)
            else:
                dicts.append(theDict)
                anagrams.append([sentence])
        return anagrams


# ------------------------------------------------------
class Solution(object):
    def Counter(self, sent):
        dct = dict()
        set_ = set(sent)
        for letter in set_:
            dct[letter] = sent.count(letter)
        return dct
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicts = []
        anagrams = []
        for sentence in strs:
            theDict = self.Counter(sentence)
            if theDict in dicts:
                anagrams[dicts.index(theDict)].append(sentence)
            else:
                dicts.append(theDict)
                anagrams.append([sentence])
        return anagrams

