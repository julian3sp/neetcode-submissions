class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def dfs(index):
            if index >= len(s):
                res.append(cur.copy())
                return

            for r in range(index, len(s)):
                if isPalindrome(s[index : r + 1]):
                    cur.append(s[index : r + 1])
                    dfs(r + 1) 
                    cur.pop()

        def isPalindrome(s):
            l = 0
            r = len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        dfs(0)
        return res
