class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        n = len(nums)
        res = [0] * n
        for i in range(n):
            if nums[i] == 0:
                zero_count += 1
        
        if zero_count > 1:
            return res
        
        total_product = 1
        for i in range(n):
            if nums[i] != 0:
                total_product *= nums[i]
        for i in range(n):
            if zero_count:
                res[i] = 0 if nums[i] else total_product
            else:
                res[i] = total_product // nums[i] 
        return res
