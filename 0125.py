# URL: https://leetcode.com/problems/valid-palindrome/                        
# TITLE: Valid Palindrome                            
# DIFFICULTY: Easy                                
# ------------------------------------------------------
# two pointers
class Solution(object):
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        s = s.lower()
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l] == s[r]: 
                    l += 1
                    r -= 1
                else: return False
            if not s[l].isalnum(): l += 1
            if not s[r].isalnum(): r -= 1
        return True

# ------------------------------------------------------
# reverse string
class Solution(object):
    def isPalindrome(self, s):
        s = ''.join([s[i] for i in range(len(s)) if s[i].isalnum()]).lower()
        return s == s[::-1]
