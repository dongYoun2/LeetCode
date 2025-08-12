[Problem](https://leetcode.com/problems/majority-element/)

## Sorting Solution

- [Submission](https://leetcode.com/problems/majority-element/submissions/1731845853/)
- Runtime: 4 ms, Memory: 19.43 MB
- TC: $O(n \log n)$, due to sorting.
- SC: $O(1)$.

<br>

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]

```


## Hash Map Solutions

### Using `defaultdict`

- [Submission](https://leetcode.com/problems/majority-element/submissions/1566366951/)
- Runtime: 14 ms, Memory: 19.24 MB
- TC: $O(n)$
- SC: $O(n)$

<br>

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

- [Submission](https://leetcode.com/problems/majority-element/submissions/1566158226/)
- Runtime: 0 ms, Memory: 19.68 MB
- TC: $O(n)$
- SC: $O(n)$

<br>

```python
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        return cntr.most_common()[0][0]

```


## Boyer-Moore Voting Algorithm

- [Submission](https://leetcode.com/problems/majority-element/submissions/1566370748/)
- Runtime: 3 ms, Memory: 19.10 MB
- TC: $O(n)$
- SC: $O(1)$

<br>

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
