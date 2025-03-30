# Although I knew that I had to use heap, I was not sure how to implement it.

# I first thought of the brute force approach, where I would generate all possible pairs and then sort them (with heap sort or any other sorting algorithm) and return the first k pairs. However, this would be inefficient as the time complexity would be O(n*m*log(n*m)), where n and m are the lengths of the two lists.

# Since each input list is sorted, I tried to figure out how to use this property. It is guaranteed that the smallest sum will be the first element of the two lists. The next smallest sum will be either (nums1[0], nums2[1]) or (nums1[1], nums2[0]). So, I used two pointers to keep track of the current index of each list and used a heap to store the pair indices. If these two pairs are the only cases to consider for each and every iteration, there is no need to utilize the heap data structure because we always know which one would be the next pair with the smallest sum (it would be either between nums[i][j+1] or nums[i+1][j]). However, there is one missing case; after writing the below code, it got an error on test cases. Then, while debugging, I realized that I was missing one case.

# Let's say we chose (nums1[0], nums2[1]) as the pair with the second smallest sum. Then, would the next pair be either only between (nums1[0], nums2[2]) or (nums1[1], nums2[1])? No, we also have to consider the leftover from the previous iteration, which would be (nums1[1], nums2[0]). So, we need to keep track of the pairs that we have already considered. This is where the heap comes in. We can use a min-heap to store the sum and the index pair, and pop the smallest sum from the heap for k times. The time complexity of this approach becomes O(k log k), where k <= n*m.

# For more details, refer the markdown file and the LeetCode Editorial.

import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        i = j = 0
        heap = []
        cnt = 0

        while cnt <= k:
            s = nums1[i] + nums2[j]
            elem = (s, (nums1[i], nums2[j]))
            heapq.heappush(heap, elem)

            if i == n-1 and j == m-1:
                break

            if i == n-1:
                j += 1
            elif j == m-1:
                i += 1

            if nums1[i] + nums2[j+1] > nums1[i+1] + nums2[j]:
                i += 1
            else:
                j += 1

            cnt += 1

        return [[n1, n2] for k, (n1, n2) in heap]

# notes while solving:
# k <= 10k

# 1            7  11
#   2   4   6


# 1    4   6   8
#   3    5   7


# 1 2 3 4
#           10 20 30 40
