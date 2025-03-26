# https://leetcode.com/problems/3sum/

# TC: O(N^2)
# SC: O(N)

# I remember the below algoritm as I have studied this problem before, and got a bit shocked from this solution. Editorial doesn't provide this kind of case-dividing approach. I believe this is very intuitive and easy to understand.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        pos_arr = [n for n in nums if n > 0]
        neg_arr = [n for n in nums if n < 0]
        zeros = [n for n in nums if n == 0]

        pos_set = set(pos_arr)
        neg_set = set(neg_arr)

        if len(zeros) >= 3:
            ans.add((0,0,0))

        # 1. two positives, one negative
        for i in range(len(pos_arr)):
            for j in range(i+1, len(pos_arr)):
                cand = - (pos_arr[i] + pos_arr[j])

                if cand in neg_set:
                    ans.add(tuple(sorted([cand, pos_arr[i], pos_arr[j]])))

        # 2. two negatives, one positive
        for i in range(len(neg_arr)):
            for j in range(i+1, len(neg_arr)):
                cand = - (neg_arr[i] + neg_arr[j])

                if cand in pos_set:
                    ans.add(tuple(sorted([cand, neg_arr[i], neg_arr[j]])))

        # 3. one positive, one negative, one zero
        if zeros:
            for pos in pos_arr:
                if -pos in neg_set:
                    ans.add((-pos, 0, pos))

        return list(ans)
