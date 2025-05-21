# URL: https://leetcode.com/problems/generate-parentheses/                        
# TITLE: Generate Parentheses                            
# DIFFICULTY: Medium                                
# ------------------------------------------------------
class Solution(object):
    def generateParenthesis(self, n):
        res = []
        def generate(s='', o=0, c=0):
            if len(s) == 2*n: 
                res.append(s)
                return
            if o == c: 
                generate(s + '(', o+1, c)
            elif o+1 <= n:
                generate(s + '(', o+1, c)
                generate(s + ')', o, c+1)
            else:
                generate(s + ')', o, c+1)
        generate()
        return res