# URL: https://leetcode.com/problems/two-sum/                        
# TITLE: Two Sum                            
# DIFFICULTY: Easy                                
# ------------------------------------------------------
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            wanted = target - num
            if wanted in nums[i+1:]:
                i2 = nums[i+1:].index(wanted)
                return [i, i+i2+1]
        return []


# ------------------------------------------------------
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dct = dict()
        for i, num in enumerate(nums):
            wanted = target - num
            if wanted in dct:
                return [dct[wanted], i]
            dct[num] = i
        return []
