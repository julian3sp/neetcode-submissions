class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        counts = {}
        maxFreq = 0
        # r - l + 1 - count[maxFreq]


        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            maxFreq = max(maxFreq, counts[s[r]])


            if ((r - l + 1) - maxFreq) > k:
                counts[s[l]] -= 1
                l += 1
                

            res = max(res, r - l + 1)
        return res

            
