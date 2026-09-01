class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        r = 0
        prev_index = {}

        while r < len(s):

            if s[r] in prev_index:
                l = max(prev_index[s[r]] + 1, l)
            prev_index[s[r]] = r
            res = max(res, r - l + 1)
            r += 1 

        return res

            
            