# submission: https://leetcode.com/problems/substring-with-concatenation-of-all-words/submissions/1790452725/
# time limit exceeded

# TC: O(n*m) where n is the length of `s` and m is the length of `words` (number of total words).
# SC: O(U), where U is the number of unique words in `words`.


# this is a brute-force solution with tiny optimization.


from collections import Counter
from copy import deepcopy

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        assert len(words) >= 1
        word_len = len(words[0])

        ans = []
        curr_words = []
        cntr = Counter(words)
        copied_cntr = deepcopy(cntr)
        start = i = 0

        while i < len(s):
            curr_word = s[i:i+word_len]
            if curr_word in cntr and cntr[curr_word] > 0:
                curr_words.append(curr_word)
                cntr[curr_word] -= 1

                if len(curr_words) != len(words):
                    i += word_len
                    continue
                else:
                    ans.append(start)

            curr_words = []
            cntr = deepcopy(copied_cntr)
            start += 1
            i = start

        return ans


# notes while solving:
# len(words) <= 50K
# len(words[i]) are all same length
# len(words[i]) <= 30
# len(s) <= 10K
