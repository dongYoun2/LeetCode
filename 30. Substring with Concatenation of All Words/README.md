
[Problem](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)


## Sliding Window Approach (feat. ChatGPT)

Code below is created by ChatGPT. it's the readable, concise, efficient, and interview-friendly code.

cf.) Instead of copying the `Counter` object (in `04_02_2025.py` and `10_02_2025.py`), we can simply use the `clear()` method.


- [Submission](https://leetcode.com/problems/substring-with-concatenation-of-all-words/submissions/1791335852/) (Runtime: 23 ms, Memory: 18.60 MB)
- TC: $O(n)$
- SC: $O(U)$
  - $n$: length of `s`
  - $w$: length of each word (all words are the same length)
  - $U$: number of unique words in `words`


```python
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        assert len(s) > 0 and len(words) > 0

        w = len(words[0])                 # word length
        m = len(words)                    # number of words to match
        total = w * m
        n = len(s)
        if n < total:
            return []

        need = Counter(words)             # required multiset of words
        ans = []

        # Try all alignments within a word
        for offset in range(w):
            left = offset                 # window left (inclusive)
            seen = Counter()
            used = 0                      # number of words currently in window

            # Slide right in strides of word length
            for right in range(offset, n - w + 1, w):
                word = s[right:right + w]

                if word not in need:
                    # Hard reset on unknown word
                    seen.clear()
                    used = 0
                    left = right + w
                    continue

                # Include the word
                seen[word] += 1
                used += 1

                # If this word overflows, shrink from the left
                while seen[word] > need[word]:
                    left_word = s[left:left + w]
                    seen[left_word] -= 1
                    left += w
                    used -= 1

                # When we have exactly m words, record and pop one from the left
                if used == m:
                    ans.append(left)
                    left_word = s[left:left + w]
                    seen[left_word] -= 1
                    left += w
                    used -= 1

        return ans

```