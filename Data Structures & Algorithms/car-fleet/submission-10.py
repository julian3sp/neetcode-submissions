class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        slowest_time = 0
        fleets = 0

        for car in cars:
            time = (target - car[0]) / car[1]
            if slowest_time < time:
                fleets +=1
                slowest_time = time
                
        return fleets