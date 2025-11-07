[Problem](https://leetcode.com/problems/factorial-trailing-zeroes/)


## Counting Factors of 5 (Linear Time)

This approach is identical to the [11_07_2025.py](11_07_2025.py) solution or the Editorial's Approach 2. Please refer to either for the details.


## Counting Factors of 5 Efficiently (Logarithmic Time)

This solution solves the **follow-up question**.

From [11_07_2025.py](11_07_2025.py) solution, once we notice that the number of multiples of $5^k$ up to n is actually the number of times the inner loop runs, we can simply leverage a division operation instead of a inner loop (in `11_07_2025.py`). therefore, the time complexity is reduced to $O(\log_5(n))$.


cf.) This approach is the same as the Editorial's Approach 3.


- [Submission](https://leetcode.com/problems/factorial-trailing-zeroes/submissions/1823473630/) (Runtime: 0 ms, Memory: 17.61 MB)
- TC: $O(\log_5(n))$, where $n$ is the input number.
- SC: $O(1)$

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Count how many times 5 is a factor in numbers from 1 to n
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count

```