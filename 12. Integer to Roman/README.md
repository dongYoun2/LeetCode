[Problem](https://leetcode.com/problems/integer-to-roman/)



## Greedy Approach

Unlike [08_05_2026.py](08_05_2026.py) implementation, we can also include the subtractive cases to the lookup table, and iterate through them in the same greedy manner. 

[Submission](https://leetcode.com/problems/integer-to-roman/submissions/2095654895/)—Runtime: 11 ms (13.68%), Memory: 19.26 MB (beats 63.34%)

- TC: $O(1)$
- SC: $O(1)$


```python
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        result = []
        for value, symbol in values:
            count, num = divmod(num, value)
            result.append(symbol * count)

        return "".join(result)

```

cf.) Above solution is the same as the [Editorial's Approach 1: Greedy](https://leetcode.com/problems/integer-to-roman/editorial/#approach-1-greedy).