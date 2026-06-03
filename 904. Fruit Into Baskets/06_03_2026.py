# submission: https://leetcode.com/problems/fruit-into-baskets/submissions/2021590520/
# runtime: 268 ms (beats 6.49%), memory: 26.15 MB (beats 12.86%)
# 25 min
# solved with a sliding window approach

# TC: O(n)
# SC: O(1)


# chose from a neetcode "sliding window" category.

# this is a typical variable-size sliding window solution. the key idea is to expand the window by one by including the current element, and shrink the window until the window contains at most 2 distinct fruits. to do this, we can simply use `while` loop when shrinking the window.

# cf.) just like how we optimized the sliding window solution in the problem "1838. Frequency of the Most Frequent Element", we can apply exactly the same technique to this problem. since we want the maximum valid window size, we can utilize a lazy sliding window approach. for details, refer to either: 
# 1. comments in the "06_02_2026.py" solution of the "1838" problem or
# 2. a submission with the optimized sliding window: https://leetcode.com/problems/fruit-into-baskets/submissions/2021602082/.


from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        collected = Counter((fruits[0],))
        left = 0
        ans = 1
        for right in range(1, n):
            collected[fruits[right]] += 1

            while len(collected) > 2:
                to_remove = fruits[left]
                collected[to_remove] -= 1
                if collected[to_remove] == 0:
                    del collected[to_remove]

                left += 1
            
            ans = max(ans, right-left+1)

        return ans
