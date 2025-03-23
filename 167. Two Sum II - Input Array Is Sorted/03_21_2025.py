# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

# took 6 min
# n: the number of elements in numbers array
# TC: O(n)
# SC: O(1) (this has to be satisifed, which was required from the question)

# Tried to figure out how to solve the question using constant extra space. Since the array is already sorted, I assumed this property has to be used. So I started to think of binary search at first, but realized this problem cannot be solved with it.

# Then, I started to think of a two-pointer algorithm. I realized that I could find two numbers by iteratively modifying the two front and rear pointers.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]

            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:   # s == target
                return [l+1, r+1]
