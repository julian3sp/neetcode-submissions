class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            hashMap[nums[i]] = i

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashMap and hashMap[complement] < i:
                return [hashMap[complement], i]
            hashMap[num] = i