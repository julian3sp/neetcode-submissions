class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            hashMap[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashMap and i < hashMap[complement]:
                return [i, hashMap[complement]]

            hashMap[i] = nums[i]
        return [0, 0]