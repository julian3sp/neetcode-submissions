class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n 

        zero_count = 0

        for i in range(n):
            if nums[i] == 0:
                zero_count += 1

        if zero_count > 1:
            return res

        total_prod = 1

        for i in range(n):
            if nums[i] == 0:
                continue
            total_prod *= nums[i]
        for i in range(n):
            if zero_count == 0:
                res[i] = total_prod // nums[i]
            elif nums[i] == 0:
                res[i] = total_prod
        return res