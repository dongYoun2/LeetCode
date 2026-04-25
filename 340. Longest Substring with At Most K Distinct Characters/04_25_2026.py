# submission: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/submissions/1987770277/
# runtime: 559 ms (beats 5.02%), memory: 19.61 MB (beats 5.15%)
# 6 min
# solved with the sliding window technique

# TC: O(n*k), where n is the length of s and k is the maximum number of distinct characters given in the problem
# SC: O(k)


# chose from a neetcode "sliding window" category.

# this problem is exactly the same as the problem "159. Longest Substring with At Most Two Distinct Characters", except that the maximum number of distinct characters is given as a parameter `k`. similar to this previous problem, i planned to use `del` to remove the key once it reaches zero. 

# meanwhile, noticing a unary plus operator `+` on a counter object automatically removes all keys with zero or negative counts, i employed this technique instead. however, the real problem is that it takes O(k) time since it creates a new counter object by iterating over all keys in the original counter object. therefore, entire solution takes O(n*k) time. optimized solution with O(n) time can be found here: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/submissions/1987770820/

# cf.) at least, i learned that we can use the unary plus operator on a counter object.


from collections import Counter

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        left = ans = 0
        cntr = Counter()
        for right in range(n):
            cntr[s[right]] += 1

            # uniary plus operator automatically removes all keys with zero or negative counts
            while len(+cntr) > k:
                cntr[s[left]] -= 1
                left += 1
            
            ans = max(ans, right-left+1)
        
        return ans
