# submission: https://leetcode.com/problems/copy-list-with-random-pointer/submissions/1794259747/
# runtime: 42 ms, memory: 18.83 MB

# 30 min
# TC: O(n), where n is the number of nodes in the linked list
# SC: O(n)

# to come up with an idea is not that difficult, but implementing takes quite a bit of time.

# cf.) for more readable, concise, and interview-friendly code as well as the O(1) space solution, refer to the markdown file.


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
        node_addr_arr = []
        cp_node_arr = []

        cp_ptr = dummy = Node(-10001)   # dummy node
        orig_ptr = head
        while orig_ptr:
            node_addr_arr.append(id(orig_ptr))

            new_node = Node(orig_ptr.val)
            cp_node_arr.append(new_node)

            cp_ptr.next = new_node

            cp_ptr = cp_ptr.next
            orig_ptr = orig_ptr.next

        addr_to_idx = {addr: i for i, addr in enumerate(node_addr_arr)} # original list
        cp_idx_to_node = {i: node for i, node in enumerate(cp_node_arr)}    # copied list

        cp_ptr = dummy.next
        orig_ptr = head
        while orig_ptr:
            if not orig_ptr.random:
                cp_ptr.random = None
            else:
                rand_node_addr = id(orig_ptr.random)
                rand_node_idx = addr_to_idx[rand_node_addr]

                cp_rand_node = cp_idx_to_node[rand_node_idx]
                cp_ptr.random = cp_rand_node

            orig_ptr = orig_ptr.next
            cp_ptr = cp_ptr.next

        return dummy.next
