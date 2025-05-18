# URL: https://leetcode.com/problems/top-k-frequent-elements/                        
# TITLE: Top K Frequent Elements                            
# DIFFICULTY: Medium                                
# ------------------------------------------------------
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequent = {}
        for num in nums:
            frequent[num] = frequent.get(num, 0) + 1
        sort = sorted(frequent.items(), key = lambda x: x[1], reverse=True)
        return [item[0] for item in sort[:k]]