[Problem](https://leetcode.com/problems/copy-list-with-random-pointer/description/)



## Hash Table Approach

This approach uses a hashmap to map each original node to its clone in two simple passes.


- [Submission](https://leetcode.com/problems/copy-list-with-random-pointer/submissions/1794296806/) (Runtime: 50 ms, Memory: 18.6 MB)
- TC: $O(n)$, where $n$ is the number of nodes in the linked list.
- SC: $O(n)$

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 1) Clone all nodes (just values); remember old->new mapping
        old_to_new = {}
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # 2) Use the map to wire next/random pointers
        cur = head
        while cur:
            clone = old_to_new[cur]
            clone.next = old_to_new.get(cur.next)     # None if cur.next is None
            clone.random = old_to_new.get(cur.random) # None if cur.random is None
            cur = cur.next

        return old_to_new[head]
```


## Interleaving Nodes Approach (O(1) space)

The code below has three steps:
1. Interleave clones with originals
2. assign randoms
3. then detach

This approach solves the problem in $O(1)$ space.

- [Submission](https://leetcode.com/problems/copy-list-with-random-pointer/submissions/1794300119/) (Runtime: 44 ms, Memory: 18.64 MB)
- TC: $O(n)$
- SC: $O(1)$

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 1) A->A'->B->B'->...
        cur = head
        while cur:
            nxt = cur.next
            cur.next = Node(cur.val, nxt)
            cur = nxt

        # 2) Set random for clones
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 3) Detach clone list
        cur, pseudo = head, head.next
        copy_head = pseudo
        while cur:
            cur.next = pseudo.next
            pseudo.next = pseudo.next.next if pseudo.next else None
            cur = cur.next
            pseudo = pseudo.next

        return copy_head

```