# URL: https://leetcode.com/problems/valid-anagram/                        
# TITLE: Valid Anagram                            
# DIFFICULTY: Easy                                
# ------------------------------------------------------
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        unique = set(s)
        if set(t) != unique: return False

        for letter in unique:
            if s.count(letter) != t.count(letter): return False

        return True