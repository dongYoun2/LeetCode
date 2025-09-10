# submission: https://leetcode.com/problems/3sum/submissions/1766345391/
# runtime: 502 ms, memory: 21.2 MB

# 20 min
# TC: O(n^2), where n is the number of elements in nums
# SC: O(n)


# From LeetCode Top Interview 150 - Two Pointers

# though it's a two-pointer approach, i solved it with dividing cases. it's very straightforward and easy to understand once you divide the cases. one caveat is that for the third and fourth cases, it's important not to loop through the positive set (or negative set) for the most outer loop because then the time complexity becomes O(n^3). we can notice that this problem should be solved in O(n^2) when you see the constraints (n <= 3000). so we need nested loops for the negative list (or positive list) and directly check if the positive (or negative) counterpart exists in the set, which will take O(1) time due to hashing.

# cf.) at first i tried to solve this problem with two-pointer approach spending more than an hour, but i was keep getting wrong answer. therefore, i gave up and decided to solve it in a below way, which i was aware of for this problme.


from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cntr = Counter(nums)
        ans = set()

        positives = sorted([n for n in nums if n > 0])
        negatives = sorted([n for n in nums if n < 0])

        p_len, n_len = len(positives), len(negatives)
        P, N = set(positives), set(negatives)

        # 1. 3 zeros answer
        if cntr[0] >= 3:
            ans.add((0, 0, 0))

        # 2. 1 zero, (1 neg, 1 pos)
        if cntr[0] > 0:
            for p in list(P):
                if -p in N:
                    ans.add((-p, 0, p))

        # 3. 2 negatives, 1 positive
        for i in range(n_len):
            for j in range(i + 1, n_len):
                n1, n2 = negatives[i], negatives[j]
                p = - (n1 + n2)
                if p in P:
                    ans.add((n1, n2, p))

        # 4. 1 negative, 2 positives
        for i in range(p_len):
            for j in range(i + 1, p_len):
                p1, p2 = positives[i], positives[j]
                n = - (p1 + p2)
                if n in N:
                    ans.add((n, p1, p2))

        return list(ans)
