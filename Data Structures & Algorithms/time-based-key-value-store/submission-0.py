class TimeMap:

    def __init__(self):
        self.timeMap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # setting fallback value if nothing is found
        res = ""
        # getting [value, timestamp] pairs, falling back to [] if no key
        values = self.timeMap.get(key, [])

        # binary search through the [value, timestamp] pairs
        l = 0
        r = len(values) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
