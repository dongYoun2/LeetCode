# submission: https://leetcode.com/problems/time-based-key-value-store/submissions/1898082534/
# runtime: 28 ms, memory: 68.94 MB
# 11 min

# TC:
# - set operation: O(1)
# - get operation: O(n_{key}) (worst case per key), where n_{key} is the number of values for the key
# SC: O(n), where n is the total number of set calls across all keys


# i directly thought of using hash table and performing linear scan for the specific key. i expected this would cause TLE, and planned to use binary search to optimize the get operation (instead of linear search) since timestamps are sorted. however, the code below (hash table + linear scan) actaully passed all test cases.


from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.table = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.table[key]
        for i in range(len(arr) - 1, -1, -1):
            if arr[i][0] <= timestamp:
                return arr[i][1]
        
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
