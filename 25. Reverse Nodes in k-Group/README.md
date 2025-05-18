[Problem](https://leetcode.com/problems/reverse-nodes-in-k-group/)

## Iterative Approach (Refactored from `05_18_2025.py`)

This is a more cleaner and readable solution than the original one (`05_18_2025.py`).

Several **notable changes** are:
1. The function that reverses the list segment receives `k` and `next_group_head` as arguments, allowing us to avoid disconnecting the current group from the next group (`kth.next = None` in the original code) and integrating next group's head reconnection logic into the reverse function.
2. Dummy node is used to make the code consistent and cleaner.

Primary advantages of using the **dummy node** are:
1. `prev_tail` never becomes `None` so that `get_kth()` function with `prev_tail` argument can be called without checking if `prev_tail` is `None`. (This is also relevant to `range(k)` in `get_kth()`, not `range(k - 1)`. To use `range(k - 1)`, we would need to check if `prev_tail` is `None` before calling `get_kth()`, which would make the code less readable.)
2. Removes the need for a special case for the first group. We never have to manually assign the modified list's head to the answer variable on the very first reversal (`if ans is None: ans = new_head` in the original code). Instead, we can simply return dummy.next.

- [Submission](https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/1638234847/) (Runtime: 0 ms, Memory: 18.8 MB)
- TC: $O(n)$, where $n$ is the number of nodes in the linked list.
- SC: $O(1)$.
<br>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        assert head is not None
        if k < 2: return head

        # returns the k-th node **after** `node` (equivalent as (k+1)th node from `node`), or returns None if there aren’t k nodes left
        def get_kth(node):
            assert node is not None
            curr = node
            for _ in range(k):
                curr = curr.next
                if not curr: return None

            return curr


        def reverse_segment(head: ListNode, k: int, successor: Optional[ListNode]):
            """
            Reverse exactly k nodes starting at head, linking the end to successor.
            Returns (new_head, new_tail).
            """
            prev, curr = successor, head
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            return prev, head


        dummy = ListNode(0, head)
        prev_tail = dummy

        kth = get_kth(prev_tail)
        while kth:
            # mark where the next group will start (successor == None when the number of nodes divides evenly by k)
            successor = kth.next
            curr_start = prev_tail.next

            new_head, new_tail = reverse_segment(curr_start, k, successor)

            # reconnect with previous group's tail node
            prev_tail.next = new_head
            prev_tail = new_tail

            kth = get_kth(new_tail)

        return dummy.next

```

## Recursive Approach

Notice that we use `range(k - 1)` in the `get_kth()` function here. Recursive code is more readable than the iterative one, but it requires additional space due to the recursion stack.

- [Submission](https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/1638236108/) (Runtime: 1 ms, Memory: 18.5 MB)
- TC: $O(n)$.
- SC: $O(n/k)$. We process $k$ nodes at each and every recursion level.
<br>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        assert head is not None
        if k < 2: return head

        # returns the k-th node from `node` (returns None if there aren’t k nodes left)
        def get_kth(node):
            assert node is not None
            curr = node
            for _ in range(k - 1):
                curr = curr.next
                if not curr: return None

            return curr


        def reverse_segment(head: ListNode, k: int, successor: Optional[ListNode]):
            """
            Reverse exactly k nodes starting at head, linking the end to successor.
            Returns (new_head, new_tail).
            """
            prev, curr = successor, head
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            return prev, head


        def helper_reverse_k_group(node: ListNode, k: int) -> ListNode:
            if node is None: return None

            kth = get_kth(node)
            if kth is None: return node # keeping the left-out nodes as is

            successor = kth.next
            new_head, new_tail = reverse_segment(node, k, successor)

            # reconnect with next group
            new_tail.next = helper_reverse_k_group(successor, k)

            return new_head


        return helper_reverse_k_group(head, k)

```