This document explains the solution for the follow-up question of the LeetCode [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/).

## Initial Approach: Hash Table + Linear Search
The original code (`03_22_2025.py`), which uses two-pointer algorithm is inefficient when there are many query strings — that is, $s_1, s_2, \cdots, s_k$, where $k \geq 10^9$. The time complexity becomes $O(k * |t|)$. This means for each and every query, we have to scan the target string.

To try to optimize this, I coded up like below.
```python
# took 29 min

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_char_to_index = {}

        for i, c in enumerate(t):
            if c in t_char_to_index:
                t_char_to_index[c].append(i)
            else:
                t_char_to_index[c] = [i]

        pos = -1
        for c in s:
            try:
                t_indicies_of_c = t_char_to_index[c]

                new_pos = -1
                for t_idx in t_indicies_of_c:
                    if t_idx > pos:
                        new_pos = t_idx
                        break

                if new_pos < pos:
                    return False

                pos = new_pos
            except: # when 'c' keyError for 't_char_to_index' dict
                return False

        return True

# notes while solving this problem

# abcb
# aaabbcbb
```

A logic itself for this code is correct, but there's still a room for further optimization. The approach is on the right track in that it —

1. uses **hash table**
2. searches index of current source string's character in a target string **greedily**.

A **time complexity** for this code is $O(t + k * |s| * |t|)$, which is bounded by $O(k * |s| * |t|)$. It seems like it got worsen than the two-pointer algorithm since the |s| is additionally introduced. There can be two scenarios:

1. **average case**: characters of target string are well distributed over the hash map keys (length of each list in a hasp map is similar)
2. **worst case**: hasp map's lists are skewed (target string has many (or all) repeated characters)


## Optimizing Further: Binary Search Over Linear Search

For the worst case, two-pointer algorithm ($O(k * |t|)$) performs better. Therefore, we have to optimize the worst case scenario. How can we do this? since each list in the hash map is sorted, we can use **binary search** instead of **linear search**. This will reduce the time complexity to $O(t + k * |s| * log |t|)$, which is bounded by $O(k * |s| * log |t|)$.

This is more efficient than the two-pointer algorithm when there are many queries $s_1, s_2, \cdots, s_k$.

It seems like there exists a case where two-pointer algorithm still performs better — that is, when $|s| \gt |t|$. This can be prevented using the length-based early return.

Fully optimized code is as follows:
```python
import bisect


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        t_char_to_index = {}
        for i, c in enumerate(t):
            if c in t_char_to_index:
                t_char_to_index[c].append(i)
            else:
                t_char_to_index[c] = [i]

        target_index = -1
        for c in s:
            try:
                index_list = t_char_to_index[c]
                find_idx = bisect.bisect_right(index_list, target_index)

                if find_idx == len(index_list):
                    return False

                target_index = index_list[find_idx]
            except: # when 'c' keyError for 't_char_to_index' dict
                return False

        return True
```

cf.) This algorithm is the same as the approach shown in the `Editorial` section's **Approach 3: Greedy Match with Character Indices Hashmap**. Further details can be found there as well.