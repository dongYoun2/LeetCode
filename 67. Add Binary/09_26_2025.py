# submission: https://leetcode.com/problems/add-binary/submissions/1783719099/
# runtime: 2 ms, memory: 18.02 MB

# 17 min

# again, i solved it with the similar logic as i did in the `06_17_2025.py` code. i hope i can solve it either bit-by-bit computation (AC implementation) or bit manipulation next time.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(reversed(a))
        b = list(reversed(b))

        if len(a) > len(b):
            small, big = b, a
            small_l, big_l = len(b), len(a)
        else:
            small, big = a, b
            small_l, big_l = len(a), len(b)


        def compute(one_cnt: int):
            if one_cnt == 0:
                return '0', '0'
            if one_cnt == 1:
                return '1', '0'
            if one_cnt == 2:
                return '0', '1'
            if one_cnt == 3:
                return '1', '1'


        ans = []
        carry = i = 0
        while i < small_l:
            one_cnt = int(small[i] == '1') + int(big[i] == '1') + int(carry == '1')
            nxt_val, carry = compute(one_cnt)
            ans.append(nxt_val)
            i += 1

        while i < big_l:
            one_cnt = int(big[i] == '1') + int(carry == '1')
            nxt_val, carry = compute(one_cnt)
            ans.append(nxt_val)
            i += 1

        if carry == '1':
            ans.append('1')

        ans.reverse()
        return ''.join(ans)


# notes while solving:
#   1 1 1
#       1
# 1 0 0 0