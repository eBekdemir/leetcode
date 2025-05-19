# URL: https://leetcode.com/problems/score-of-a-string/                        
# TITLE: Score of a String                            
# DIFFICULTY: Easy                                
# ------------------------------------------------------
class Solution(object):
    def scoreOfString(self, s):
        return sum([abs(ord(s[i]) - ord(s[i-1])) for i in range(1, len(s))])


# ------------------------------------------------------
class Solution(object):
    def scoreOfString(self, s):
        score = 0
        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i-1])) 
        return score