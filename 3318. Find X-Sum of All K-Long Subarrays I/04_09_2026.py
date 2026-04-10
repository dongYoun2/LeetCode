# submission: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/submissions/1973955277/
# runtime: 28 ms (beats 25.66%), memory: 19.42 MB (beats 41.89%)
# 36 min

# TC: O((n-k) * (k log k + k)) -> O((n-k) * k log k), where n is the length of the array, and k is the window size
# SC: O(k), for the counter and sorting's temporary space (output space is not considered)


# chose from the "sliding window" topic.

# took longer than expected. spent too much time on understanding the problem and debugging (regarding the last `if` condition).

# i thought of recomputing the entire counter for each window, but knew it's inefficient (but considering the input constraints where 1 <= n <= 50 as well as that the problem level is "easy", it's actually not a problem here). so instead, i manually decrement the leftmost element and increment the new rightmost element of the counter.

# also, i first used the Counter's `most_common()` method to get the top x elements, but in this problem, we cannot use that since there's a requirement that if multiple elements have the same frequency, the bigger number should be considered. (`most_common()` preserves the insertion order). therefore, i used sorting to get the top x elements. 

# though the code below starts with the fixed window size then shrink the leftmost and expand the rightmost, a more interview-friendly implementation is starting directly with the expand-shrink pattern. refer to the README.md's "Expand-Shrink Pattern (Interview-friendly)" section.

# cf.) there's an exact same problem, "3321. Find X-Sum of All K-Long Subarrays II" (https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/), but with the larger input constraints, where n can be at most 100K. in this case, we should reuse the counter (just like in the code below). moreover, i believe we may need to keep a heap (priority queue) data structure to avoid sorting the counter for each window. will attempt this second version in the future.


from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        window_sz = k
        answer = [0] * (n-k+1)

        cntr = Counter(nums[:window_sz])
        for i in range(n-k+1):
            cntr_sorted = sorted(cntr.items(), key=lambda item: (-item[1], -item[0]))
            answer[i] = sum(n*freq for n, freq in cntr_sorted[:x])
            
            cntr[nums[i]] -= 1
            if i+window_sz < n:
                cntr[nums[i+window_sz]] += 1
        
        return answer
