class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]

        cur_fastest_time = 0
        fleets = 0
        cars.sort(reverse=True)
        for p, s in cars:
            destination_time = (target - p) / s
            if cur_fastest_time < destination_time:
                fleets += 1
                cur_fastest_time = destination_time
        return fleets