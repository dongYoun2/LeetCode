[Problem](https://leetcode.com/problems/top-k-frequent-words/)


## Hash Table + Sorting

Refer to the [03_21_2026.py](03_21_2026.py) file.


## Max Heap (All Elements)

Refer to the [03_21_2026_max_heap.py](03_21_2026_max_heap.py) file.


## Min Heap (Of Size $k$)

This approach solves the **Follow-up** question, which asks "Could you solve it in $O(n \log(k))$ time and $O(n)$ extra space?"

The idea is to maintain a heap of size $k$, and whenever the heap size exceeds $k$, we pop the smallest item (which is the "worse" item) from the heap. This way, the heap always contains the $k$ most frequent items. Then, once we iterate through all unique words, we can simply sort the heap by frequency descending and lexicographically ascending to get the final result.


[Submission](https://leetcode.com/problems/top-k-frequent-words/submissions/1954910078/)—Runtime: 0 ms (beats 100.00%), Memory: 19.66 MB (beats 15.57%)


Symbols:
- $n$: length of words
- $m$: number of unique words
- $k$: number of most frequent words to return
<br>

- TC: $O(n + m \log k)$ (Since $m \leq n$, it satisfies the time complexity requirement of the Follow-up question.)
  - Building Counter: $O(n)$
  - For each $m$ word, we push to the heap once and pop at most once: $O(m \log k)$
- SC: $O(m + k)$ -> $O(m)$ (Counter and the heap)

Important thing to notice is we defined a custom `Item` class with **`__lt__` magic method** to define the "worse" items as smaller where multiple keys are used for the heap priority.

**There are other ways to use multiple keys for the heap priority**. The simplest one is to **use a tuple** just like in the [Max Heap (All Elements)](#max-heap-all-elements) approach. However, we cannot use a tuple in this approach since the heap is supposed to keep the **worst item** at the top, so that when the heap size becomes $k+1$, we pop the worst one. The key difference is that in the [Max Heap (All Elements)](#max-heap-all-elements) approach, the answer would be the elements that are popped from the heap eventually, whereas here, elements left in the heap at the end are the answer.

Another way is to define a **custom dataclass using a `@dataclass` decorator and `field(compare=False)`** function as mentioned [here](https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes). Likewise, it's a little tricky for this approach. Thus, we simply used the `__lt__` magic method way as shown in the code below.

cf.) In a LeetCode problem [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/), we also needed to use multiple keys for the heap priority. Refer to the [01_28_2026.py](../23.%20Merge%20k%20Sorted%20Lists/01_28_2026.py) for a code and a brief explanation.


```python
from collections import Counter
import heapq

class Item:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        # Define "worse" items as smaller so they get popped first
        
        # 1. Lower frequency is worse
        if self.freq != other.freq:
            return self.freq < other.freq
        
        # 2. If frequencies are equal, lexicographically larger word is worse
        return self.word > other.word


class Solution:
    def topKFrequent(self, words, k):
        cntr = Counter(words)

        pq = []
        
        for word, freq in cntr.items():
            heapq.heappush(pq, Item(word, freq))
            
            if len(pq) > k:
                heapq.heappop(pq)

        # Heap now contains the top k elements
        # Sort by frequency descending, then lexicographically ascending
        result = sorted(pq, key=lambda x: (-x.freq, x.word))
        
        return [item.word for item in result]

```