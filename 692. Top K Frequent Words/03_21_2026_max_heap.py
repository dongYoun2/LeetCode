# submission: https://leetcode.com/problems/top-k-frequent-words/submissions/1954882081/
# runtime: 0 ms (beats 100.00%), memory: 19.58 MB (beats 40.20%)
# 14 min
# coded while attempting the follow-up question.

# symbols:
# - n: length of words
# - m: number of unique words
# - k: number of most frequent words to return

# TC: O(n + m + k log m) -> O(m + k log m)
#   - Building Counter: O(n)
#   - Heapify: O(m)
#   - Popping k elements with the heap size of m: O(k log m)
# SC: O(m) (Counter and the heap)


# after solving first using the hash table (counter) and sorting (in 03_21_2026.py), i attempted the follow-up question. i thought of using the heap data structure. so i coded up like below, but realized the time complexity is actually O(m + k log m) instead of O(m log k) (or O(n log k)). to make it to O(m log k), i somehow had to maintain a heap of size k, but i couldn't thinkg of it.

# correct solution can be found in README.md's "Min Heap (Of Size $k$)" section. actually, the technique used in a proper solution is widely used when using heap data structure. i remember i used this algorithm from previous other problem (don't remember which one though), so i should have solved this follow-up question properly.


import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cntr = Counter(words)
        pq = [(-f, w) for w, f in cntr.items()]

        heapq.heapify(pq)

        ans = []
        for _ in range(k):
            _, w = heapq.heappop(pq)
            ans.append(w)
            
        return ans
