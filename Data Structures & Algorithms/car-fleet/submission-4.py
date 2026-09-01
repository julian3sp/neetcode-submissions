class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse = True)
        fleets = 1
        cur_fastest_time = (target - cars[0][0]) / cars[0][1]

        for i in range(1, len(cars)):
            currCar = cars[i]
            currTime = (target - cars[i][0]) / cars[i][1]
            if currTime > cur_fastest_time:
                fleets += 1
                cur_fastest_time = currTime
        return fleets


