class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        candidates.sort()

        def backtrack(index):
            if sum(cur) == target:
                res.append(cur.copy())
                return
            if sum(cur) > target or index == len(candidates):
                return
            
            cur.append(candidates[index])
            backtrack(index + 1)
            cur.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1)

        backtrack(0)
        return res