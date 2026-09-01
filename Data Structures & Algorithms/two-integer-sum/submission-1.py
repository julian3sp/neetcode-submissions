class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
            # we use this because it allows for O(1) lookup
        for j in range(len(nums)):
            complement = target - nums[j]
            if complement in hashmap and j != hashmap[complement]:
                return [j, hashmap[complement]]
        return []