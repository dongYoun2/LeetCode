# problem: https://leetcode.com/problems/simplify-path/
# submission: https://leetcode.com/problems/simplify-path/submissions/1603832194

# 13 min
# TC: O(n), where n is the length of the path string
# SC: O(n)

# From LeetCode Top Interview 150 - Stack

# Feel like it's important to consider many possible cases.


from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        print(dirs)

        stack = deque()

        for dir_name in dirs:
            if dir_name == "" or dir_name == ".": continue
            elif dir_name == "..":
                if not stack: continue

                stack.pop()
            else:
                stack.append(dir_name)

        ans = "/" + "/".join(stack)

        return ans
