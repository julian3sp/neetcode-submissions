class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            cur = 0
            i = 0
            while n + i in numSet:
                cur += 1
                i += 1
            if cur > longest:
                longest = cur
        return longest

