[Problem](https://leetcode.com/problems/time-based-key-value-store/description/)


## Hash Table + Linear Search

Refer to the [01_26_2026_linear_search.py](01_26_2026_linear_search.py) file.



## Hash Table + Binary Search

Unlike [01_26_2026_binary_search.py](01_26_2026_binary_search.py), we can avoid accessing `m + 1` index by keep looping until `l` and `r` meet. In other words, there is no `return` statement in the loop. Moreover, since we are not accessing `m + 1` index, we don't need to check the edge cases to early return as a guardrail. Runtime slightly increased from 44 ms to 159 ms, but the code is more readable and concise.

- [Submission](https://leetcode.com/problems/time-based-key-value-store/submissions/1898106433/) (Runtime: 159 ms, Memory: 68.93 MB)
- TC: 
  - set operation: $O(1)$
  - get operation: $O(n_{key} \log n_{key})$ (worst case per key), where $n_{key}$ is the number of values for the key
- SC: $O(n)$, where $n$ is the total number of set calls across all keys

```python
from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)  # key -> List[(ts, val)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        if not arr:
            return ""

        # Find rightmost index with arr[i][0] <= timestamp
        lo, hi = 0, len(arr) - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_ts = arr[mid][0]
            if mid_ts <= timestamp:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return arr[ans][1] if ans != -1 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

```


Insead of manually implementing binary search, we ca use Python's built-in `bisect_right` function in **`bisect` module**. 

Note that we need to use `chr(127)`, which is the ASCII value larger than all printable characters, to directly compare tuples only on the timestamp field. I have tried extracting `timestamp` field with list comprehension, and using that list to call `bisect_right`, but it caused **TLE** since list comprehension takes $O(n_{key})$ time and $O(n_{key})$ space. Failed submission can be found [here](https://leetcode.com/problems/time-based-key-value-store/submissions/1898106685/).

- [Submission](https://leetcode.com/problems/time-based-key-value-store/submissions/1898106433/) (Runtime: 159 ms, Memory: 68.93 MB)
- Time and space complexity are the same as the above code.

```python
from collections import defaultdict
from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)  # key -> [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        if not arr:
            return ""

        # bisect on (timestamp, high-sentinel)
        idx = bisect_right(arr, (timestamp, chr(127))) - 1
        return arr[idx][1] if idx >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

```