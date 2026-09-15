class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap.get(key, [])
        l = 0
        r = len(values) - 1
        res = ""

        while l <= r:
            mid = l + ((r - l) // 2)

            if values[mid][1] < timestamp:
                res = values[mid][0]
                l = mid + 1
            elif values[mid][1] > timestamp:
                r = mid - 1
            else:
                return values[mid][0]
        return res
