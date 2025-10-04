# submission: https://leetcode.com/problems/substring-with-concatenation-of-all-words/submissions/1790497765/
# runtime: 101 ms, memory: 18.7 MB

# 79 min (includes time writing the 10_03_2025_tle.py code)
# TC: O(n), where n is the length of `s`.
# SC: O(U), where U is the number of unique words in `words`.


# it stil took quite a long time though it's my second time solving this problem. unlike on 04/02/2025, i dind't know which data structure or algorithm to use in advance. so i wrote brute-force solution (with little optimization, including using hash table, striding by word size, etc.) first, and then optimized it.

# after writing the brute-force solution, i noticed directly thrwing everything away (curr_words = [], reset cntr to the full multiset) and shift the start by 1 is inefficient. then, i realized that for all offset less than `word_size`, i can check whether there are concatenated strings while striding by `word_size`. for each offset, finding concatenated strings can be done by sliding windw appraoch with variable window size (in the code below, window start and end are `start` and `i + word_size - 1`, respectively).

# however, two improvements are possible:
# 1. early returns
# 2. directly skipping unknown words: moving start to the next word of the last (rightmost) word (`curr_word`) if it's an unknown word (e.g. `curr_word not in cntr`). actually, 04_02_2025.py performs this.

# cf) additionally, the code below is a little messy and hard to read. for better code and more details, refer to the markdown file.


from collections import Counter
from copy import deepcopy

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        assert len(words) >= 1
        word_size = len(words[0])

        ans = []
        orig_cntr = Counter(words)
        start = i = 0

        for i in range(word_size):   # word_size <= 30
            cntr = deepcopy(orig_cntr)
            start = i

            while i < len(s):
                curr_word = s[i:i+word_size]
                if curr_word in cntr and cntr[curr_word] > 0:   # matched
                    cntr[curr_word] -= 1
                    if cntr[curr_word] == 0:
                        del cntr[curr_word]

                    if not cntr:    # found concatenated string
                        ans.append(start)

                        first_word = s[start:start+word_size]
                        cntr[first_word] += 1
                        start += word_size

                    i += word_size
                    continue

                first_word = s[start:start+word_size]
                cntr[first_word] += 1
                start += word_size


        return ans


# notes while solving:
# len(words) <= 50K
# len(words[i]) are all same length
# len(words[i]) <= 30
# len(s) <= 10K