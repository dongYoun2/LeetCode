# submission: https://leetcode.com/problems/word-break/submissions/1591524083/
# runtime: 7 ms (Beats 22.37%), memory: 17.91 MB (Beats 57.31%)
# 20 min

# with the same symbols in the 04_25_2024.py,
# TC: O(m*k + n^3) (m*k for creating the "w_dict" set, n^2 for substring checks, which is done by looping over indices `i` and all entries in `true_indices` (b/c in worst-case, `true_indices` list can grow to length n), and each check involves python string slice costing O(n).)
# SC: O(m*k + 2*n) -> O(m*k + n) (m*k for the "w_dict" set, and n for the "dp" list and "true_indices" list, respectively)

# Knowing that I had to use the dynamic programming algorithm, I tried to iterate from the beginning of the string "s" to the end, and for each character, I checked if the substring from the last "true" index to the current index was in the word dictionary. If it was in the dictionary, I marked the current index as "true" in the "dp" list.

# There are other dynamic programming approaches. Refer to the Editorial section's Approach 2 (top-down) and Approach 3 (bottom-up) for more details.

# cf.) The below code is almost the same as the LeetCode Editorial section's "Approach 5: A Different DP")


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        w_dict = set(wordDict)
        n = len(s)
        dp = [False] * n
        true_indices = [-1]

        for i in range(n):
            dp[i] = any(s[j+1:i+1] in w_dict for j in true_indices)
            if dp[i]:
                true_indices.append(i)

        return dp[-1]


# notes while solving:

# l e e t c o d e
# f f f t

# c a t s a n d o g
# f f t t

# s.length <= 300
# n^2

# K: set of all previous 'true' ended indices
# dp[curr_idx] = any([s[i+1:curr_idx] in word_dict for i in K])
