class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            cur = 1
            for j in range(len(nums)):
                if i != j:
                    cur *= nums[j]
            result.append(cur)
        return result