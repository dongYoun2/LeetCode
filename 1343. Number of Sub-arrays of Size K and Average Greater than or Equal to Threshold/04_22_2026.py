# submission: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/submissions/1985304887/
# runtime: 67 ms (beats 17.22%), memory: 30.97 MB (beats 11.03%)
# 5 min

# TC: O(n)
# SC: O(1) (temporary space for a slice is not considered)


# chose from a neetcode "sliding window" category.

# it's a pretty straightforward sliding window problem.

# brute-force solution would be recomputing the sum of each subarray (or the window) of size k every time, which takes O(n*k) time. since k can be at most n, the worst case becomes O(n^2) time.

# with the sliding window technique, we can compute the sum of the current window in constant time by adding the new element and subtracting the leftmost element.

# cf.) instead of computing the average which requires division, we can simply compare the sum with the threshold * k. this code's submission can be found here: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/submissions/1985306566/


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        curr_sum = sum(arr[:k])
        ans = int(curr_sum / k >= threshold)

        for i in range(n-k):
            curr_sum += - arr[i] + arr[i+k]
            ans += int(curr_sum / k >= threshold)
        
        return ans
