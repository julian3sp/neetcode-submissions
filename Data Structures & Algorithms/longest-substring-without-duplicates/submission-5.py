class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_ind = {}
        res = 0
        l = 0

        for i in range(len(s)):

            if s[i] in last_ind:
                l = max(l, last_ind[s[i]] + 1)


            last_ind[s[i]] = i

            res = max(res, i - l + 1)

        return res


            
            