# submission: https://leetcode.com/problems/integer-to-roman/submissions/2095607497/
# runtime: 0 ms (beats 100.00%), memory: 19.19 MB (beats 90.85%)
# greedy + string replacement solution
# 14 min

# TC: O(1)
# SC: O(1)


# pretty straightforward solution. first, we greedily convert the input number to roman symbols without considering the subtractive cases from larger to smaller symbols. then, we replace the subtractive cases (e.g., 4, 9, 40, 90, 400, 900) with their corresponding roman symbols. one thinkg to keep in mind here is that the replacement order matters. 9 has to be replaced before 4, 90 before 40, and 900 before 400 because the larger subtractive cases contain the smaller ones.

# cf.) instead of string replacement as a post-processing, we can simply include the subtractive cases to the predefined `symbols` and `values` lists, and iterate through them in the same greedy manner. this is more elegant. refer to the README.md for details of this optimal solution.


class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        values = [1000, 500, 100, 50, 10, 5, 1]

        ans_arr = []
        n = num
        for i in range(7):
            q, r = divmod(n, values[i])
            ans_arr.append(symbols[i] * q)
            n = r

        ans = ''.join(ans_arr)

        ans = ans.replace('DCCCC', 'CM')
        ans = ans.replace('CCCC', 'CD')
        ans = ans.replace('LXXXX', 'XC')
        ans = ans.replace('XXXX', 'XL')
        ans = ans.replace('VIIII', 'IX')
        ans = ans.replace('IIII', 'IV')

        return ans


# notes while solving:
# 49
# XXXXVIIII
