class Solution(object):
    def prod(self, nums):
        x = 1
        for nm in nums:
            x *= nm
        return x

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zeros = nums.count(0)
        if zeros > 1: return [0]*len(nums)
        
        if zeros == 1:
            ind = nums.index(0)
            x = [0]*len(nums)
            x[ind] = self.prod(nums[:ind] + nums[ind + 1:])
            return x
        
        production = self.prod(nums)
        return [production//nm for nm in nums]