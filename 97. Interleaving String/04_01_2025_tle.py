# submission: https://leetcode.com/problems/interleaving-string/submissions/1593580461/
# time limit exceeded
# 28 min
# wrong top-down dfs + memoization approach (but close though)


# two problems exist in the code:
# 1. incomplete key: `target` alone does not identify the state. The same `target` can occur with different remaining `s` and `t`, so different recursion paths that lead to the same `target` get conflated.
# 2. one-sided caching: it only caches successful states (when `interleaving(...)` returns `True`). in other words, subproblem returning `False` is not cached. hence, failed states are recomputed repeatedly, so memoization does not effectively prune the search (this is the cause of the TLE).

# "04_01_2025.py" is the solution that fixes these problems by @cache decorator.


# cf.) here is another correct implementation that fixes the above problems by using a dictionary for a memoization: https://leetcode.com/problems/interleaving-string/submissions/1593603270/—runtime: 251 ms (beats 5.38%), memory: 19.35 MB (beats 72.52%)

# in the above submitted code, one point to notice is that we don't have to use all parameters, that is, `s`, `t`, and `target`, as a key for the `memo` dictionary. This is because we assume (and maybe enforce) this function to be called only when `len(s) + len(t) == len(target)` as seen in the `assert` statement. Due to this invariant, we can simply use `(s, t)` as the key (or we can also use `(s, target)` or `(t, target)`).


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
