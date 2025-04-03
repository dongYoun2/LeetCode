# problem: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# submission: https://leetcode.com/problems/substring-with-concatenation-of-all-words/submissions/1594933402/

# 84 min
# L: length of `words`
# W: length of each word (they are all the same length (fixed))
# S: length of `s`
# TC: O(W*L + W*(S/W)*2) -> O(W*L + S) (W*L for counter, S times of sliding window process, and (S/W)*2 for each sliding window process)
# SC: O(W*L) (counter)

# I knew that I had to use the sliding window algorithm since I was solving problems based on the algorithm type.

# Implementing this was very tough. For this kind of problem, I believe it is really important to approach things logically and go step by step—i.e., accurately deciding when to move the start and end pointers of the window, and what exactly needs to happen after each move.

# At first, I just jumped into coding without really thinking through the logical flow. One of the issues with this is that it gets hard to debug. So I removed the whole and restarted from scratch (if I had done it properly at first, I could save time). Then, debugging became much more manageable, and finally I was able to solve the problem.

# I learned that I have to take the time to think logically about what should occur at certain steps so that every line of code has a clear purpose. I also realized that using clear and meaningful variable names—i.e., `i` to `window_s`—helps this process a lot.

# Consult the markdown for the debugging process and intermediate codes (which are wrong) that I went through before arriving at the final one below.

from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_cnt, word_size = len(words), len(words[0])
        ans = []

        if len(s) < word_cnt * word_size:   # early return
            return ans

        def find_concat_strings(start):
            word_cntr = Counter(words)
            word_cntr_cp = word_cntr.copy()

            window_s = start
            window_e = start + word_size - 1
            while window_e < len(s) and window_s < len(s):
                last_word = s[window_e+1-word_size:window_e+1]

                if last_word not in word_cntr:  # renew window's start and end to the next word of the last (rightmost) word
                    word_cntr = word_cntr_cp.copy()

                    window_s = window_e + 1
                    window_e += word_size
                    continue

                # last_word exists in word_cntr from here

                if word_cntr[last_word] > 0:    # valid last_word (rightmost word)
                    word_cntr[last_word] -= 1
                else:
                    first_word = s[window_s:window_s+word_size]
                    word_cntr[first_word] += 1
                    window_s += word_size
                    continue

                if window_e - window_s + 1 == word_cnt * word_size: # found concatenated string
                    ans.append(window_s)

                window_e += word_size

        for i in range(word_size):  # perform sliding window process for all possible starting points
            find_concat_strings(i)

        return ans