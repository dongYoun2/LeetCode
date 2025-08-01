# submission: https://leetcode.com/problems/edit-distance/submissions/1707604205/

# 40 min
# TC: O(n * m), where n is the length of word1 and m is the length of word2
# SC: O(n * m) for the dp array

# From LeetCode Top Interview 150 - Multidimensional DP

# This is a Levenshtein distance problem except for that we don't have to track the operations (insert, delete, replace) but just return the minimum number of operations needed. I studied this algorithm while working at Return Zero Inc., since I was looking for the golang implementation of Levenshtein distance to compare ASR results with the human transcription.

# I forgot the details since it's been a while, but I knew that it's a dynamic programming problem. I defined dp[i][j] as the minimum edit distance between word1[0..i] and word2[0..j] (i and j are inclusive). Then, we can notice that the general recurrence formula is:

# deletion: dp[i][j] = dp[i-1][j] + 1
# insertion: dp[i][j] = dp[i][j-1] + 1
# substitution: dp[i][j] = dp[i-1][j-1] + (word1[i] != word2[j])

# This is implemented in the nested for loop (last for loop) below.

# However, the messy part is when filling out the first row and column of the dp array. I need to have a flag variable (`found`) to ensure only the first time word1[0] == word2[j] (when filling out the first row) lets me "stop paying" for a replacement cost. The concrete example is as follows:

# word1 = "h", word2 = "ahh"
# 1) dp[0][0]: “h” -> “a” is 1 (replace).
# 2) j=1, word2[1] == 'h' == word1[0] and found is False → set dp[0][1] = dp[0][0] = 1, and set found = True. That corresponds to inserting 'a' before the 'h', so cost 1.
# 3) j=2, word2[2] == 'h' but found is now True, so you go to the else: dp[0][2] = dp[0][1] + 1 = 2. You need one more insertion ('h' at end) to get "ahh" from "h".

# If found is not used, dp[0][2] wound be 1 since word1[0] and word2[2] are the same, but we still need to insert 'h' at the end.

# The simple workaround (or more commonly used approach) is to use dp array with size (n+1) x (m+1), where you include the empty prefix explicitly. I noticed this better formulation after writing below code. Refer to the markdown file for this better approach and for more details.


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        if n == 0 and m == 0:
            return 0
        elif n == 0:
            return m
        elif m == 0:
            return n

        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1 if word1[0] != word2[0] else 0

        # fill out the first row
        found = False
        for j in range(1, m):
            if word1[0] == word2[j] and not found:
                dp[0][j] = dp[0][j-1]
                found = True
            else:
                dp[0][j] = dp[0][j-1] + 1

        # fill out the first column
        found = False
        for i in range(1, n):
            if word1[i] == word2[0] and not found:
                dp[i][0] = dp[i-1][0]
                found = True
            else:
                dp[i][0] = dp[i-1][0] + 1

        for i in range(1, n):
            for j in range(1, m):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        return dp[-1][-1]

# notes while solving:
#    r  o  s
# h  1  2  3
# o  2  1  2
# r  2  2  2
# s  3  3  2
# e  4  4  3