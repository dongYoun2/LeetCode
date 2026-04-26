# submission: https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/submissions/1988677423/
# runtime: 19 ms (beats 11.67%), memory: 19.40 MB (beats 50.83%)
# 20 min (includes time writing the "04_26_2026.py" solution)
# used sliding window technique

# TC: O(n) (true linear time unlike the "04_26_2026.py" solution)
# SC: O(k) -> O(m) -> O(1), where m is the number of unique characters in a window of size k -> m <= min(26, k); 26 is the number of lowercase English letters


# chose from a neetcode "sliding window" category.

# optimized from the "04_26_2026.py" solution. the key idea is instead of iteratively checking all the counter values for each and every window, we can simply maintain another set (`repeated`) to keep track of the characters that are repeated in the window. so, every time we remove the leftmost character or add the rightmost character, we check whether the character needs to be removed or added to the `repeated` set.

# however, there is a much simpler way to optimize the TC to true O(n) time from "04_26_2026.py" solution. this can be found in the README.md file.


from collections import Counter

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        n = len(s)
        if k > n:
            return 0

        cntr = Counter(s[:k])
        repeated = {k for k, v in cntr.items() if v > 1}
        ans = int(all(v == 1 for v in cntr.values()))
        
        for i in range(k, n):
            c_left = s[i-k]
            cntr[c_left] -= 1

            if cntr[c_left] == 0:
                del cntr[c_left]
            elif cntr[c_left] == 1:
                repeated.remove(c_left)
            
            c_right = s[i]
            cntr[c_right] += 1

            if cntr[c_right] > 1:
                repeated.add(c_right)

            ans += int(not repeated)

        return ans
