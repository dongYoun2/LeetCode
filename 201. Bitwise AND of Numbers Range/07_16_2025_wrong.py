# submission: https://leetcode.com/problems/bitwise-and-of-numbers-range/submissions/1700473662/
# wrong answser

# 59 min

# From LeetCode Top Interview 150 - Bit Manipulation

# spent an hour attempting to solve this problem, but could not solve it.

# i first tried with a brute force solution, which i iterate through all numbers in the range and do a bitwise AND operation, but since the range can be maximum 2^31, it shows the time limit exceeded error.

# then, by manually simulating over the binary representation of the numbers (in the notes below), i thought the problem is asking the same question as finding the first bit taht is different from the one before (in a higher position) in the binary representation of the AND operation of the two numbers, and then replacing all bits after that with 0s. however, this is incorrect, as shown in the counterexamples in the submission.

# counterexamples:
# left = 416 (0b110100000), right = 436 (0b110110100)
# correct answer: 416 (0b110100000)
# my answer: 384 (0b110000000)


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        tmp = left & right
        if tmp == 0: return 0

        tmp_b = bin(tmp)[2:]
        assert len(tmp_b) > 0

        prev = tmp_b[0]
        found = 0
        for i in range(1, len(tmp_b)):
            if prev == '1' and tmp_b[i] == '0':
                found = i
                print(found)
                break
            prev = tmp_b[i]

        ans: str = tmp_b[:found] + '0' * (len(tmp_b) - found)

        return int(ans, 2)


# notes while solving:
# 0:  0000
# 1:  0001
# 2:  0010
# 3:  0011
# 4:  0100
# 5:  0101
# 6:  0110
# 7:  0111
# 8:  1000
# 9:  1001
# 10: 1010
# 11: 1011
# 12: 1100
# 13: 1101
# 14: 1110
# 15: 1111

# including pairs: (0, 1), (1, 2), (3, 4), (7, 8), (15, 16)
# (2^k - 1, 2^k) --> 0