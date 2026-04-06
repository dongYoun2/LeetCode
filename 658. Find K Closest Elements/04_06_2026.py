# submission: https://leetcode.com/problems/find-k-closest-elements/submissions/1970943548/
# runtime: 16 ms (beats 36.79%), memory: 20.63 MB (beats 71.21%)
# 14 min

# TC: O(log n + k log k), where n is the length of the array
# - O(log n): binary search
# - O(k): expanding pointers (or window)
# - O(k log k): sorting the answer array
# SC: O(1) (output array is not considered)


# this solution uses binary search + two pointers approach.

# from the problem constraints, i first assumed the problem should be solved in O(n log n) time. i noticed that i need to find the element closest to the `x`, then expand the left and right pointers from there to find all the k closest elements. to achieve this, i used binary search (instead of linear search), and inserted the closest elements one by one to the `ans` array while expanding the pointers. because the insertion order is not guaranteed to be ascending, i need to sort the `ans` array at the end, which requires additional O(k log k) time.

# one improvement we can make is that instead of inserting the closest elements one by one to the `ans` array, we can simply expand two pointers until the window size reaches k, and then return the window (i.e. return `nums[l+1:r]`). this removes the extra sorting step so that the final TC becomes O(log n + k). refer to the README.md's second approach for this optimized version.


import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pos = bisect.bisect_left(arr, x)
        ans = []
        l, r = pos - 1, pos
        while k > 0 and l >= 0 and r < len(arr):
            
            assert arr[l] < x
            assert arr[r] >= x

            if arr[r] - x < x - arr[l]:
                ans.append(arr[r])
                r += 1
            else:
                ans.append(arr[l])
                l -= 1
            
            k -= 1

        if k > 0:
            if l >= 0:
                ans.extend(arr[l+1-k:l+1])
            else:
                ans.extend(arr[r:r+k])

        ans.sort()
        
        return ans
