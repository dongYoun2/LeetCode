# submission: https://leetcode.com/problems/generate-parentheses/submissions/2030178647/
# runtime: 2 ms (beats 35.45%), memory: 19.22 MB (beats 94.68%)
# 36 min (time includes the "06_11_2026_wrong.py" solution)
# solved with backtracking

# refer to the "05_27_2025.py" solution for a complexity analysis


# as mentioned in the "06_11_2026_wrong.py" solution, i approached in a wrong way initially though the problem felt like a backtracking problem. after doing some simulations, i solved with a backtracking approach. it took longer than i expected.


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = set()
        def gen(curr, n):
            nonlocal ans

            if n == 0:
                if curr not in ans:
                    ans.add(curr)
                return
            
            gen('(' + curr + ')', n-1)
            gen('()' + curr, n-1)
            gen(curr + '()', n-1)


        gen('', n)

        return list(sorted(ans))
