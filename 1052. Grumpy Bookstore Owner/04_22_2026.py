# submission: https://leetcode.com/problems/grumpy-bookstore-owner/submissions/1985444114/
# runtime: 25 ms (beats 9.60%), memory: 22.44 MB (beats 7.85%)
# 24 min
# used sliding window + prefix sum

# TC: O(n)
# SC: O(n)


# chose from a neetcode "sliding window" category.

# knew it's a sliding window problem in advance. i also used prefix sum to store the cumulative sum of the satisfied customers.

# my thought process is as follows:
# 1. there would be satisfied customers due to the owner's technique. this forms a window of size k (`forced_satisfied`). we will slide this window from the start to the end.
# 2. outside of this window, there would be satisfied customers without getting affected by the owner's technique (`satisfied`). then the total number of satisfied customers (at the current window state) is the sum of the satisfied customers inside the window (`force_satisfied`) + the satisfied customers outside the window. 
# 3. how can we compute the satisfied customers outside the window? the brute-force would be to iterate over the satisfied customers outside the window and sum them up, which reuires O(n) time for each and every state of the window. to do more efficiently, we can use prefix sum (`satisfied_cum`), which allows to compute in constant time. (but this is overengineering. we actually don't need prefix sum to solve this problem, lol.)
# 4. so at a current state of the window, the number of satisfied customers on the left side of the window is `satisfied_cum[i-k]` and the number of satisfied customers on the right side of the window is `satisfied_cum[-1] - satisfied_cum[i]`. therefore, we can compute the total number of satisfied customers at the current window state.
# 5. finally, find the maximum number of satisfied customers while sliding the window.

# cf.) as mentioned above, prefix sum is overengineering. we can solve this problem using only the sliding window technique, and this reduces the space complexity to O(1). refer to the README.md for details.


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        # assert len(grumpy) == n
        k = minutes
        
        satisfied = [c * (not g) for c, g in zip(customers, grumpy)]
        satisfied_cum = [satisfied[0]]  # satisfied prefix sum
        for i in range(1, n):
            e = satisfied_cum[-1] + satisfied[i]
            satisfied_cum.append(e)
        
        # assert len(satisfied_cum) == n

        force_satisfied = sum(customers[:k])    # satisfied customers with owener's technique
        ans = force_satisfied + (satisfied_cum[-1] - satisfied_cum[k-1])
        for i in range(k, n):
            force_satisfied += - customers[i-k] + customers[i]
            curr = force_satisfied + satisfied_cum[i-k] + (satisfied_cum[-1] - satisfied_cum[i])
            ans = max(ans, curr)
        
        return ans