[Problem](https://leetcode.com/problems/find-the-duplicate-number/description/)

The problem requires 1) not to modify the input array `nums` and 2) to solve with constant extra space.

If this is not the case, we can simply:
1. use ahash table (or set), which would be $O(n)$ time and $O(n)$ space (exact algorithm is explained in [03_20_2026_technically_wrong.py](03_20_2026_technically_wrong.py)), or
2. sort the array and then find the adjancent numbers that are the same while iterating through the array, which would be $O(n log n)$ time and $O(1)$ space
<br>

Solutions shown below all satisfy the two problem requirements.

Before diving into the solutions, let's touch on the first **Follow-up question**: 

> "How can we prove that at least one duplicate number must exist in `nums`?"

We can prove this by contradiction using the [Pigeonhole Principle](https://en.wikipedia.org/wiki/Pigeonhole_principle).

Let's assume that all elements in `nums` are distinct. The **pigeons** are the $n+1$ elements, and the **pigeonholes** are the $n$ possible values $1,2,\dots,n$. Let $m$ be the number of unique values in `nums`. Then we would have $m = n+1$, but since all values lie in $[1, n]$, we must have $m \leq n$. This is a contradiction. Therefore, at least one value must repeat.


## Search on the Value Space


The intuition is that for a candidate value $k$, we count how many elements in `nums` are $\le k$. If there were no duplicates, this count would be at most $k$. If the count exceeds $k$, then by the pigeonhole principle the duplicate must lie in $[1, k]$; otherwise, it lies in $[k+1, n]$. This tells us to search over the **value range $[1, n]$** (inclusive) instead of indices.

This condition is **monotonic** over the value space, so we can [linearly scan](#linear-search) or apply [binary search](#binary-search). The smallest value $k$ for which the count exceeds $k$ is exactly the duplicate that we are looking for.


### Linear Search

[Submission](https://leetcode.com/problems/find-the-duplicate-number/submissions/1955048754/)—Time Limit Exceeded

- TC: $O(n^2)$
- SC: $O(1)$


```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1

        for k in range(1, n+1):
            cnt = sum(n <= k for n in nums)
            if cnt > k:
                return k

```


### Binary Search

[Submission](https://leetcode.com/problems/find-the-duplicate-number/submissions/1955059434/)—Runtime: 261 ms (Beats 5.04%), Memory: 33.39 MB (Beats 94.71%)

The reason it beats only 5.04% of submissions in runtime is that LeetCode doesn't check whether the input array is modified, nor does the code use only a constant extra space; thus, submitting with the code using standard functions like `sorted()`, which would be faster in practice, would be accepted.

- TC: $O(n \log n)$—The binary search takes $O(\log n)$ time, and for each iteration, we call `sum()` which takes $O(n)$ time.
- SC: $O(1)$

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        assert len(nums) >= 2
        n = len(nums) - 1
        l, r = 1, n

        while l < r:
            m = (l + r) // 2
            cnt = sum(x <= m for x in nums)
            if cnt <= m:
                l = m+1
            else:
                r = m

        assert l == r
        return r

```


## Floyd's Cycle Detection Algorithm (Floyd's Tortoise and Hare)

This solution solves the second **Follow-up question** that requires solving in $O(n)$ time.

The key idea is to treat the array as a function $f(i) = \text{nums}[i]$, which defines a pointer $i \rightarrow \text{nums}[i]$. In this way, the array behaves like a linked list. Then, this becomes a problem of finding the entrance of a cycle in a linked list ([142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/description/)).

Since there are $n+1$ indices but only $n$ possible values, by the pigeonhole principle at least two indices must map to the same value. This creates a structure where paths merge and eventually form a cycle. The entrance of this cycle corresponds to the duplicate value.

We can use Floyd’s cycle detection algorithm to solve this problem. In **Phase 1**, we move a slow pointer (tortoise) by one step and a fast pointer (hare) by two steps until they meet inside the cycle. In **Phase 2**, we reset the slow pointer to the start (or head) and move both pointers one step at a time; they will meet at the cycle entrance, which is the duplicate.
<br>

**Why It Works (Math)?**

Let $L$ be the distance from the start to the cycle entrance, $C$ be the cycle length, and $x$ be the distance from the entrance to the meeting point.

**Phase 1**: When the two pointers meet, the slow pointer has traveled $L + x$ and the fast pointer has traveled $2(L + x)$. Since the fast pointer moves twice as fast, we have: $2(L + x) = L + x + kC \Rightarrow L + x = kC$. Rearranging gives: $L = kC - x = (k-1)C + (C - x)$.

**Phase 2**: The slow pointer starts from the beginning and the fast pointer starts from the meeting point. After $L$ steps, the slow pointer reaches the cycle entrance. The fast pointer travels $(k-1)C + (C - x)$, where the full cycles $(k-1)C$ cancel out, and the remaining $(C - x)$ steps bring it to the entrance. Therefore, both pointers meet at the cycle entrance.
<br>

[Submission](https://leetcode.com/problems/find-the-duplicate-number/submissions/1955146694/)—Runtime: 26 ms (Beats 59.58%), Memory: 33.45 MB (Beats 84.62%)


- TC: $O(n)$
- SC: $O(1)$

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: find intersection inside the cycle
        # slow (tortoise): move 1 step
        # fast (hare): move 2 steps
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: find the cycle entrance (duplicate)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

```