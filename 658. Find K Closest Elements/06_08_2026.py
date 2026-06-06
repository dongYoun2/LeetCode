# submission: https://leetcode.com/problems/find-k-closest-elements/description/
# runtime: 48 ms (beats 19.23%), memory: 20.90 MB (beats 34.36%)
# 21 min
# solved using linear search (the closest element to `x`) + two pointers approach

# TC: O(n + k), where n is the length of the array and k is the number of closest elements to return
# SC: O(1)


# chose from a neetcode "sliding window" category.

# though i chose from the "sliding window" category, this problem is not essentially a sliding window problem. there are several approaches to solve this problem:
# 1. Sort by distance, take k, sort result
# 2. Linear scan closest + expand outward (the code below is this approach)
# 3. Binary search closest + expand outward
# 4. Remove farther endpoint until size k
# 5. Binary search on window start

# the first, third, and fifth approaches are described in the README.md.

# cf.) in the code below, `if r-l+1 == k: break` block is not necessary since the while loop has the exact same condition. also, this code is messy and not that readable. the improved version using the same "linear scan closest + expand outward" approach can be found here: https://leetcode.com/problems/find-k-closest-elements/submissions/2026698837/.


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        closest = float('inf')

        def get_closer(a, b):
            aa, bb = abs(a-x), abs(b-x)
            if aa < bb:
                return a
            elif aa > bb:
                return b
            return min(a, b)

        pos = 0
        for i in range(n):
            closest = get_closer(closest, arr[i])
            if closest == arr[i]:
                pos = i

        l = r = pos
        while 0 <= l-1 and r+1 < n and r-l+1 < k:
            c = get_closer(arr[l-1], arr[r+1])

            if c == arr[l-1]:
                l -= 1
            else:
                r += 1
            
            if r-l+1 == k:
                break
        
        if l == 0:
            return arr[:k]
        elif r == n-1:
            return arr[-k:]
        
        return arr[l:r+1]
