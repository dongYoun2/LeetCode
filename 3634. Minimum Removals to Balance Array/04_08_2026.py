# submission: https://leetcode.com/problems/minimum-removals-to-balance-array/submissions/1972584537/
# runtime: 138 ms (beats 43.73%), memory: 34.73 MB (beats 34.02%)
# 47 min

# TC: O(n log n + n) -> O(n log n)
# SC: O(1) (sorting's temporary space is not considered)


# i chose this problem from the "sliding window" category to practice and focus on sliding window algorithms.

# the key idea is to find the longest subarray that satisfies the condition, "max <= min * k". once we found this, the final answer is "n - longest subarray length". to achieve this, we can use a sliding window technique.

# my thought process is as follows:

# 1. first i thought of brute-force solution (even without sorting). this requires tring all subsets of the array to remove, then checking if the remaining array satisfies the condition, which takes O(2^n) time (exponential time). 
# 2. now, the insight is that once we sort the array, we can easily notice the left part of the array is smaller than or eqaul to the right part. with this, the brute force becomes O(n^2) time (still inefficient).
# 3. i started thinking with the sliding window (though i knew this problem is a sliding window problem):
#   - first, i fixed the start of the window to the leftmost index, and only expand the end pointer. since this cannot find the subarray that actaully contains the left part of the array, i also thought of fixing the right pointer (from the rightmost index of the array) and only expand the start pointer, which is simply running the same logic backwards (so total two cases). however, this approach only explores **the window that touch either end**, whereas the optimal window can be fully in the middle.
#   - noticing the above problem, now i started from the huge window (just like the two-pointer approach, where oftentimes the left and right pointers are set as the outermost indices of the array), and try to shrink the window. however, the problem is that we cannot decide which pointer to shrink; the optimal choice is not locally determined. i tried with a greedy decision, but of course this doesn't work since a locally valid move can ignore the larger future window (or the global optimal window). the wrong submission can be found here: https://leetcode.com/problems/minimum-removals-to-balance-array/submissions/1972577340/. notice the failed test case: nums = [51,70,9,21] and k = 2.
#   - finally, i realized that we can start from the window of size 1. then we can simply expand the window from the right end, and shrink from the left end while keeping checking if the window satisfies the condition (this is the code below).

# cf.) just like thoughts on yesterday's problem "424. Longest Repeating Character Replacement", i need to keep practicing the sliding window problems. it took quite a long time to solve though i knew it's a sliding window problem.


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        assert nums

        n = len(nums)
        nums.sort()

        max_size = 0

        s = 0   # s (window start)
        for e in range(n):  # e (window end)
            while nums[e] > nums[s]*k:
                s += 1
            
            max_size = max(max_size, e-s+1)
        
        return n - max_size
