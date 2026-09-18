class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        maxFreq = 0
        res = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxFreq = max(freq[s[r]], maxFreq)

            while ((r - l + 1) - maxFreq) > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res