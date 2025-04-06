# problem: https://leetcode.com/problems/group-anagrams/
# submission: https://leetcode.com/problems/group-anagrams/submissions/1598766103/

# 15 min
# TC: O(N * K log K) where N is the number of strings and K is the maximum length of a string
# SC: O(N * K)

# Knew that I had to use a hash map since I am solving problems based on the algorithm type.

# Below, I used sorted string as the key to group anagrams together. However, this can be improved by using a tuple of counts of each character as the key, which leads to a O(N*K) time complexity. For details, refer to the LeetCode Editorial.

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for s in strs:
            key_ = "".join(sorted(s))
            anagram_dict[key_].append(s)

        return list(anagram_dict.values())
