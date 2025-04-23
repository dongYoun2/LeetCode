# problem: https://leetcode.com/problems/contains-duplicate-ii/
# submission: https://leetcode.com/problems/contains-duplicate-ii/submissions/1615736821/

# 5 min
# runtime: 24 ms, memory: 36.7 MB
# TC: O(n), where n is the number of elements in the list
# SC: O(n)

# From LeetCode Top Interview 150 - Hashmap

# I used a hashmap to store the value -> index mapping. One thing to notice is that the index of the value is updated every time we see the value again, so that we can check the distance between the current index and the last index of the value, since we are checking if the distance is less than or equal to k.

# The space complexity can be optimized to O(min(n, k)). Refer to the markdown file for more details.


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        val_to_idx = {}

        for i, n in enumerate(nums):
            if n in val_to_idx:
                idx = val_to_idx[n]
                if abs(i - idx) <= k:
                    return True

            val_to_idx[n] = i

        return False
