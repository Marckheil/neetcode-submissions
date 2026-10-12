class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr = self.store[key]
        res = ""
        
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:    # this save is at or before what we asked
                res = arr[mid][1]           # it's a candidate, remember its value
                left = mid + 1              # but try to find a later one still valid
            else:                           # this save is too late
                right = mid - 1             # look earlier
        return res
        
