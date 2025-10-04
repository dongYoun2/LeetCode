# submission: https://leetcode.com/problems/happy-number/submissions/1791252815/
# runtime: 4 ms, memory: 17.77 MB

# 13 min
# TC: O(log n)
# SC: O(1)
# cf.) for complexity analysis, refer to 04_11_2025.py


# the problem mentions that if the number is not a happy number, the loop must be endless. getting hint from this, i assummed that non-happy number will eventually fall into a cycle. to detect the cycle, i used a set to keep track of the numbers that have been seen.


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            next_n = 0
            while n != 0:
                n, r = divmod(n, 10)
                next_n += r ** 2

            if next_n in seen:
                return False

            seen.add(next_n)
            n = next_n

        return True


# notes while solving:
# 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

# 2^31 - 1 = 2,147,483,648 -> 275 -> 78

# 999999999 -> 729

# but how to prove that endless loop means it's hitting the previous number that have seen
