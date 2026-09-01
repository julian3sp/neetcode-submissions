class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]

        pairs.sort(reverse=True)
        cur_time, fleets = 0, 0
        for p, s in pairs:
            destination_time = (target - p)/s
            if cur_time < destination_time:
                fleets += 1
                cur_time = destination_time

        return fleets