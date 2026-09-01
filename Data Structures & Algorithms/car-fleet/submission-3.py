class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]

        prev_time = 0
        fleets = 0
        cars.sort(reverse=True)
        for p, s in cars:
            cur_time = (target - p) / s
            if prev_time < cur_time:
                fleets += 1
                prev_time = cur_time
        return fleets