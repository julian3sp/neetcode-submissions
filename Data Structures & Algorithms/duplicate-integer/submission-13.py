class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurences = set()

        for num in nums:
            if num in occurences:
                return True
            occurences.add(num)
        return False