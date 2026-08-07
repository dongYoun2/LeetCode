# submission: https://leetcode.com/problems/add-binary/submissions/2098431553/
# runtime: 2 ms (beats 48.65%), memory: 19.43 MB (beats 16.92%)
# 14 min
# solved implementing AC logic (bit-by-bit computation); identical to the README.md's "Bit-by-Bit Computation (ripple-carry adder)" and Editorial's Approach 1.

# refer to the README.md's "Bit-by-Bit Computation (ripple-carry adder)" section for complexity anaylsis


# i could think of using `zfill()` function to pad the shorter string with leading zeros instead of manually calculating the difference in lengths and prepending zeros.

# i saw in the Notion's comments to solve either by bit manipulation (README.md's "Bit Manipulation" solution) or by bit-by-bit computation. i couldn't think of a solution using bitwise operators, so i solved with the latter approach, which is quite straightforward.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)

        ans = []
        carry = 0
        for i in range(n-1, -1, -1):
            d1, d2 = int(a[i]), int(b[i])
            carry, curr = divmod(d1+d2+carry, 2)
            ans.append(str(curr))

        if carry == 1:
            ans.append(str(carry))

        ans.reverse()
        return ''.join(ans)
