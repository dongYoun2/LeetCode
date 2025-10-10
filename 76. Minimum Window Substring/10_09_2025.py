# submission: https://leetcode.com/problems/minimum-window-substring/submissions/1796524360/
# runtime: 183 ms, memory: 18.22 MB

# 106 min
# TC: O(m + n), where m is the length of s and n is the length of t
# SC: O(52) -> O(1), upper and lower case english letters


# i remembered that i couldn't solve this problem on 04/05/2025 though i knew which algorithm to use beforehand. i knew it's a sliding window problem this time as well. i finally solved it, but it took so long and the code is very verbose. i spent a lot of time thinking the logic (when to update the left pointer etc.), implementing, and debugging. i have gone throughh many iterations, and trial and errors.

# the cuase of the verbosity is that when shrinking the window, i check if the current substring is a valid substring everytime the left pointer character is in 't', including the first time. however, i realized that this can be optimized by checking only once after shrinking the window.

# cf.) for more readable, concise, and interview-friendly code, refer to the markdown file.


from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        assert s and t

        cntr = Counter(t)
        remaining = len(t)

        i = 0   # find first index of s where s[index] is in 't'
        while i < len(s) and s[i] not in cntr:
            i += 1

        if i >= len(s):
            return ''

        if len(t) == 1:
            return s[i]

        cntr[s[i]] -= 1; remaining -= 1
        min_len = float('inf')
        ans = s[i]
        left, right = i, i + 1
        while right < len(s):
            curr_c = s[right]
            if curr_c in cntr:
                if cntr[curr_c] <= 0:
                    cntr[curr_c] -= 1
                else:
                    cntr[curr_c] -= 1; remaining -= 1
                    if remaining == 0:
                        assert cntr[curr_c] == 0

                        candidate = s[left:right+1]
                        if len(candidate) < min_len:
                            ans = candidate
                            min_len = len(candidate)

                        assert s[left] in cntr
                        cntr[s[left]] += 1
                        if cntr[s[left]] > 0:
                            remaining += 1
                        left += 1

                        while left < len(s):
                            if s[left] in cntr:
                                if remaining > 0:
                                    break

                                candidate = s[left:right+1]
                                if len(candidate) < min_len:
                                    ans = candidate
                                    min_len = len(candidate)

                                cntr[s[left]] += 1
                                if cntr[s[left]] > 0:
                                    remaining += 1
                            left += 1

            right += 1

        return ans if min_len != float('inf') else ''
