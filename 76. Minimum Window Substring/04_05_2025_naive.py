# problem: https://leetcode.com/problems/minimum-window-substring/
# submission: https://leetcode.com/problems/minimum-window-substring/submissions/1597708217/ (This submission includes a TLE test case)

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)

        if n > m:
            return ""

        t_cntr = Counter(t)
        t_cntr_cp = t_cntr.copy()

        valid_chars = set(t)

        pos_list = []
        for i, c in enumerate(s):
            if c in valid_chars:
                pos_list.append((i, c))

        min_len = float('inf')
        start = end = None

        for i in range(len(pos_list)):
            cnt = len(valid_chars)
            t_cntr = t_cntr_cp.copy()

            idx_start, c_start = pos_list[i]

            for j in range(i, len(pos_list)):
                idx_end, c_end = pos_list[j]

                if t_cntr[c_end] > 0:
                    t_cntr[c_end] -= 1

                    if t_cntr[c_end] == 0:
                        cnt -= 1

                        if cnt == 0:
                            window_len = idx_end - idx_start + 1
                            if window_len < min_len:
                                min_len = window_len
                                start, end = idx_start, idx_end
                                break

        return s[start:end+1] if start is not None else ""

# notes while solving:
# 1 3   5   6  20
# A C   C   B   A