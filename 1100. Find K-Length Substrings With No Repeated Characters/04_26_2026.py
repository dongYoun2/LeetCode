# submission: https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/submissions/1988671108/
# runtime: 31 ms (beats 5.42%), memory: 19.42 MB (beats 12.92%)
# 14 min
# used sliding window technique

# - let m be the number of unique characters in a window of size k -> m <= k
# - since the string contains only lowercase English letters, m <= 26
# - therefore, m <= min(26, k) (bounded by a constant)

# TC: O(n*k) (this is a general worst case since m <= k) -> O(n*m) -> O(n)
# SC: O(k) -> O(m) -> O(1)


# chose from a neetcode "sliding window" category.

# since we are looking for k-length substrings with no repeated characters, i fixed the window size to k. then, i used a counter to count the number of occurrences of each character in the window. 

# how did i check if the window contains no repeated characters? i iteratively checked if all values in the counter are 1 (`all(v == 1 for v in cntr.values())`). i knew that this would take O(m) time, but since m is bounded by 26 (the number of lowercase English letters), i simply did in this way.

# however, noticing that checking whether the substring contains no repeated characters can be done in constant time (thus, the total time complexity becomes true O(n)), i optimized from this solution, which can be found in "04_26_2026_optimal.py" solution.


from collections import Counter

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        n = len(s)
        if k > n:
            return 0

        cntr = Counter(s[:k])
        ans = int(all(v == 1 for v in cntr.values()))
        for i in range(k, n):
            c_left = s[i-k]
            cntr[c_left] -= 1

            if cntr[c_left] == 0:
                del cntr[c_left]
            
            c_right = s[i]
            cntr[c_right] += 1

            ans += all(v == 1 for v in cntr.values())

        return ans
