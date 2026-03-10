# submission: https://leetcode.com/problems/maximum-product-subarray/submissions/1944330381/
# runtime: 4 ms (beats 60.68%), memory: 19.86 MB (beats 70.63%)
# 53 min

# TC: O(n), where n is the length of the nums array
# SC: O(1)


# i solved with a sliding window approach. however, typical algorithms would be dynamic programming or prefix-suffix scan (refer to the README.md for these approaches).

# looking at the constraint that the maximum length of the array is 2 * 10^4, i assumed that i need to solve it in O(n log n) time. there seems to be no part where sorting is needed, so i expected the solution to have O(n) time complexity. i thought of DP approach as well, but i am not sure why but i was more toward to the two-pointer or sliding window approach.

# first, dividing the case where the array contain zeros or not, i tried to figure out how to track the maximum product. in the mean time, i realized i can apply the same algorithm for finding the maximum product for the case where the array contains no zeros to each segment array separated by zeros for the case where the array contains zeros, then find the maximum product among all segments. this idea can be implemented by either prefix-suffix scan or sliding window (the code below), though it's much more concise and straightforward to implement with a prefix-suffix scan.

# though i solved it, it took long and i fee like i didn't thoroughly implemented following a systematic approach or a rigorous logic (or thinking process). hope i can solve it better next time.

# cf.) i added comments to the code below with the help of ChatGPT.


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        start = end = 0

        # curr = product of current window [start, end]
        # ans  = best product seen so far
        ans = curr = nums[0]

        # If first element is zero, treat it as a segment boundary.
        # Reset product to 1 so we can start multiplying the next segment.
        if nums[0] == 0:
            ans = 0
            curr = 1
            start = 1
        else:
            ans = curr = nums[0]
            start = 0

        def shrink_window():
            nonlocal curr, ans, start, end
            # After finishing a segment (or before a zero),
            # repeatedly remove elements from the left.
            # This enumerates all suffix products of the segment.
            # equality is needed; if not, test case [-2,1,0] will fail.
            while curr <= ans and abs(curr) >= abs(ans) and start < end:
                curr //= nums[start]        # exact division since curr was built by multiplication
                ans = max(ans, curr)       # check this suffix product
                start += 1                 # move window start right

        for i in range(1, len(nums)):
            if nums[i] == 0:
                # Zero splits the array into independent segments.
                shrink_window()            # evaluate suffixes of the previous segment
                curr = 1                   # reset product for next segment
                ans = max(ans, 0)          # zero itself can be the answer
                start = i + 1
                continue
            
            end = i
            curr *= nums[end]              # extend window product (prefix scan)
            ans = max(ans, curr)           # check prefix product

        shrink_window()                    # process suffixes of the final segment

        return ans
