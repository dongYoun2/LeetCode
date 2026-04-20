# submission: https://leetcode.com/problems/longest-nice-substring/submissions/1983544931/
# runtime: 214 ms (beats 5.05%), memory: 19.35 MB (beats 44.15%)
# 29 min
# brute-force solution

# TC: O(n^3)
# SC: O(26 * 2) -> O(1) (two lower and upper case alphabet sets)


# chose from the "sliding window" category.

# i directly think of using the sliding window technique. however, i couldn't think of how to implement it. so, given the input constraints (n <= 100), where up to O(n^3) is acceptable, i simply decided to code up the brute-force solution.

# the brute-force solution iterates through all possible substrings and check if it is a nice substring. iterating through all possible substrings takes O(n^2) time. then, i iterated through all characters of the current substring to create two sets (loewr and upper case alphabet set each), and this takes O(n) time. checking if these two sets are equal takes constant (O(26)) time.

# however, we can do better. first method is to properly utilize the hash table (or set) on top of the brute-force solution. anthoer approach is to employ the divide and conquer algorithm. both of these approaches reduce the time complexity to O(n^2) time. for more details, refer to the REAMDE.md.

# cf.) though i chose from the "sliding window" category, sliding window technique is hard to apply to this problem (many comments in a dicussion section mentions this). i decided to choose the algorithm category from the neetcode website instead of leetcode, lol.


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        ans_i, ans_j = 0, -1

        for i in range(n):
            for j in range(i+1, n):
                lower, upper = set(), set()
                for k in range(i, j+1):
                    if s[k].islower():
                        lower.add(s[k])
                    else:
                        upper.add(s[k])
                if lower == {e.lower() for e in upper} and j-i > ans_j - ans_i:
                    ans_i, ans_j = i, j
        
        return s[ans_i:ans_j+1]
