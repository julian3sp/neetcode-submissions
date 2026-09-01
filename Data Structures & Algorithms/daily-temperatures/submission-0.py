class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        length = len(temperatures)

        for i in range(length):
            days = 0
            for j in range(i + 1, length):
                if temperatures[j] > temperatures[i]:
                    days = j - i
                    res.append(j - i)
                    break
            if days == 0:
                res.append(days)    
        return res