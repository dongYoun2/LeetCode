[Problem](https://leetcode.com/problems/permutations/description/)

## (Optimized) Backtracking

`01_21_2026.py` is the optimized version of the `05_19_2025_backtracking.py`. (Refer to the `01_21_2026.py` file for the code)

The main optimization is passing a **set** `seen` down down to a recursive function instead of:
1. Passing a list of candidates (`cands` in `05_19_2025_backtracking.py`) constructed by slicing, or
2. Performing membership check on a direct list of numbers (`curr_perm` in `05_19_2025_backtracking.py` or `curr` in `01_21_2026.py`).

Because of this, we can:
1. Avoid passing candidate numbers and using slicing operations, and
2. Perform a membership check in $O(1)$ time.
<br>

- [Submission](https://leetcode.com/problems/permutations/submissions/1892653586/) (Runtime: 3 ms, Memory: 19.70 MB)
- TC: $O(n \cdot n!)$, where n is the length of `nums` ($n!$ number of permutations with length $n$ for each of them).
- SC: $O(n + n + n)$ -> $O(n)$ (for the recursion stack, `seen` set, and `curr` list, respectively).



cf.) A code for not passing a candidate numbers list but performing membership check on a direct list of numbers can be found [here](https://leetcode.com/problems/permutations/submissions/1638470472/) (Runtime: 0 ms, Memory: 17.98 MB). This solutions solves in $O(n^2 \cdot n!)$ time. It's better than the `05_19_2025_backtracking.py`, but worse than the `01_21_2026.py` in terms of time complexity.