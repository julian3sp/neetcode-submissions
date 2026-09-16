class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]


        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] < nums[m - 1]:
                return nums[m]
            
            if nums[m] > nums[r]:
                # min in right side
                l = m + 1
            elif nums[m] < nums[r]:
                r = m - 1
            else: 
                return nums[m]
        return -1  

            


