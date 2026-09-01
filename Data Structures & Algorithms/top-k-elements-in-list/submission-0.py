class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            map[n] = 1 + map.get(n, 0)
        # map frequency of each number in nums
        for key, val in map.items():
            freq[val].append(key)
        # tells us which items appear x amount of times
        # ex. freq[1] gives us a list of the values that appear once
        result = []
        for i in range(len(freq) - 1, 0, -1):
            # move backwards 
            for n in freq[i]:
                # iterate through each list since multiple elements can 
                # occur a certain amount of times
                result.append(n)
                if len(result) == k:
                    return result
