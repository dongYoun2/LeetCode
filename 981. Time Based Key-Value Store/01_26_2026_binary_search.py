# submission: https://leetcode.com/problems/time-based-key-value-store/submissions/1898089178/
# runtime: 44 ms, memory: 69.24 MB
# 23 min

# refer to the README.md for the time and space complexity analysis


# after solving with linear search (01_26_2026_linear_search.py), i used binary search noting that timestamps are sorted. since we are looking for the largest timestamp less than or equal to the given timestamp, i though of accessing `m + 1` index in the loop. to achieve this, i needed to early return cases where the timestamp is smaller than the first timestamp or larger than the last timestamp, and the empty list case, which ensures `arr` afterwards will contain at least 2 elements.

# however, this edge case handling is a bit messy, and we can make code more readable by without accessing `m + 1` index in the loop. for more details, refer to the README.md.


from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.table = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.table[key]

        if len(arr) == 0 or arr[0][0] > timestamp:
            return ""
        if arr[-1][0] <= timestamp:
            return arr[-1][1]

        assert len(arr) > 2

        l, r = 0, len(arr) - 1
        while l < r:
            m = (l + r) // 2

            if arr[m][0] <= timestamp:
                if arr[m+1][0] > timestamp:
                    return arr[m][1]
                else:
                    l = m + 1
            else:
                r = m  - 1

        return arr[r][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)