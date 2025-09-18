# problem: https://leetcode.com/problems/longest-consecutive-sequence/
# submission: https://leetcode.com/problems/longest-consecutive-sequence/submissions/1600160547/

# 54 min (includes writing memory limit exceeded code (04_07_2025_mle.py))
# TC: O(n), where n is the number of elements in nums
# SC: O(n)


# Knew that I had to use hash map since I am solving problems based on the algorithm type.

# After getting memory limit exceeded from the "04_07_2025_mle.py", I came up with this solution. Howver, I think there would be a better implementation (and approach) than this since there are some redundancy in the code.

# The core idea is as follows:
# We want to check if n-1 and n+1 exist in `nums` (or `set(nums)`) while iterating through `nums`.
# - If both exist, find the minimum number in the consecutive sequence by decrementing from n-1 until a number not in the `set(nums)` is found. Then, count the length of the consecutive sequence by incrementing from the minimum number until a number not in the `set(nums)` is found.
# - If only n+1 exists, count the length of the consecutive sequence starting from n+1.
# - If only n-1 exists, count the length of the consecutive sequence starting from n-1.

# Also, to exclude the numbers that has already been counted, I used the `visited` set to keep track of them.

# Just now, after looking at the Editorial's approach 3, I realized that I don't have to consider both directions, that is, n-1 and n+1, at the same time. Rather I could just check  n-1 after ensuring that the n+1 doesn't exist in `nums` (or equivalently, checking only n+1 after ensuring that the n-1 doesn't exist). This is because we can guarantee that we will always  check the consecutive sequence starting from the maximum (or minimum) number of the sequence while iterating through `nums`.

# cf.) This question could also be solved using a union-find data structure.


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums_s = set(nums)
        visited = set()

        ans = 1
        for n in nums:
            if n in visited:
                continue

            visited.add(n)

            if (n - 1 in nums_s) and (n + 1 in nums_s):
                k = n - 1
                while k in nums_s:
                    min_n = k
                    k -= 1

                consecutive_cnt = 0
                while min_n in nums_s:
                    visited.add(min_n)
                    consecutive_cnt += 1
                    min_n += 1

            elif n + 1 in nums_s:
                consecutive_cnt = 1
                min_n = n + 1
                while min_n in nums_s:
                    visited.add(min_n)
                    consecutive_cnt += 1
                    min_n += 1

            elif n - 1 in nums_s:
                consecutive_cnt = 1
                max_n = n - 1
                while max_n in nums_s:
                    visited.add(max_n)
                    consecutive_cnt += 1
                    max_n -= 1
            else:
                consecutive_cnt = 1

            ans = max(ans, consecutive_cnt)


        return ans


# notes while solving:
# 100 4 200 1 3 2
# 101, 99?

# 4 200 1 3 2
# 5, 3?

# ans = 2
# 200 1 3 2
# 2?

# ans = 3
# 200 1 2
# 1?

# ans = 4
# 200

# 200