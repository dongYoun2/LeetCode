# submission: https://leetcode.com/problems/odd-even-linked-list/submissions/1968019186/
# runtime: 0 ms (beats 100.00%), memory: 21.32 MB (beats 6.30%)
# 17 min

# TC: O(n), where n is the number of nodes in the linked list
# SC: O(1)
# the above complexities are required from the problem statement.


# the below approach is pretty straightforward. we build two separate linked lists (odd and even), then merge them. one caveat is we need `even_curr.next = None` at the end. Otherwise, we may have a cycle in the merged linked list.

# another method that uses less memory than this approach is to rewire the nodes in-place while taversing the main linked list. for details, refer to the submission: https://leetcode.com/problems/odd-even-linked-list/submissions/1968030020/ — runtime: 0 ms (beats 100.00%), memory: 20.82 MB (beats 99.51%)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_curr = odd_dummy = ListNode(-1)
        even_curr = even_dummy = ListNode(-1)

        curr = head
        while curr is not None and curr.next is not None:
            odd_curr.next = curr
            even_curr.next = curr.next

            odd_curr = odd_curr.next
            even_curr = even_curr.next

            curr = curr.next.next
        
        if curr:
            odd_curr.next = curr
            odd_curr = odd_curr.next
            assert odd_curr.next is None
        
        odd_curr.next = even_dummy.next
        even_curr.next = None
        return odd_dummy.next
