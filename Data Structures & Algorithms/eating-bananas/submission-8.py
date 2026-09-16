class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)
        k = 0


        while l <= r:
            m = l + ((r - l) // 2)
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / m)

            if totalTime <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k