# problem: https://leetcode.com/problems/longest-repeating-character-replacement/
# spent around half an hour, but couldn't solve it.


# chose from a neetcode "sliding window" category.

# i attempted directly with a sliding window technique. i tried to expand the window rightward while the current window state satisfies the condition. once the condition is violated, i shrink the window from the left until the condition satisfies again. here, the condition is to keep the same letter using less than or equal to k replacements of other letters. i kept the hash table that records the current window's frequency of each letter.

# now, i struggled to come up with a solution since i was only considering of the approach to check the condition in O(1) time for each window. the only way to achieve this is the "sliding window with a stale maximum frequency" technique, which is the README.md's Approach 3 "Sliding Window (Optimal)"; i think this is really hard to think of at first glance. 

# however, since the string only contains the uppercase english letters, iterating over the hash table is at worst O(26) time; thus, it's totally fine to iterate over the hash table; refer to the README.md's "Sliding Window (Intuitive)" > "Exact `max_freq` (O(26) Recompute per Step)". hopefully, i could solve this problem next time being aware of this.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass
