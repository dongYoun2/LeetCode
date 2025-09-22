[Problem](https://leetcode.com/problems/missing-number/)

- [Sorting + Linear Search](#sorting--linear-search)
- [Sorting + Binary Search](#sorting--binary-search)
- [Hash Table](#hash-table)
- [Math](#math)
- [Bit Manipulation](#bit-manipulation)


## Sorting + Linear Search

- [Submission](https://leetcode.com/problems/missing-number/submissions/1779237034/) (Runtime: 13 ms, Memory: 18.55 MB)
- TC: $O(n log n + n)$ -> $O(n log n)$, $n log n$ for sorting, $n$ for linear search
- SC: $O(1)$

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i, n in enumerate(nums):
            if i != n:
                return i

        return len(nums)

```


## Sorting + Binary Search

From the [Sorting + Linear Search approach](#sorting--linear-search), we can notice that the linear search can be replaced with binary search since now the input array is sorted and we are looking for the missing number.

- [Submission](https://leetcode.com/problems/missing-number/submissions/1779238553/) (Runtime: 7 ms, Memory: 18.70 MB)
- TC: $O(n log n)$
- SC: $O(1)$

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if m < nums[m]:
                r = m - 1
            else:
                l = m + 1

        return l

```


## Hash Table

We can reduce the time complexity from $O(n log n)$ to $O(n)$ by using a hash table.

- [Submission](https://leetcode.com/problems/missing-number/submissions/1779244503/) (Runtime: 3 ms, Memory: 19.1 MB)
- TC: $O(n)$
- SC: $O(n)$

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set(nums)

        for number in range(n + 1):
            if number not in seen:
                return number

```


## Math

Refer to the [09_22_2025.py](09_22_2025.py) file.


## Bit Manipulation


The key idea is to use the XOR bitwise operation. Three important features of the XOR bitwise operation are:

1. XOR with itself will be 0: $a \oplus a = 0$
2. XOR with 0 will be itself: $a \oplus 0 = a$
3. Commutative property: $a \oplus b = b \oplus a$

cf.) This property is also used in the [136. Single Number](../136.%20Single%20Number/07_16_2025.py) problem.

- [Submission](https://leetcode.com/problems/missing-number/submissions/1779249771/) (Runtime: 4 ms, Memory: 18.65 MB)
- TC: $O(n)$
- SC: $O(1)$


```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)

        for i, n in enumerate(nums):
            ans = ans ^ i ^ n

        return ans

```
