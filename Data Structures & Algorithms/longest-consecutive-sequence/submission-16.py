class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest_sequence = 0
        
        for num in hashset:
            if num - 1 not in hashset:
                current = 1
                while num + current in hashset:
                    current += 1
                longest_sequence = max(current, longest_sequence)
        return longest_sequence
            

