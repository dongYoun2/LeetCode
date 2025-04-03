
[Problem](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

- [Wrong Code 1](#wrong-code-1)
- [Wrong Code 2](#wrong-code-2)
- [Wrong Code 3](#wrong-code-3)
- [Correct Code (same as the `04_02_2025.py`)](#correct-code-same-as-the-04_02_2025py)

<br>

## Wrong Code 1

This is the code that I first wrote without thinking the logical steps in detail. Could not debug. (cf. I have this code because I commented this code out, then started to code up again, which became **Wrong Code 2**, lol)

```python
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_cnt, word_size = len(words), len(words[0])
        ans = []

        if len(s) < word_cnt * word_size:
            return ans

        word_cntr = Counter(words)

        i = j = 0
        while True:
            if j - i + 1 < word_cnt * word_size: # insertion possible
                if j+word_size >= len(s):
                    break

                cand_word = s[j+1:(j+1)+word_size]

                if cand_word in word_cntr:
                    if word_cntr[cand_word] > 0:
                        word_cntr[cand_word] -= 1
                        j = j+word_size
                    else:
                        i = i+word_size
                else:
                    while i <= j:
                        curr_w = s[i:i+word_size]
                        word_cntr[curr_w] += 1
                        i += word_size

                    i = j = j + 1

                if j - i + 1 == word_cnt * word_size:
                    ans.append(i)

                    first_word = s[i:i+word_size]
                    word_cntr[c] += 1
                    i += word_size

        return ans
```
<br>


## Wrong Code 2

- [Submission](https://leetcode.com/problems/substring-with-concatenation-of-all-words/submissions/1594903797/)

Rewrote from scratch after removing the **Wrong Code 1**.

While debugging, I found out that I only checked the indices with `0 + i * word_size`. For example, if `word_size` is 3, this code only checks indices with 0, 3, 6, ... . Concatenated string "can" start from index 5 in this case, if it fails to exist at index 3.


```text
# Failed test case

s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]
```


```python
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_cnt, word_size = len(words), len(words[0])
        ans = []

        if len(s) < word_cnt * word_size:
            return ans

        word_cntr = Counter(words)
        word_cntr_cp = word_cntr.copy()

        window_s = 0
        window_e = 0 + word_size - 1
        while window_e < len(s) and window_s < len(s):
            last_word = s[window_e+1-word_size:window_e+1]

            if last_word not in word_cntr:
                word_cntr = word_cntr_cp.copy()

                window_s = window_e + 1
                window_e += word_size
                continue

            # last_word exists in word_cntr from here

            if word_cntr[last_word] > 0:
                word_cntr[last_word] -= 1
            else:
                first_word = s[window_s:window_s+word_size]
                word_cntr[first_word] += 1
                window_s += word_size
                continue

            if window_e - window_s + 1 == word_cnt * word_size: # found concatenated string
                ans.append(window_s)

            window_e += word_size

        return ans
```
<br>


## Wrong Code 3

- [Submission](https://leetcode.com/problems/substring-with-concatenation-of-all-words/submissions/1594903797/)

The issue with this code is that the `word_counter` doesn't get refreshed for the following sliding window iterations. This is because the word counter gets initialized only once. The code is at the outside of the outer loop; it has to be inside the outer loop or the `find_concat_strings()` function.

```text
# Failed test case

s = "aaaaaaaaaaaaaa"
words = ["aa","aa"]
```

```python
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_cnt, word_size = len(words), len(words[0])
        ans = []

        if len(s) < word_cnt * word_size:
            return ans

        word_cntr = Counter(words)
        word_cntr_cp = word_cntr.copy()

        def find_concat_strings(start):
            nonlocal word_cntr
            window_s = start
            window_e = start + word_size - 1
            while window_e < len(s) and window_s < len(s):
                last_word = s[window_e+1-word_size:window_e+1]

                if last_word not in word_cntr:
                    word_cntr = word_cntr_cp.copy()

                    window_s = window_e + 1
                    window_e += word_size
                    continue

                # last_word exists in word_cntr from here

                if word_cntr[last_word] > 0:
                    word_cntr[last_word] -= 1
                else:
                    first_word = s[window_s:window_s+word_size]
                    word_cntr[first_word] += 1
                    window_s += word_size
                    continue

                if window_e - window_s + 1 == word_cnt * word_size: # found concatenated string
                    ans.append(window_s)

                window_e += word_size

        for i in range(word_size):
            find_concat_strings(i)

        return ans
```
<br>


## Correct Code (same as the `04_02_2025.py`)

- [Submission](https://leetcode.com/problems/substring-with-concatenation-of-all-words/submissions/1594933402/)
<br>

- `Counter` has to be used instead of `set` since duplicated word could exists in `words`.
- To easily update the `word_cntr` when the rightmost word in the window is an invalid word (word that doesn't exist in `words`), `word_cntr_cp` (copied version of the initial word counter) is maintained.
- `windw_s` and `window_e` indicate the start and end pointers of the sliding window.
- early return when the `len(s)` is less than the number of total characters in `words`.
- `find_concat_strings()` performs one sliding window process (one pass). (So, `word_size` times of sliding window processes.)

cf.) consult the `04_02_2025.py` comments for the time and space complexity analysis.


```python
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
```