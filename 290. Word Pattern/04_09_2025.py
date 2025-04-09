# problem: https://leetcode.com/problems/word-pattern/
# submission: https://leetcode.com/problems/word-pattern/submissions/1601902260/

# 8 min
# TC: O(n + m), where n for the pattern and m for the string "s"
# SC: O(n + m)

# From LeetCode Top Interview 150 - Hashmap

# This problem is similar to the "Isomorphic Strings" problem, and I solved it yesterday. I was impressed by its Editorial Approach 2, so I was able to solve this problem with that approach.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def transform(arr):
            to_idx = {}
            ret_arr = []
            for i, e in enumerate(arr):
                if e in to_idx:
                    ret_arr.append(to_idx[e])
                else:
                    to_idx[e] = str(i)
                    ret_arr.append(str(i))

            return " ".join(ret_arr)    # without whitespace, "10" is ambiguous since it could mean two different indices 1 and 0, or one index 10.

        return transform(list(pattern)) == transform(s.split(" "))
