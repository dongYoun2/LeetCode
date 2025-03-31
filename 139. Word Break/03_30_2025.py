# problem: https://leetcode.com/problems/word-break/
# submission: https://leetcode.com/problems/word-break/submissions/1591524083/

# 20 min
# |s|: the number of characters in the string "s"
# w: the number of words in the wordDict
# l: the average length of words in the wordDict
# TC: O(w*l + |s|^3) (w*lfor creating the "w_dict" set, |s|^2 for the looping over "s" and "true_indices" (b/c in worst-case, "true_indices" list can be of length |s|), and |s| for the slicing operation.)
# SC: O(w*l + 2*|s|) -> O(w*l + |s|) (w*l for the "w_dict" set, and |s| for the "dp" list and "true_indices" list, respectively)

# Knowing that I had to use the dynamic programming algorithm, I tried to iterate from the beginning of the string "s" to the end, and for each character, I checked if the substring from the last "true" index to the current index was in the word dictionary. If it was, I marked the current index as "true" in the "dp" list.

# There is another dynamic programming approach. Refer to the Editorial section's Approach 2 (top-down) and Approach 3 (bottom-up) for more details.

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
