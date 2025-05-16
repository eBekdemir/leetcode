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