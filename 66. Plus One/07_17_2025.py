# submission: https://leetcode.com/problems/plus-one/submissions/1701580539/

# 8 min
# TC: O(n), where n is the length of the `digits` list.
# SC: O(1)

# From LeetCode Top Interview 150 - Math


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        has_carry = True
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                has_carry = False
                break

        return [1] + digits if has_carry else digits
