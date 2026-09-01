class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        candidate = []


        def backtrack(index):
            # our base condition
            if sum(candidate) == target:
                res.append(candidate.copy())
                return
            if index >= len(nums) or sum(candidate) > target:
                return
            
            candidate.append(nums[index])
            backtrack(index)
            candidate.pop()
            backtrack(index + 1)

        backtrack(0)
        return res