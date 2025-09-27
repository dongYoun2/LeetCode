[Problem](https://leetcode.com/problems/palindrome-linked-list/)


## Finding the Middle Node + Reversing Linked List (Solves Follow-up Question)

To solve the follow-up question, which requires solving it in O(1) space, we can first find the middle node ([876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/description/)), and reverse the second half ([206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)). Then, we can compare the two halves to check if they are the same.

The code below is the improved version of the code in `09_27_2025.py`. Three main improvements are made:
1. the reversing linked list part became simpler without separating the logic for the one node case. (`nxt` nees to be initialized to `None` in the beginning, and loop while the `curr` is not `None`.)
2. we reversed the **second half** instead of the first half.
3. the code uses one pass to find the middle node by using the slow and fast pointers.

One point to be aware of is that we need to traverse up to the **second half** (not up to the first half) because the number of nodes in the second half is smaller by one or equal to the number of nodes in the first half, depending on whether the total number of nodes is even or odd.

- [Submission](https://leetcode.com/problems/palindrome-linked-list/submissions/1783853266/) (Runtime: 36 ms, Memory: 34.69 MB)
- TC: $O(n)$, where $n$ is the number of nodes in the linked list.
- SC: $O(1)$

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        assert head is not None


        def find_upper_middle(head: ListNode) -> ListNode:
            slow = fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow


        def reverse(head: ListNode) -> ListNode:
            prev = nxt = None
            curr = head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev


        mid = find_upper_middle(head)
        reversed_second_half = reverse(mid)

        curr1, curr2 = head, reversed_second_half
        # only need to traverse till up to second half (guaranteed that (# first half) - (# second half) is 0 or 1 depending on the total length of the linked list is even or odd)
        while curr2:
            if curr1.val != curr2.val:
                return False

            curr1 = curr1.next
            curr2 = curr2.next

        return True

```


## Using Array to Store Values

Pleae refer to the `11_18_2024.py` file.


## Using Stack

The key is to use the stack to store the first half of the linked list, and then compare the stack values with the second half on the fly while traversing the second half. This requires only **one pass**.

The code below uses `slow` and `fast` pointers to find the middle node instead of counting the number of nodes. One thing I learned here is that we can still know whether the **length of the linked list is odd or even** by checking if the `fast` pointer is `None` or not.

I feel like this is very interview-friendly approach. Mixture of linked list, two pointers, and stack.


- [Submission](https://leetcode.com/problems/palindrome-linked-list/submissions/1783835889/) (Runtime: 28 ms, Memory: 39.04 MB)
- TC: $O(n)$, where $n$ is the number of nodes in the linked list.
- SC: $O(n)$ (for the stack)

```python
from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        assert head is not None
        stack = deque()

        slow = fast = head
        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next

        if fast:    # odd length: skip the middle
            slow = slow.next

        curr = slow # start of the second half
        while curr:
            if stack.pop() != curr.val:
                return False
            curr = curr.next

        return True

```
