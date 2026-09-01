class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map = {2: "abc", 3: "def", 4: "ghi",
        5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 
        9: "wxyz" }
        res = []
        #we can create a string out of combining the strings 
        #associated with each of our digits

        #then find all combinations of len(digits) within this string

        def backtrack(index, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return

            for num in num_map[int(digits[index])]:
                backtrack(index + 1, cur + num)
        if digits:       
            backtrack(0, "")
        return res
