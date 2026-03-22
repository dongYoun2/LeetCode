# submission: https://leetcode.com/problems/top-k-frequent-words/submissions/1954867092/
# runtime: 2 ms (beats 61.98%), memory: 19.50 MB (beats 40.20%)
# 9 min

# TC: O(n + m log m), where n is the length of words and m is the number of unique words
# SC: O(m)


# the solution is straightforward. i used hash table (Counter) and sorting to solve this problem.

# cf.) instead of sorting twice, we can simply write `ans.sort(key=lambda e: (-e[1], e[0]))` in python.


from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cntr = Counter(words)
        ans = list(cntr.items())
        ans.sort(key=lambda e: e[0])    # lexico
        ans.sort(key=lambda e: e[1], reverse=True)  # freq

        return [w for w, _ in ans][:k]
