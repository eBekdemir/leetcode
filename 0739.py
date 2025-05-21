# URL: https://leetcode.com/problems/daily-temperatures/                        
# TITLE: Daily Temperatures                            
# DIFFICULTY: Medium                                
# ------------------------------------------------------
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if stack:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    poped_i = stack.pop()
                    res[poped_i] = i - poped_i
            stack.append(i)
        return res