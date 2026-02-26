# submission: https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/1932204122/
# runtime: 71 ms (beats 39.57%), memory: 20.06 MB (beats 15.82%)
# 69 min (time including implementing "02_26_2026_wrong.py")

# TC: O(n), where n is the length of s
# SC: O(1)


# i got stuck while solving the problem. the approach i thought of was correct, but got confused while implementing. after some refreshing, i could solve it with the code below. 

# the main idea is to use a (variable size) sliding window with a hash table (counter). once the string formed by the window is an anagram of p, we add the start index (left pointer) of the window to the answer list.

# since the `Counter` object's default value is 0, we don't need to perform a membership check and simply add 1 if needed. for example, in the code below, we can simply write `cntr[s[l]] += 1` instead of checking if `s[l]` is in `cntr` and then adding 1.

# also, we can use `all()` to check if the counter has all values equal to 0 instead of manually `del` the key when the value is 0. this submitted code can be found here: https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/1932204278/

# cf.) the impelmentation below is a little different from the usual sliding window approach since the sliding window is not with a fixed size. due to the inner while loop (i.e. `while r < len(s) and cntr[s[r]] > 0`), we expand only if the next character is still “needed." this makes the code a bit more verbose and complicated. for cleaner code with fixed window size, refer to the markdown file.


from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []

        cntr = Counter(p)
        ans = []
        r = 0

        for l in range(len(s)):
            while r < len(s) and cntr[s[r]] > 0:
                cntr[s[r]] -= 1
                if cntr[s[r]] == 0: del cntr[s[r]]
                r += 1
            
            if not cntr:
                ans.append(l)
                cntr[s[l]] = 1
            else:
                if s[l] not in cntr:
                    cntr[s[l]] = 1
                else:
                    cntr[s[l]] += 1

        return ans
