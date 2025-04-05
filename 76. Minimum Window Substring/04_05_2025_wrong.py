# problem: https://leetcode.com/problems/minimum-window-substring/
# submission: https://leetcode.com/problems/minimum-window-substring/submissions/1597747094 (This includes a test case that fails on this code)

# 90 min (including around 25 min for the brute-force solution): but couldn't solve it

# Although I knew that this was a sliding window problem, I couldn't solve it. I first implemented it with a brute-force solution in the "04_05_2025_naive.py" file. Then, I tried to optimize it with a sliding window approach, but couldn't do it.

# In the code below, I extended the window by moving the right pointer until I found a valid string, that is, a substring that contains all the characters of "t". Then, I shrank the window by moving the left pointer until I found the character that's also in "t".

# However, right now, after looking at the four hints provided in the problem appendix, I realized that I should have kept moving the left pointer while ensuring the window covers all characters of "t", that is, while maintaining the window as a valid string, to minimize the substring length. This is the main reason why my code didn't work properly.


from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)

        if n > m:
            return ""

        t_cntr = Counter(t)
        t_cntr_cp = t_cntr.copy()

        min_len  = float('inf')
        substr_s = substr_e = -1

        window_s = 0
        while window_s < m and s[window_s] not in t_cntr:
            window_s += 1

        if window_s >= m:
            return ""

        cnt = n
        window_e = window_s
        while window_e < m:
            c_end = s[window_e]
            # print(cnt)
            # print(s[window_s:window_e+1])
            # print(t_cntr)

            if t_cntr.get(c_end, -1) == 0 and c_end == s[window_s]:
                while True:
                    window_s += 1
                    if window_s >= m or (s[window_s] in t_cntr):
                        break

            if t_cntr.get(c_end, 0) > 0:
                t_cntr[c_end] -= 1
                cnt -= 1
                # print(cnt)

                if cnt == 0:
                    window_len = window_e - window_s + 1
                    # print(s[window_s:window_e+1])

                    if window_len < min_len:
                        min_len = window_len
                        substr_s, substr_e = window_s, window_e

                    cnt += 1
                    t_cntr[s[window_s]] += 1

                    while True:
                        window_s += 1
                        if window_s >= m or (s[window_s] in t_cntr):
                            break

            window_e += 1


        return s[substr_s:substr_e+1] if substr_s != -1 else ""
