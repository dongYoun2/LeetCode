# problem: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
# 57 min

# i thought of solving with a sliding window approach with hash table (counter), and the approach is correct. however, the implementation is wrong. it fails on the first test case, where s = "cbaebabacd" and p = "abc". the code got messy because i used two while loops and manually updating the indices. it took so long to debug, but wasn't able to fix it. after taking a break, and reconsidering my algorithm from scratch, i could solve with the code in "02_26_2026.py".


from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []

        cntr_backup = Counter(p)
        cntr = Counter(p)
        ans = []
        l = r = 0

        while l < len(s) and r < len(s):
            while r < len(s) and cntr[s[r]] > 0:
                cntr[s[r]] -= 1
                if cntr[s[r]] == 0: del cntr[s[r]]
                r += 1
                
            if not cntr:
                ans.append(l)
                cntr[s[l]] = 1
                l += 1
            else:
                r += 1
                l = r
                cntr = cntr_backup.copy()

        return ans
