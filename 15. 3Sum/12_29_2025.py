submission: https://leetcode.com/problems/3sum/submissions/1868803809/
runtime: 1321 ms, memory: 19.84 MB

34 min
TC: O(n^2)
SC: O(log n) (for built-in sorting) (output space is not counted)


This is very popular problem in the LeetCode. For me, the easiest appraoch is "Dividing Cases" as shown in the `09_10_2025_dividing_cases.py`. However, I wanted to solve it with a optimized two-pointer approach since I knew this problem can be solved with that.

The code below itself is correct, but it contains a lot of unnecessary codes. First, as discuessed in the "With Optimization" section of the README, we actually don't need to skip the already seen middle and largest numbers (two additional while loops within the `while l < r` loop). If I really want to add them, they should be added only after the hit case, where the triplet is found, not the every iteration. By removing this, we can also remove the `if l == r: break` condition. Second, when skpping the already checked smallest number, we can simply check with `if i != 0 and nums[i-1] == nums[i]:` instead of `a_prev = float('inf')` and `if nums[i] == a_prev: continue`. Lastly, to make it simpler, we can use `set` instead of `list` for the `ans` variable.

Two-pointer approach without optimization is pretty straightforward (refer to the README), but I should logically think and review why the two optimizations (early return and skipping the already seen smallest number) are needed.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        ans = []
        a_prev = float('inf')
        for i in range(n):
            if nums[i] == a_prev:
                a_prev = nums[i]
                continue

            b_prev = c_prev = float('inf')
            l, r = i + 1, n - 1
            while l < r:
                while l < r and nums[l] == b_prev: l += 1
                while l < r and nums[r] == c_prev: r -= 1

                if l == r: break

                if nums[l] + nums[r] == - nums[i]:
                    ans.append((nums[i], nums[l], nums[r]))
                    b_prev = nums[l]
                    c_prev = nums[r]
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > - nums[i]:
                    c_prev = nums[r]
                    r -= 1
                else:
                    b_prev = nums[l]
                    l += 1

            a_prev = nums[i]

        return ans
