# problem: https://leetcode.com/problems/copy-list-with-random-pointer/
# submission: https://leetcode.com/problems/copy-list-with-random-pointer/submissions/1608672045/

# 25 min
# TC: O(n + n) -> O(n), where n is the number of nodes
# SC: O(n + n) -> O(n) (for `node_to_idx` and `cp_node_list`)

# From LeetCode Top Interview 150 - Linekd List


# I think the most important idea is how to copy the random pointers. Since random pointers that I need to copy may not be copied yet, I used a dictionary to map the node address to the index in the linked list during the first pass. Then, I was able to use this hash table to assign the random pointers of the copied nodes in the second pass.

# LeetCode Editorial provides slightly different approaches. The basic idea that the hash table has to be used is the same, but one of the approaches (Approach 1) uses the "visited" dictionary with the recursive method (Approach 2 converts this approach 1 into the one-pass iterative approach.). Although using the hash table could ease the implementation with O(n) space, this problem could be implemented with the one-pass iterative approach in O(1) space (Approach 3). For more details, refer to the LeetCode Editorial.


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
        node_to_idx = {}
        cp_node_list = []

        ptr = head
        cnt = 0
        ans = curr = Node(-1)  # dummy node
        while ptr is not None:  # copy normal linked list
            node = Node(ptr.val)
            cp_node_list.append(node)

            curr.next = node
            curr = curr.next

            node_to_idx[id(ptr)] = cnt
            cnt += 1

            ptr = ptr.next

        # consider (last) null node as well
        node_to_idx[id(None)] = cnt
        cp_node_list.append(None)

        ptr = head
        curr = ans.next
        while ptr is not None:  # copy random pointers
            id_random = id(ptr.random)
            idx = node_to_idx[id_random]
            node_random = cp_node_list[idx]

            curr.random = node_random
            curr = curr.next

            ptr = ptr.next


        return ans.next
