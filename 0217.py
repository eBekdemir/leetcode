# URL: https://leetcode.com/problems/contains-duplicate/                        
# TITLE: Contains Duplicate                            
# DIFFICULTY: Easy                                
# ------------------------------------------------------
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = set(nums)
        return True if len(x) < len(nums) else False