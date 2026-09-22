class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0

        while l <= r:
            totalTime = 0
            m = l + ((r - l) // 2)

            for pile in piles:
                totalTime += math.ceil(float(pile) / m)

            if totalTime <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res




