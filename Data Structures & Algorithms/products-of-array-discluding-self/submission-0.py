class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
      result = [1] * len(nums) 
      for i in range(len(nums)):
        cur = 1 
        for j in range(len(nums)):
            if j != i:
                cur *= nums[j]
        result[i] = cur
      return result

