- [TLE Code](#tle-code)
- [Correct Code](#correct-code)
- [Editorial's Approach 2: Recursion with memoization Code](#editorials-approach-2-recursion-with-memoization-code)

<br>

[Problem](https://leetcode.com/problems/interleaving-string/)
<br>


### TLE Code

- [Submission](https://leetcode.com/problems/interleaving-string/submissions/1593580461/)
- Problems: 1) incomplete key, 2) one-sided caching

I first submitted the below code while solving the problem, but I got the **Time Limit Exceeded**. Since the code passed the provided test cases, I assumed that the implementation for memoization was wrong. I tried to debug for a bit, but couldn't figure out the reason. So, I just used a cache decorator from the Python Standard Library, and I could solve this question (`04_01_2025.py`).

There are two problems with the below code. One is that the **key for the caching dictionary is incomplete**. Here, only the `target` string is used for the key. This does not uniquely represent the current state of the recursion. Therefore, different recursion paths that lead to the same `target` get conflated.

**One-sided caching** is another issue. In the below code, we only cache when the result (or the output) of the `interleaving()` is `True`. In other words, the subproblem returning `False` is not added to the memoization storage. As a result, many failing subproblems (that are not valid interleaving strings for specific states) get recomputed over and over again. (This is the reason for the TLE)

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = set()
        def interleaving(s, t, target):
            assert len(s) + len(t) == len(target)

            if target == "":
                return True

            if target in memo:
                return True

            for i in range(1, len(s) + 1):
                if s[:i] == target[:i]:
                    if interleaving(s[i:], t, target[i:]):
                        memo.add(target[i:])
                        return True

            for i in range(1, len(t) + 1):
                if t[:i] == target[:i]:
                    if interleaving(s, t[i:], target[i:]):
                        memo.add(target[i:])
                        return True


        return interleaving(s1, s2, s3)

```
<br>

### Correct Code

- [Submission](https://leetcode.com/problems/interleaving-string/submissions/1593603270/)
- Solved previous two issues
- $n$ is the length of `s1`, and $m$ is the length of `s2`
- TC: $O(n \cdot m \cdot (n + m))$ (number of states, and string operation (i.e. python slicing) for each state)
- SC: $O(n \cdot m \cdot (n + m) + (n + m))$ -> $O(n \cdot m \cdot (n + m))$ (Adding $n + m$ is for the maximum recursion stack)

One thing to notice is that we don't have to use all parameters, that is, `s`, `t`, and `target`, as a key for the `memo` dictionary. This is because we assume (and maybe enforce) this function to be called only when `len(s) + len(t) == len(target)` as seen in the `assert` statement. Due to this invariant in the recursion, adding `target` in the key is redundant. (This means we can also use `(s, target)` or `(t, target)` as the key.)

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        def interleaving(s, t, target):
            assert len(s) + len(t) == len(target)

            if target == "":
                return True

            key = (s, t)
            if key in memo:
                return memo[key]

            for i in range(1, len(s) + 1):
                if s[:i] == target[:i]:
                    if interleaving(s[i:], t, target[i:]):
                        memo[(s[i:], t)] = True
                        return True

            for i in range(1, len(t) + 1):
                if t[:i] == target[:i]:
                    if interleaving(s, t[i:], target[i:]):
                        memo[(s, t[i:])] = True
                        return True

            memo[key] = False
            return False


        return interleaving(s1, s2, s3)
```
<br>

### Editorial's Approach 2: Recursion with memoization Code

- [Submission](https://leetcode.com/problems/interleaving-string/submissions/1593637163/) (To compare the execution time and memory usage)
- TC: $O(n \cdot m)$
- SC: $O(n \cdot m + (n + m))$ ($n + m$ for the recursion stack)

In the above codes and in `04_01_2025.py`, I used python slicing operations, and defined the parameter as the string itself for the recursive function. However, in the below code, indices are passed as the argument and they are directly used as a key for a dictionary for caching. This improves the time and space complexity since additional memory and slicing operations (looping over characters on the given string) are not needed.


```python
class Solution:
    def is_Interleave(
        self, s1: str, i: int, s2: str, j: int, s3: str, k: int, memo: list
    ) -> bool:
        if i == len(s1):
            return s2[j:] == s3[k:]
        if j == len(s2):
            return s1[i:] == s3[k:]
        if memo[i][j] >= 0:
            return memo[i][j] == 1
        ans = False
        if (
            s3[k] == s1[i]
            and self.is_Interleave(s1, i + 1, s2, j, s3, k + 1, memo)
            or s3[k] == s2[j]
            and self.is_Interleave(s1, i, s2, j + 1, s3, k + 1, memo)
        ):
            ans = True
        memo[i][j] = 1 if ans else 0
        return ans

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = [[-1] * len(s2) for _ in range(len(s1))]
        return self.is_Interleave(s1, 0, s2, 0, s3, 0, memo)

```