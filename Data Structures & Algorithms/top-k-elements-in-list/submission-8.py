class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range((len(nums) + 1))]
        counter = Counter(nums)
        res = []

        for num, count in counter.items():
            freq[count].append(num)

        for i in range(len(freq) - 1, -1, -1):
            if len(res) == k:
                return res
            for num in freq[i]:
                res.append(num)
        return res

