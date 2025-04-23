[Problem](https://leetcode.com/problems/contains-duplicate-ii/)

## Using Fixed Size Hashmap (== Sliding Window Approach)


By using a sliding window approach, which is equivalent to using a hashmap with a fixed size of k, the space complexity can be optimized from $O(n)$ in `04_23_2025.py` to $O(min(n, k))$.

- [Submission](https://leetcode.com/problems/contains-duplicate-ii/submissions/1615742949/) (runtime: 33 ms, memory: 30.3 MB)
- TC: $O(n)$, where n is the number of elements in the list.
- SC: $O(min(n, k))$


```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        set_ = set()
        for i, n in enumerate(nums):
            if n in set_: return True

            set_.add(n)
            if len(set_) > k:
                set_.remove(nums[i-k])

        return False

```