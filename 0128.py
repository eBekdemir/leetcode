# URL: https://leetcode.com/problems/longest-consecutive-sequence/                        
# TITLE: Longest Consecutive Sequence                            
# DIFFICULTY: Medium                                
# ------------------------------------------------------
class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        sequences_lengths = [0]
        for nm in nums:
            if (nm - 1) in nums:
                continue
            i = 1
            while (nm + i) in nums:
                i += 1
            sequences_lengths.append(i)
        return max(sequences_lengths)


# ------------------------------------------------------
class Solution(object):
    def longestConsecutive(self, nums):
        if nums == []: return 0
        srt = sorted(set(nums))
        last = srt[0]
        mx = 1
        crt = 1
        for i in range(0, len(srt)):
            if last == srt[i] - 1:
                crt += 1
            else:
                if crt > mx: mx = crt
                crt = 1
            last = srt[i]
        return max(mx, crt)