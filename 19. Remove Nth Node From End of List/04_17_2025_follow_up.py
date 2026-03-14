# submission: https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1609502562/
# runtime: 0 ms (beats 100.00%), memory: 17.72 MB (beats 100.00%)
# 7 min
# this solution solves the follow-up question but with extra space. i think the purpose of this question is to make us think about the two-pointer approach. for that, refer to the markdown file.

# TC: O(n), where n is the number of nodes in the linked list (one-pass alg.)
# SC: O(n) (`nodes` array)

# From LeetCode Top Interview 150 - Linekd List

# The follow-up question requires solving it in one pass. I used the `nodes` array to allow the indexing of the node to be removed. However, using an array for the convenience of indexing in the linked list-related problems is usually not the best solution nor a good practice since it requires the additional O(n) space. Instead, the two-pointer approach can also be done in one pass with constant space (markdown file).


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        nodes.append(None)  # to make the logic consistent when only one node exists

        if len(nodes) - 1 == n: # remove the first node
            return nodes[1]

        nodes[-n-2].next = nodes[-n]    # index has to be -(n+1)-1 since null ptr is appended at the end of the array


        return head