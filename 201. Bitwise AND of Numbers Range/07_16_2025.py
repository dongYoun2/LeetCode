# submission: https://leetcode.com/problems/bitwise-and-of-numbers-range/submissions/1700568611/
# runtime: 13 ms, memory: 18 MB
# solved it after noticing that the problem is exact same problem as finding the common prefix of the binary representation of the two numbers from Editorial section. (but didn't see the code there)

# From LeetCode Top Interview 150 - Bit Manipulation

# the code below is simply the implementation of finding the common prefix of the two integers with the help of converting binary representaion to strings, which is not the most efficient way. for a much efficient and concise solution, refer to the Editorial's approach 1: bit shift. (got shocked by how simple and elegant it is)


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        total_bit_cnt = prefix_bit_cnt = 0
        common_prefix_reversed = []

        while left or right:
            total_bit_cnt += 1
            left_lsb, right_lsb = left & 1, right & 1
            if left_lsb == right_lsb:
                prefix_bit_cnt += 1
                common_prefix_reversed.append(str(left_lsb))
            else:
                prefix_bit_cnt = 0
                common_prefix_reversed = []
            left >>= 1
            right >>= 1

        if not common_prefix_reversed:
            return 0

        common_prefix = list(reversed(common_prefix_reversed))
        ans = int("".join(common_prefix), 2)
        ans = ans << (total_bit_cnt - prefix_bit_cnt)

        return ans
