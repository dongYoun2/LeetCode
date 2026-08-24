[Problem](https://leetcode.com/problems/palindrome-linked-list/)


## Find Middle (with Fast & Slow Pointers) + Reverse Second half (solves Follow-up Question)

To solve the follow-up question, which requires solving it in O(1) space, we can first find the middle node ([876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/description/)), and reverse the second half ([206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)). Then, we can compare the two halves to check if they are the same.

The code below is the improved version of [09_27_2025.py](./09_27_2025.py). Three main improvements are:
1. the reversing linked list part became simpler without separating the logic for the one node case. (`nxt` nees to be initialized to `None` in the beginning, and loop while the `curr` is not `None`.)
2. Reverse the **second half** instead of the first half.
3. the code uses one pass to find the middle node by using the slow and fast pointers.

One point to be aware of is that we need to traverse up to the **second half** (not up to the first half) because the number of nodes in the second half is smaller by one or equal to the number of nodes in the first half, depending on whether the total number of nodes is even or odd. This is mainly because when we are finding the middle node, both `fast` and `slow` pointers are initialized to the `head`, which makes `slow` pointer become the second one if there are two middle nodes (when the total number of nodes is even).

cf.) The typical approach to find the first middle node when the total number of nodes is even is to initialize `slow` to `head` and `fast` to `head.next` in the beginning. i din't know this until now, so we can see that i used `dummy` node to find the first middle node (refer to the [08_24_2026.py](./08_24_2026.py)).


[Submission](https://leetcode.com/problems/palindrome-linked-list/submissions/1783853266/)—Runtime: 36 ms (beats 50.42%), Memory: 34.69 MB (beats 99.94%)


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


## Find Middle (with Fast & Slow Pointers) + Stack

The key is to use the stack to store the first half of the linked list, and then compare the stack values with the second half on the fly while traversing the second half. This requires only **one pass**.

The code below uses `slow` and `fast` pointers to find the middle node instead of counting the number of nodes. One thing I learned here is that we can still know whether the **length of the linked list is odd or even** by checking if the `fast` pointer is `None` or not.

I feel like this is very interview-friendly approach. Mixture of linked list, two pointers, and stack.


[Submission](https://leetcode.com/problems/palindrome-linked-list/submissions/1783835889/)—Runtime: 28 ms (beats 71.82%), Memory: 39.04 MB (beats 97.10%)

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


## Array-Based Palindrome Check

Pleae refer to the [11_18_2024.py](./11_18_2024.py) file.


## Convert to Doubly Linked List + Two-End Traversal

Though we can convert the singly linked list to a doubly linked list, and compare the values from the two ends simultaneously, this is not recommended since it mutates the original input.

[Submission](https://leetcode.com/problems/palindrome-linked-list/submissions/1456439095/)—Runtime: 24 ms (beats 78.83%), Memory: 46.65 MB (beats 43.40%)


- TC: $O(n)$
- SC: $O(n)$ (since we add a `prev` reference to each node)


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        curr = head
        node_len = 1

        while curr.next is not None:
            prev = curr
            curr = curr.next
            curr.prev = prev
            node_len += 1

        forward_curr = head
        backward_curr = curr
        for i in range(node_len // 2):
            if forward_curr.val != backward_curr.val:
                return False
            
            forward_curr = forward_curr.next
            backward_curr = backward_curr.prev
        
        return True

```