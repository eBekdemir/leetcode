# two pointers
class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1
        while r > l:
            res = numbers[l]+numbers[r]
            if res == target: return [l+1, r+1]
            elif res > target: r -= 1
            else: l += 1
