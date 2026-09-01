class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        frequency = [[] for i in range(len(nums) + 1)]
        res = []

        for num in counter:
            frequency[counter[num]].append(num)

        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                k -= 1
                res.append(num)
                if k == 0:
                    return res
            