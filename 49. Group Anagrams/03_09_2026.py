# submission: https://leetcode.com/problems/group-anagrams/submissions/1943309355/
# runtime: 19 ms (beats 22.59%), memory: 24.04 MB (beats 17.04%)
# 12 min

# TC: O(N * K), where N is the number of strings and K is the maximum length of a string
# SC: O(N * K)


# this solution uses a frequency array as a key for the hash map (note that "04_06_2025.py" uses a sorted string as a key). though this solution has a better time complexity than the "04_06_2025.py", the runtime in practice seems to be slower; maybe it's because of the python overhead? (according to GPT, repeated dictionary lookups are expensive)


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            key = [0] * (ord('z') - ord('a') + 1)
            for c in word:
                key[ord(c) - ord('a')] += 1
            group[tuple(key)].append(word)

        return list(group.values())
