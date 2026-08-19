[Problem](https://leetcode.com/problems/majority-element/)



## Sorting Solution


Refer to the file [08_11_2025.py](08_11_2025.py).


## Hash Map Solutions

### Using `defaultdict`

[Submission](https://leetcode.com/problems/majority-element/submissions/1566366951/)—Runtime: 14 ms (beats 20.87%), Memory: 19.24 MB (beats 100.00%)

- TC: $O(n)$
- SC: $O(n)$

```python
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)

        for n in nums:
            counter[n] += 1

            if counter[n] > len(nums) // 2:
                return n

```

### Using `Counter`

We  can simply use the `Counter`'s `most_common` method.


[Submission](https://leetcode.com/problems/majority-element/submissions/1566158226/)—Runtime: 0 ms (beats 100.00%), Memory: 19.68 MB (beats 100.00%)


- TC: $O(n)$
- SC: $O(n)$

```python
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        return cntr.most_common()[0][0]

```


## Boyer-Moore Voting Algorithm

This approach solves the **follow-up question**.

cf.) [08_11_2025_boyer_moore.py](08_11_2025_boyer_moore.py) and [08_18_2026_follow_up.py](08_18_2026_follow_up.py) also implement this algorithm.


[Submission](https://leetcode.com/problems/majority-element/submissions/1566370748/)—Runtime: 3 ms (beats 84.89%), Memory: 19.10 MB (beats 100.00%)

- TC: $O(n)$
- SC: $O(1)$


```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        predominance = 0    # count of the current candidate
        candidate = None    # since majority element is guaranteed to exist, this `candidate` will simply be the answer (majority element)

        for n in nums:
            if predominance == 0:
                candidate = n

            if n == candidate:
                predominance += 1
            else:
                predominance -= 1

        return candidate

```
