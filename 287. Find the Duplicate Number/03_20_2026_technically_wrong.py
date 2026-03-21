# submission: https://leetcode.com/problems/find-the-duplicate-number/submissions/1954068031/
# though the submission is accepted, this solution doesn't actually meet the constant space requirement.
# runtime: 305 ms (Beats 5.01%), memory: 33.40 MB (Beats 84.88%)
# 44 min

# TC: O(n)
# SC: O(n); O(1) when n <= 32


# i intuitively thought of using bit manipulation with XOR operation when i saw the requirement of constant space. it took 44 minutes to solve, though i realized this is not a true constant space solution after submitting. 

# i directly attempted with XOR bitwise operation, but couldn't figure out. spending time too much, i decided to first think of a brute force solution using hash table (or set) without caring about the space complexity requirement. the algorithm is straightforward; we put the numbers in a set while iterating through `nums` and once we find the number that is already in the set, we can directly return it. that would be the answer. 

# since set uses O(n) space, i tried to convert this set into a bit table (i.e., a list of bits; `table` in the below code). first, by XORing the bit table and the current number (technically, the bit mask of the current number; `mask` in the below code), we can flip the corresponding bit of the bit table. then, if that bit becomes 0, which means it's flipped back to the original state or appeared twice (we can check this with `table & mask == 0`), we can ensure the current number is the answer or the duplicate number.

# however, this solution uses constant space only when n <= 32 because we use one integer variable as a bit table. this solution works since python doesn't bound the size of integers, but it won't work in other languages.

# MAIN TAKEAWAY: if an optimized solution doesn't come to mind directly, it's often better to first start with a brute force solution, then trying to optimize from there!

# cf.) for a correct solution, refer to the README file.


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        table = 0
        for n in nums:
            mask = 1 << n
            table ^= mask

            if table & mask == 0:
                return n
