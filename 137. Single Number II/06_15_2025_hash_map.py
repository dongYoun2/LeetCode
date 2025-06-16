# submission: https://leetcode.com/problems/single-number-ii/submissions/1665519153/

# 1 min
# TC: O(n), where n is the number of elements in nums
# SC: O(n), for the hash map to store the counts of each number


# From LeetCode Top Interview 150 - Bit Manipulation

# The problem statement requires us to solve the problem in linear time and constant space. Even though I knew I had to use a bit manipulation since I chose this problem from the Bit Manipulation section, I couldn't come up with a solution, thinking for an hour. So, I used a hash table to solve in linear time, but not in constant space.

# For a bit manipulation solution, refer to Approaches 4 and 5 in the Editorial section. (Approach 6 also uses bit manipulation, but it covers concepts in Boolean Algebra of Discrete Mathematics and Karnaugh Maps of Digital Logic Design.)


from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cntr = Counter(nums)

        for n, cnt in cntr.items():
            if cnt == 1:
                return n
