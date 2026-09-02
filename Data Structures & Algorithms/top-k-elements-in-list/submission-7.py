class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        frequency = [[] for i in range(len(nums) + 1)]
        res = []

        for num, freq in counter.items():
            frequency[freq].append(num)

        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                res.append(num)
                if len(res) == k:
                    return res

        


        




