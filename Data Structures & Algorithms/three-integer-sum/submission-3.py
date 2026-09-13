class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []


        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                threeSum = nums[j] + nums[k]
                target = -nums[i]

                if threeSum < target:
                    j +=1      
                elif threeSum > target:
                    k -=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j +=1
                    while nums[j] == nums[j-1] and j < k:
                        j +=1

        return res