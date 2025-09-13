# submission: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1768839893/
# runtime: 11 ms, memory: 17.7 MB

# 16 min

# from the input range constraint, i noticed this problem has to be solved in O(n log n) time, and since it didn't seem like requiring sorting, or binary search logics, which generally has log n term in time complexity, i though this can be solved in O(n) time. trying with additional example ('dbcb') other than given in the test cases, i found out i can solve it with the sliding window technique.

# cf.) one little thinkg i learned here is taht the python's set discard() and remove() are slightly different. discard() does nothing if the element is not in the set, while remove() raises a KeyError if the element is not in the set.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0

        front = rear = 0
        ans = 0
        bag = set()

        while rear < n:
            if s[rear] not in bag:
                bag.add(s[rear])
                ans = max(ans, rear - front + 1)
            else:
                while s[front] != s[rear]:
                    bag.discard(s[front])
                    front += 1

                front += 1

            rear += 1

        return ans


# notes while solving:
# dbcb
