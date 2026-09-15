class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        

        while l <= r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = l + ((r - l) // 2)

            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            if nums[mid] > nums[r]:
                # min in right side
                l = mid + 1
            elif nums[mid] < nums[r]:
                # min in left side
                r = mid - 1
            else:
                return nums[mid]
            
        return -1
