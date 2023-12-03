class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        left, right = 0, len(self.store[key]) - 1

        largest_min = self.store[key][0]    # tuple
        if timestamp < largest_min[1]:
            return ""

        while left <= right:
            mid = left + (right - left) // 2
            mid_tuple = self.store[key][mid]

            if timestamp >= mid_tuple[1]:
                largest_min = mid_tuple
                left = mid + 1
            else:
                right = mid - 1

        return largest_min[0]


timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))
print(timeMap.get("foo", 3))
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))