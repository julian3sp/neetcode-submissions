class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
            # we use this because it allows for O(1) lookup of values
            # we are looking for the correct value, we can find the index after
        for j in range(len(nums)):
            complement = target - nums[j]
            # calculate number were looking for
            if complement in map and j != map[complement]:
                # if our number is in the map and the index of it != j
                return [j, map[complement]]
    # return empty array if not found
        return []