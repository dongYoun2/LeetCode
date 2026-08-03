# spent 30 min trying to solve this problem, but could not even come up with a correct approach. was flabbergasted by that we can simply use bitwise operations to find the common prefix. hope i can solve with this approach next time.


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        


# notes while solving:
# 5 = 101 (left)
# 6 = 110
# 7 = 111 (right)

# 1    1
# 2   10
# 3   11
# 4  100
