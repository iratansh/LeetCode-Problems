class TimeMap:
    def __init__(self):
        self.map  = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        vals = self.map.get(key, [])

        start, end = 0, len(vals) - 1
        while start <= end:
            mid = (start + end) // 2

            if vals[mid][1] <= timestamp:
                ans = vals[mid][0]
                start = mid + 1
            else:
                end = mid - 1
        
        return ans
