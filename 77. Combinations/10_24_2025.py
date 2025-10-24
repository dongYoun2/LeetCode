# submission: https://leetcode.com/problems/combinations/submissions/1810600669/
# runtime: 123 ms, memory: 59.79 MB

# 11 min
# time and space complexity are the same as the "fully optimized backtracking" solution described in the markdown file.


# solved with backtracking + pruning. though i knew that i can easily solve with python's `combinations` function, i wanted to practice the backtracking approach. note that it only prunes based on the second criterion mentioned in the markdown file (there are two pruning criteria for this problem). for more details, refer to the makrdown file.

# cf.) also note that it's important to copy the current state when appending to the answer list.


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def dfs(curr):
            if len(curr) == k:
                ans.append(curr[:]) # need to copy current state
                return

            if curr and n - curr[-1] < k - len(curr):    # prune
                return

            lo = 1
            if curr: lo = curr[-1] + 1

            for num in range(lo, n + 1):
                curr.append(num)
                dfs(curr)
                curr.pop()


        dfs([])
        return ans
