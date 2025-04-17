# problem: https://leetcode.com/problems/reverse-linked-list-ii/
# submission: https://leetcode.com/problems/reverse-linked-list-ii/submissions/1609028720/

# 54 min
# TC: O(n), where n is the number of nodes in the linked list
# SC: O(n) (for the `nodes` list)

# From LeetCode Top Interview 150 - Linekd List

# The problem was quite tricky and confusing. At first, I tried to implement it in one pass without using extra space (The logic and the code were similar to the C code in the markdown file). However, debugging a null pointer when the left (and also right) is at the left-end (and right-end for the right pointer) was very confusing. It took too much time, and I failed to do so.

# So, I decided to use extra space with an array, which provides the convenience of accessing the nodes by their index. I'm not sure if this is a good practice for solving linked list problems. I will try solving this problem again later without additional space.

# LeetCode Editorial provides two solutions: a Recursive method (Approach 1) and a one-pass iterative method (Approach 2). The recursive method uses O(n) space due to the recursion stack, whereas the iterative method uses O(1) space. Although this iterative method and the C code in the markdown file are both one-pass with constant space, the implementation details are slightly different. For more details, refer to the LeetCode Editorial and the markdown file.

# cf.) I don't really like linked list problems — they are pretty confusing :(


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        assert head is not None

        nodes = [None]
        cnt = 1
        curr = head
        while curr is not None:
            nodes.append(curr)
            cnt += 1
            curr = curr.next

        nodes.append(None)

        for i in range(left, right + 1):
            nodes[i].next = nodes[i-1]

        if left != 1:
            nodes[left-1].next = nodes[right]

        nodes[left].next = nodes[right+1]


        return head if left != 1 else nodes[right]

# notes while solving:
# 0    1 2 3
# None 1 5 None
