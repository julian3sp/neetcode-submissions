class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        result = []
        frequency = [[] for i in range(len(nums) + 1)]

        for key, val in hashmap.items():
            frequency[val].append(key)

        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                result.append(n)
            if len(result) == k:
                break
        return result